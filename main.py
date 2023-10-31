import smtplib
import sqlite3
from email.message import EmailMessage

import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pandas_schema import Schema, Column
from pandas_schema.validation import IsDtypeValidation, DateFormatValidation

import setting


def get_email_client() -> object:
    """
    Get email client
    :return: email client to send email
    """
    print(setting.EMAIL)
    server = smtplib.SMTP(
        setting.EMAIL['host'], setting.EMAIL['port']
    )
    server.starttls()
    server.login(
        setting.EMAIL['user'], setting.EMAIL['password']
    )

    return server


def email_render(average: dict, template_name: str) -> str:
    """
    Render email template
    :param average:
    :param template_name:
    :return:
    """
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template(template_name)

    return template.render(average)


def send_email(user_email: str, average: dict) -> dict:
    """
    Send email to user
    :param user_email:
    :param average:
    :return:
    """
    email_client = get_email_client()
    email = EmailMessage()
    email['Subject'] = 'Summary Story account'
    email['From'] = setting.EMAIL['sender']
    email['To'] = user_email
    email.set_content(
    email_render(average, 'summary_email.html'),
        subtype='html'
    )

    return email_client.send_message(email)


def get_df_from_file(file_path: str) -> [bool, object]:
    """
    Open file and return pandas dataframe
    :param file_path: path to file
    :return: pandas dataframe
    """
    df = pd.read_csv(
        file_path,
        parse_dates=['Date'],
        dtype={'Transaction': float, 'Id': int}
    )

    schema = Schema([
        Column('Id', [IsDtypeValidation(int)]),
        Column('Date', [DateFormatValidation('%Y-%m-%d')]),
        Column('Transaction', [IsDtypeValidation(float)])
    ])

    errors = schema.validate(df)
    if errors:
        for error in errors:
            print(error)
        return False, None
    return True, df


def get_average_from_df(df: object) -> dict:
    """
    Get average from dataframe
    Total balance / number of transactions
    Number of transactions group by month
    Average debit amount:
    Average credit amount:
    :return
    dict with average values
    """
    average = {
        'total_balance': df['Transaction'].sum(),
        'number_of_transactions': df['Transaction'].count(),
        'average_debit_amount': df[df['Transaction'] < 0]['Transaction'].mean(),
        'average_credit_amount': df[df['Transaction'] > 0]['Transaction'].mean(),
        'number_of_transactions_group_by_month': df.groupby(
           df['Date'].dt.strftime('%B')
        )['Transaction'].count().to_dict()
    }

    return average


def save_df_to_sql(df, table_name='transactions'):
    con = sqlite3.connect('transactions.db')
    df.to_sql(table_name, con, if_exists='replace', index=False)


def prosses_file(user_email, file_path):
    print('get_df_from_file')
    success, df = get_df_from_file(file_path)
    if not success:
        raise Exception('Error in file')
    print('save_df_to_sql')
    save_df_to_sql(df)
    print('get_average')
    average = get_average_from_df(df)
    print('send_email')
    send_email(user_email, average)
    print('Done')


if __name__ == '__main__':
    user_email = setting.SUMMARY_USER
    file_path = setting.FILE_PATH

    prosses_file(user_email, file_path)
