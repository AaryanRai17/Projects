#Program to check weather numbers betweeen range are prime or composite
print('(a,b) Enter the lower limit in place of a and the upper limit in place of b')
a=int(input('Enter Lower Limit a: '))
b=int(input('Enter Upper Limit b: '))
x=''
y=''
count1=0
count2=0
print(f'The status of each number in the range ({a},{b}) is:')
for i in range(a,b+1):
    #Check Prime
    flag=False
    if i>1:
        for w in range(2,i):
            if i%w ==0:
                flag=True
                break
    if flag:
        x='Not a Prime Number and '
    elif i==1:
        x='Not a Prime Number and'
    else:
        x='Prime Number and'
        count1=count1+1        
    #Check Composite
    is_composite=False
    for q in range(2, i):
        if i % q == 0:
            is_composite = True

    if is_composite == True:
        y=" is a composite number"
        count2=count2+1
    else:
        y="not a composite number"
    print(i,'is',x,y) 
print(f'The range has {count1} prime number and {count2} composite number.')   