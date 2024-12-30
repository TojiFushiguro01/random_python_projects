import pytest
import os
import csv
from project import validate_response, register


def test_register():
    # Test data
    account_name = "test_account"

    # Call the register function
    register(account_name)

    # Check if balance file exists and contains "0"
    balance_file_path = f"{account_name}_balance.txt"
    try:
        with open(balance_file_path, "r") as file:
            balance_content = file.read().strip()
            assert balance_content == "0", f"Balance file content incorrect: {balance_content}"
    except FileNotFoundError:
        assert False, "Balance file not created"

    # Check if transaction history file exists and has the correct header
    records_file_path = f"{account_name}_records.csv"
    try:
        with open(records_file_path, "r") as file:
            reader = csv.DictReader(file)
            expected_headers = ["date", "operation", "amount"]
            assert reader.fieldnames == expected_headers, f"Headers incorrect: {reader.fieldnames}"
    except FileNotFoundError:
        assert False, "Transaction history file not created"

    # Clean up test files
    if os.path.exists(balance_file_path):
        os.remove(balance_file_path)
    if os.path.exists(records_file_path):
        os.remove(records_file_path)


def test_validate_response():
    assert validate_response("Number") == True
    assert validate_response("glisrishh") == True
    assert validate_response("97873") == True
    assert validate_response("1222") == True
    assert validate_response("2323") == True
    assert validate_response("1") == False
    assert validate_response("2") == False
