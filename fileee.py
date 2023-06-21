a=int(input('enter no.'))

o=str(input('enter first 3 letters of the operation you want to perform'))

b=int(input('enter no.'))

if o== 'add' :
    print(a+b)
elif o== 'sub' :
    print(a-b)
elif o== 'mul' :
    print(a*b)
elif o== 'div' :
    print(a/b)
elif o== 'exp' :
    print(a**b)
elif o== 'rem' :
    print(a%b)
elif o== 'fld' :
    print(a//b)
else:
    print('error')