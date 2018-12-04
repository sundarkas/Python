for char in 'string':
    print(char,end='#')
print()
for t in (1,2,3):
    print(t)

print()
for er in range(0,7):
 print(er)

for outer in range(2,10):
    #print('outer',outer)
    for inner in range(2,outer):
        #print('inner',inner)
        if not outer%inner:
            print(outer,'=',inner,'*',int(outer/inner))
            break
        else:
            print(outer,'is prime')
