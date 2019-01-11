i=int(raw_input())
if i%4==0:
    if i%100==0:
        if i%400==0:
            print "yes"
        else:
            print "no"
    else:
        print "yes"
else:
    print "no"
        
        
