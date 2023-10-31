import unittest

import pandas as pd

from main import get_average_from_df, get_df_from_file, save_df_to_sql, prosses_file


class TestYourFunctions(unittest.TestCase):
    def test_get_average_from_df(self):
        # Create a sample DataFrame for testing
        data = {
            'Id': [1, 2, 3, 4, 5],
            'Date': ['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01', '2023-03-01'],
            'Transaction': [100.0, -50.0, 25.0, -75.0, 80.0]
        }
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

        # Test the get_average_from_df function
        result = get_average_from_df(df)

        self.assertEqual(result['total_balance'], 80.0)
        self.assertEqual(result['number_of_transactions'], 5)
        self.assertAlmostEqual(result['average_debit_amount'], -62.5)
        self.assertAlmostEqual(result['average_credit_amount'], 68.33333333333333)
        self.assertEqual(result['number_of_transactions_group_by_month']['January'], 2)
        self.assertEqual(result['number_of_transactions_group_by_month']['February'], 2)
        self.assertEqual(result['number_of_transactions_group_by_month']['March'], 1)

    def test_get_df_from_file(self):
        # Test the get_df_from_file function with a sample CSV file
        success, df = get_df_from_file('data/txns.csv')

        self.assertTrue(success)
        self.assertIsInstance(df, pd.DataFrame)

    def test_save_df_to_sql(self):
        # Create a sample DataFrame for testing
        data = {'Id': [1, 2, 3, 4, 5],
                'Date': ['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01', '2023-03-01'],
                'Transaction': [100.0, -50.0, 25.0, -75.0, 80.0]}
        df = pd.DataFrame(data)

        # Test the save_df_to_sql function
        save_df_to_sql(df, table_name='test_table')

    def test_prosses_file_call_all_functions(self):
        # Test the prosses_file function
        # TMB mock all functions adn check if they were called whit the correct parameters
        pass

    def test_prosses_file_raise_exception(self):
        # Test the prosses_file function
        # TMB mock all functions adn check if they were called whit the correct parameters
        pass

    def test_send_email(self):
        # Test the send_email function
        # TMB mock  functions adn check if they were called whit the correct parameters
        pass

    def test_build_email(self):
        # Test the build_email function
        # TMB mock  functions adn check if they were called whit the correct parameters and if return the build email
        pass

    def test_send_email(self):
        # Test the send_email function
        # TMB mock  functions adn check if they were called whit the correct parameters
        pass
