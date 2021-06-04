number=int(input("Enter your number : ")) 
if number%2 ==0:
    print("Number is even")   
else:   
    print("Number is not even ")    

#Output 7.    
# Enter your number: 24 8.    
# Number is even  

# (b) This can be done using a for loop statement, 
# here we are having series of form (1/i)
#  where i is in range 1,2,3,4................

for i in range(2,11):
    print((1/i),end="\n") 

#Output 
'''
0.5
0.3333333333333333 0.25 0.2 0.16666666666666666 0.14285714285714285 0.125
0.1111111111111111 0.1
'''