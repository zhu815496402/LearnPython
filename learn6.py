hrs = raw_input("Enter Hours:")
h = float(hrs)
date = raw_input("Enter date:")
d = float(date)
if(h<40):
    pay = h*d
else:
    pay = (h-40)*1.5*d+d*40
print pay