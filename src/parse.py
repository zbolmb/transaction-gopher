"""
Parses email for name, date and cost from transaction text from email
"""


# Routes to function based on bank
def parse_email(email_text, bank):
    if bank == 'Capital One':
        return parse_capital_one(email_text)
    elif bank == 'Chase':
        return parse_chase(email_text)


# Capital One: Name is identified by upper case and after 'at', date by '/' and cost by '$'
def parse_capital_one(email_text):
    email_text = email_text.replace(',', ' ')
    words = email_text.split()
    name = cost = date = ''
    after_at = False
    for w in words:
        if w == 'at':
            after_at = True
        if w.isupper() and after_at:
            name += w + ' '
        if w[0] == '$':
            cost = w[1:]
        if len(w) > 2 and w[2] == '/':
            date = w
    name = name[:-1]
    return date, name, cost


# Chase: Name is identified between 'at' and 'has', date by '/' and cost by '($USD)'
def parse_chase(email_text):
    email_text = email_text.replace(',', ' ')
    words = email_text.split()
    name = cost = date = ''
    after_at = False
    before_has = True
    cost_bool = False
    for w in words:
        if w == 'at':
            after_at = True
        elif w == 'has':
            before_has = False
        elif after_at and before_has:
            name += w + ' '
        elif w == '($USD)':
            cost_bool = True
        elif cost_bool:
            cost = w
            cost_bool = False
        elif len(w) > 2 and w[2] == '/':
            date = w
    name = name[:-1]
    return date, name, cost
