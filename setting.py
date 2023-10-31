import os

EMAIL = {
    'host': os.environ.get('EMAIL_HOST', 'smtp.gmail.com'),
    'port': os.environ.get('EMAIL_PORT', 587),
    'sender': os.environ.get('EMAIL_SENDER', 'skomlev.ruso@gmail.com'),
    'user': os.environ.get('EMAIL_USER', 'skomlev.ruso@gmail.com'),
    # https://support.google.com/accounts/answer/185833?hl=es&sjid=14820134242632080947-SA
    'password': os.environ.get('EMAIL_PASSWORD', "yzcb zzjw hvna cgis "),
}

FILE_PATH = os.environ.get('FILE_PATH', 'data/txns.csv')
SUMMARY_USER = os.environ.get('SUMMARY_USER', 'skomlev.ruso+user@gmail.com')
