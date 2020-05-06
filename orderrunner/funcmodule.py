import sys
import numpy as np
import pandas as pd


def header(msg):
    """Prints a header message.

    Arguments:
        msg {string} -- The message to be printed.
    """
    print("*" * len(msg))
    print(msg)
    print("*" * len(msg))


def get_content(csv_file):
    """Uses Pandas to try and read the csv file sent as argument.

    Arguments:
        csv_file {string} -- The path to the file.
    """
    pd.set_option('display.max_rows', None)
    try:
        df = pd.read_csv(csv_file, sep=";")
        calc_order_per_company_desc(df)
        calc_cars_ordered_desc(df)
        calc_most_populare_per_company(df)
    except FileNotFoundError:
        err_msg = "The file you entered could not be found."
        print(err_msg)


def calc_order_per_company_desc(df):
    """Counts the number of occurrenses of a company id to calculate number of orders.


    Arguments:
        df {dict} -- A pandas dataframe which is a dict-like container for series.
    """
    header_text = "Table 1: Orders per company, descending order"
    opc = df['company_id'].value_counts()
    opc = opc.reset_index()
    opc.columns = ['Company_id', 'Orders']

    print_result(opc, header_text)


def calc_cars_ordered_desc(df):
    """Counts the number of occurenses of a car to calculate orders per car.

    Arguments:
        df {dict} -- A pandas dataframe which is a dict-like container for series.
    """
    header_text = "Table 2: Cars ordered by amount, descending order"
    coba = df['car'].value_counts()
    coba = coba.reset_index()
    coba.columns = ['Car', 'Amount']

    print_result(coba, header_text)


def calc_most_populare_per_company(df):
    """Counts the number of the same car ordered by 
        each company to find the most populare one per company

    Arguments:
        df {dict} -- A pandas dataframe which is a dict-like container for series.
    """
    header_text = "Table 3: Most populare car per company"
    mpc = (df.groupby(['company_id', 'car'])['car'].agg(['count']).sort_values(
        by='count', ascending=False).reset_index().drop_duplicates('company_id', keep='first'))

    print_result(mpc, header_text)


def print_result(table_data, header_text):
    """prints the result of a calculation.

    Arguments:
        table_data {dict} -- A pandas dataframe which is a dict-like container for series.
        header_text {string} -- The message to be printed over a table.
    """
    header(header_text)
    print(table_data)
