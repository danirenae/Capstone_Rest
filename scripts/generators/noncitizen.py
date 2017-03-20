import csv
import sqlite3


def get_noncitizen_data_parse_into_lists(NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015):
    """
    Method that will read from the CSV file titled NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015
    and parse CSV data into lists by line
    Author: Dani Adkins
    """
    with open(NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015, "r", encoding="latin-1") as noncitizen_data:
        for noncitizen_data in csv.reader(noncitizen_data):
            yield noncitizen_data

if __name__ == '__main__':
    filename = "../excel_files/NonCitizenPrisonersAndPrisonersAge17AndUnderBySex2015.csv"
    iter_data = iter(get_noncitizen_data_parse_into_lists(filename))
    next(iter_data)

    with sqlite3.connect("../../db.sqlite3") as db:
        cursor = db.cursor()

        for row in iter_data:
            state = row[1]
            total_noncitizen = row[2]
            total_minor = row[6]

            print(state, total_minor, total_noncitizen)

            # cursor.execute("""
            #         UPDATE capstone_api_statedata
            #         SET total_noncitizen,total_minor
            #         WHERE state=state

            #         (state, total_private, total_local_jail)VALUES
            #         (null, '{}', {}, {})
            #         """.format(total_noncitizen, total_minor))















