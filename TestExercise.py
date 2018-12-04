name=input('Enter your Name:')

lenght=len(name)
le=1
while lenght>0:
    print(name[-le],end='')
    lenght-=1
    le+=1

