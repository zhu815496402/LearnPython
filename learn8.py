rawstr = raw_input("Enter a number:")
try:
    raw = int(rawstr)
except:
    raw = -1

if raw > 0:
    print "Nice work"
else:
    print "Not a number"