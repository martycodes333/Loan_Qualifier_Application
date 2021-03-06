# Import pathlib
from pathlib import Path


#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators


# Import save_csv util
from qualifier.utils.fileio import save_csv


def test_save_csv():
    

    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    qualifying_loans = "test" # Give qualifying loans variable a value to be passed into the Test CSV
    csvpath = Path("./tests/qualifying_loans.csv")

    fileio.save_csv(csvpath, qualifying_loans)
       

    assert csvpath.exists()
    
   


def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84


    # @TODO: Test the new save_csv code!
   