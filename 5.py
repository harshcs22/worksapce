l=[]
for i in range(1,201):
    for j in range(1,i):
        if i%j==0 and i!=j:
            l.append(i)
print("sum : ",sum(l))
total=0
for i in range(0,len(l)):
    total=total+l[i]
print("sum = ",total)
'''
Output :  
sum: 100397
sum = 100397
(b)'''
def fib(n):
    a=0
    b=1
    a1=[]
    a1.append(a)
    a1.append(b)
    s=0
    for i in range(1,n+1):
        c=a+b
        a1.append(c)
        a=b
        b=c
    print(a1)
    for j in a1:
        if j%2==0:
            s=s+j
    print("sum of even terms upto",n,"are : ",s)
fib(50)
'''
Output : 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074]
sum of even terms upto 50 are :  26658145586'''