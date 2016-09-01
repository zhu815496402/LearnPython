try:
    score = raw_input("Enter Score: ")
    sc = float(score)
except:
    print "Please enter a number between 0.0 and 1.0"
    quit()
if (sc >= 0.0 and sc <= 1.0):
    if (sc >= 0.9):
        SG = "A"
    elif (sc >= 0.8 and sc < 0.9):
        SG = "B"
    elif (sc >= 0.7 and sc < 0.8):
        SG = "C"
    elif (sc >= 0.6 and sc < 0.7):
        SG = "D"
    else:
        SG = "F"
    print SG
else:
    print "Please enter a number between 0.0 and 1.0"
