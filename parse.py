def parse(s):
	s = s.replace(",", " ")
	str = s.split()
	name = ""
	cost = ""
	date = ""
	for w in str:
		if w.isupper():
			name += w + " "
		if w[0] == "$":
			cost = w
		if len(w) > 2 and w[2] == "/":
			date = w
	name = name[:-1]
	return date, name, cost

s = "on 04/17/2019, at SUPER CHICKEN, a pending authorization or purchase in the amount of $10.38 was"
date, name, cost = parse(s)
print(f"Spent {cost} at {name} on {date}.")