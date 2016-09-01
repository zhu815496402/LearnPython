largest=None
smallest=None
inputs=[]
while True:
    num=raw_input("enter a number:")
    if num =="done":
        break
    try:
        f=float(num)
        inputs.append(f)
    except:
        print "Invalid input"

if len(inputs)==0:
    print "no number in array"
    sys.exit(-1)

smallest=largest=inputs[0]  
for n in inputs:
    if n<smallest:
        smallest=n
    elif n>largest:
        largest=n
smallests = int(smallest)
largests = int(largest)

print "Maximum is",largests
print "Minimum is",smallests