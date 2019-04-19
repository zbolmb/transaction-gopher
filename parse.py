'''
Parses email for name, date and cost from transaction text from email
Capital One: Name is identified by upper case and after 'at', date by '/' and cost by '$'
Chase: Name is identified between 'at' and 'has', date by '/' and cost by '($USD)'
'''
def parse(s, bank):
	s = s.replace(',', ' ')
	str = s.split()
	name = cost = date = ''
	if bank == 'Capital One':
		afterAt = False
		for w in str:
			if w == 'at':
				afterAt = True
			if w.isupper() and afterAt:
				name += w + ' '
			if w[0] == '$':
				cost = w[1:]
			if len(w) > 2 and w[2] == '/':
				date = w
		name = name[:-1]
	elif bank == 'Chase':
		afterAt = False
		beforeHas = True
		costBool = False
		for w in str:
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

bank = 'Capital One'
emailFile = open('./transactions/capitalone.txt', 'r')
#bank = 'Chase'
#emailFile = open('./transactions/chase.txt', 'r')

emailText = emailFile.read()
date, name, cost = parse(emailText, bank)
print(f'Spent {cost} at {name} on {date}.')