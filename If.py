age=0
if age:
    print("Chance of getting print",age)

age=1
if age:
    print("Yes i would be exectued")

if age>=0:
    print('hurrya!!!!!')
    test=True

if age:
    test=True
    age=0
else:
    test=False

if test: print("I can be printed")

if age==0:
    print("Chance of getting print",age)

score=90
print("The grade was ",end= ' ')

if score<90:
    print('F')
elif 60<=score <70:
    print("D")
else:
    print('impossible')
    
score=60
if True: print('Score was ',score)
result='pass' if score>59 else 'fail'
if True:print ('Result:',result)
