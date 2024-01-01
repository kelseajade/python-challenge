
import os

import csv

budgetdata = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budgetdata) as budgetdata:

    print(budgetdata)

    csvheader = next(budgetdata)

    print(f"CSV Header: {csvheader}")


