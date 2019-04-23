# from parse import parse_email


def test_capital_one():
    bank = 'Capital One'
    email_file = open('./transactions/capitalone.txt', 'r')
    email_text = email_file.read()
    date, name, cost = parse_email(email_text, bank)
    assert date == '04/17/2019', 'Capital One: date should be 04/17/2019'
    assert name == 'SUPER CHICKEN', 'Capital One: name should be SUPER CHICKEN'
    assert cost == '10.38', 'Capital One: cost should be 10.38'


def test_chase():
    bank = 'Chase'
    email_file = open('./transactions/chase.txt', 'r')
    email_text = email_file.read()
    date, name, cost = parse_email(email_text, bank)
    assert date == '04/18/2019', 'Chase: date should be 04/18/2019'
    assert name == 'Amazon.com', 'Chase: name should be Amazon.com'
    assert cost == '59.35', 'Chase: cost should be 59.35'


if __name__ == "__main__":
    test_capital_one()
    test_chase()
    print("Everything passed")
