'''
Parses email for name, date and cost from transaction text from email
Name is identified by upper case, date by '/' and cost by '$'
'''
def parse(s):
	s = s.replace(',', ' ')
	str = s.split()
	name = cost = date = ' '
	for w in str:
		if w.isupper():
			name += w + ' '
		if w[0] == '$':
			cost = w
		if len(w) > 2 and w[2] == '/':
			date = w
	name = name[:-1]
	return date, name, cost

emailText = 'on 04/17/2019, at SUPER CHICKEN, a pending authorization or purchase in the amount of $10.38 was'
date, name, cost = parse(emailText)
print(f'Spent {cost} at {name} on {date}.')