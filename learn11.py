

shuzu=[]
while True:
    num = raw_input("Enter a number:")
    if (num == "done"):
        break
    try:
        f= float(num)
        shuzu.append(f)
    except:
        print "qingshuruzhengquedeshu"
zuixiaoshu=zuidashu=shuzu[0]
for f in shuzu:
    if(f>zuidashu):
        zuidashu=f
    if(f<zuixiaoshu):
        zuixiaoshu=f
print zuidashu
print zuixiaoshu
