'''
Parses email for name, date and cost from transaction text from email
Name is identified by upper case and after 'at', date by '/' and cost by '$'
'''
def parse(s):
	s = s.replace(',', ' ')
	str = s.split()
	afterAt = False
	name = cost = date = ''
	for w in str:
		if w == 'at':
			afterAt = True
		if w.isupper() and afterAt:
			name += w + ' '
		if w[0] == '$':
			cost = w
		if len(w) > 2 and w[2] == '/':
			date = w
	name = name[:-1]
	return date, name, cost

emailFile = open('./test-transaction.txt', 'r')
emailText = emailFile.read()
date, name, cost = parse(emailText)
print(f'Spent {cost} at {name} on {date}.')