
#this is what i  tried and did by myself
import sys

def uret(str):
    a=''
    b=0
    s2 = sys.argv[2]
    s3 = sys.argv[3]
    k = s2.split('=')
    print(k)
    a=k[1]

    l = s3.split('=')
    b=l[1]
    return a,b


nur=sys.argv
x,y=uret(nur)


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#with the teacher's help

import sys

def uret(str):
    a=''
    b=0
    k = str[2]
    l= str [3]
    a= k.split('=')[1]
    b= l.split('=') [1]
    return a,b

    y=uret(sys.argv)
