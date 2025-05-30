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
