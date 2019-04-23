'''
Parses email for name, date and cost from transaction text from email
'''
#Routes to function based on bank
def parseEmail(emailText, bank):
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