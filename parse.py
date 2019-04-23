'''
Parses email for name, date and cost from transaction text from email
'''
#Routes to function based on bank
def parse(emailText, bank):
	if bank == 'Capital One':
		return parseCapitalOne(emailText)
	elif bank == 'Chase':
		return parseChase(emailText)
#Capital One: Name is identified by upper case and after 'at', date by '/' and cost by '$'
def parseCapitalOne(emailText):
	emailText = emailText.replace(',', ' ')
	words = emailText.split()
	name = cost = date = ''
	afterAt = False
	for w in words:
		if w == 'at':
			afterAt = True
		if w.isupper() and afterAt:
			name += w + ' '
		if w[0] == '$':
			cost = w[1:]
		if len(w) > 2 and w[2] == '/':
			date = w
	name = name[:-1]
	return date, name, cost
#Chase: Name is identified between 'at' and 'has', date by '/' and cost by '($USD)'
def parseChase(emailText):
	emailText = emailText.replace(',', ' ')
	words = emailText.split()
	name = cost = date = ''
	afterAt = False
	beforeHas = True
	costBool = False
	for w in words:
		if w == 'at':
			afterAt = True
		elif w == 'has':
			beforeHas = False
		elif afterAt and beforeHas:
			name += w + ' '
		elif w == '($USD)':
			costBool = True
		elif costBool:
			cost = w
			costBool = False
		elif len(w) > 2 and w[2] == '/':
			date = w
	name = name[:-1]
	return date, name, cost

def test_capital_one():
	bank = 'Capital One'
	emailFile = open('./transactions/capitalone.txt', 'r')
	emailText = emailFile.read()
	date, name, cost = parse(emailText, bank)
	assert date == '04/17/2019', 'Capital One: date should be 04/17/2019'
	assert name == 'SUPER CHICKEN', 'Capital One: name should be SUPER CHICKEN'
	assert cost == '10.38', 'Capital One: cost should be 10.38'

def test_chase():
	bank = 'Chase'
	emailFile = open('./transactions/chase.txt', 'r')
	emailText = emailFile.read()
	date, name, cost = parse(emailText, bank)
	assert date == '04/18/2019', 'Chase: date should be 04/18/2019'
	assert name == 'Amazon.com', 'Chase: name should be Amazon.com'
	assert cost == '59.35', 'Chase: cost should be 59.35'


if __name__ == "__main__":
	test_capital_one()
	test_chase()
	print("Everything passed")
