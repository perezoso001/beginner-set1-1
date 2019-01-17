g=raw_input()
def reverse(s):
    str = "" 
    for i in s:
        str = i + str
    return str
k= reverse(g)
if g==k:
    print "yes"
else:
    print "no"

