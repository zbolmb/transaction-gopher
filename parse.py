def parse(s):
	str = s.split()
	name = ""
	cost = ""
	for w in str:
		if w.isupper():
			name += w + " "
		if w[0] == "$":
			cost = w
	name = name[:-1]
	return name, cost

s = "on 04/17/2019, at SUPER CHICKEN, a pending authorization or purchase in the amount of $10.38 was"
name, cost = parse(s)
print(name)
print(cost)