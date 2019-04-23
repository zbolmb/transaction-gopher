from .context import src

def test_capital_one():
	bank = 'Capital One'
	emailFile = open('./transactions/capitalone.txt', 'r')
	emailText = emailFile.read()
	date, name, cost = parseEmail(emailText, bank)
	assert date == '04/17/2019', 'Capital One: date should be 04/17/2019'
	assert name == 'SUPER CHICKEN', 'Capital One: name should be SUPER CHICKEN'
	assert cost == '10.38', 'Capital One: cost should be 10.38'

def test_chase():
	bank = 'Chase'
	emailFile = open('./transactions/chase.txt', 'r')
	emailText = emailFile.read()
	date, name, cost = parseEmail(emailText, bank)
	assert date == '04/18/2019', 'Chase: date should be 04/18/2019'
	assert name == 'Amazon.com', 'Chase: name should be Amazon.com'
	assert cost == '59.35', 'Chase: cost should be 59.35'


if __name__ == "__main__":
	test_capital_one()
	test_chase()
	print("Everything passed")