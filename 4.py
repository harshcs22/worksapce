#List : It is as same as arrays , it contains heterogeneous datatypes . 
#eg: a=[1,2,"a"]
a=[0,2,"a"]
a[0] =0
print(a)


'''
Functions in list
append()
Adds an element at the end of the list

clear()
Removes all the elements from the list

copy()
Returns a copy of the list

count()
Returns the number of elements with the specified value

extend()
Add the elements of a list (or any iterable), to the end of the current list

index()
Returns the index of the first element with the specified value

insert()
Adds an element at the specified position

pop()
Removes the element at the specified position

remove()
Removes the first item with the specified value

reverse()
Reverses the order of the list

sort()
Sorts the list
'''
 
# Creating a List 
List = [] 
print("empty List: ") 
print(List)

#Output
#empty List:
# []


# Creating a List with the use of a String 
List = ['GoEduHub.com'] 
print(List) 

'''Output
['GoEduHub.com'] 
# Creating a List with the use of multiple values 
'''
List = ["Go", "Edu", "Hub",".Com"] 
print(List[0]) #accesing values of list 
print(List[1])
print(List[2])
print(List[3])
'''
Output
Go 
Edu 
Hub 
.Com'''
# Creating a Multi-Dimensional List By Nesting a list inside a List
List = [['Go', 'Edu'] , ['hub.com']]  
print(List) 

#Output
#[['Go', 'Edu'], ['hub.com']]
# Creating a List with the use of Numbers 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]  
print(List) 
# Removing element using pop() method
List.pop() #removes last element
print(List)

''' Output
[1, 2, 4, 4, 3, 3, 3, 6, 5] 
[1, 2, 4, 4, 3, 3, 3, 6]
'''
# Print elements from beginning to a pre-defined point using Slice 
SList = List[:-6] 
print(SList)
# Print elements using Slice operation 
Sliced_List = List[3:8]  
print(Sliced_List) 
# Print elements from a pre-defined point to end 
SList = List[5:]  
print(SList) 
# Printing elements from beginning till end 
SList = List[:] 
print(SList) 
# Creating a List with  mix  values 
List = [1, 2, 'Go', 4, 'Edu', 6, 'Hub']  
print(List)
# Printing elements in reverse using Slice operation 
Sliced_List = List[::-1]  
print(Sliced_List) 
'''
Output
[1] 
[3, 3, 3, 6] 
[3, 6] 
[1, 2, 4, 3, 3, 3, 6] 
[1, 2, 'Go', 4, 'Edu', 6, 'Hub'] 
['Hub', 6, 'Edu', 4, 'Go', 2, 1] 
'''# Removing elements using Remove() method 
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  
print(List) 
List.remove(1)
print(List) 
List.remove(3)  
print(List) 

'''Output 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12] 
[1, 2, 3, 4, 7, 8, 9, 10, 11, 12]
'''# Removing elements from List using iterator
List =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
for i in List: 
    print(i) 

'''Output
1
2
3
4
5
6
7
8
9
10
11
12'
(b)'''
#Tuple :  Tuples are created by ( ) . it contains heterogeneous data-types . 
#eg: t=(1,2,3)
'''#Functions in  Tuple
len(tuple)
Gives the total length of the tuple.

max(tuple)
Returns item from the tuple with max value.

min(tuple)
Returns item from the tuple with min value.

tuple(seq)
Converts a list into tuple.
'''
 # An empty tuple 
t = () 
print (t)
tup = 'python', 'tuple'
print(tup) 
'''Output 
() 
('python', 'tuple')
'''# Another for doing the same 
tup = ('python', 'GoEduHub') 
print(tup) 

# concatenating 2 tuples 
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'GoEduhub') 
print(tuple1 + tuple2) 

#nested tupples
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'GoEduHub') 
tuple3 = (tuple1, tuple2) 
print(tuple3)

#tuple repitition
tuple3 = ('python',)*3  
print(tuple3) 
'''
tuples are immutable 
tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4
print(tuple1) 
'''
#slicing 
tuple1 = (0 ,1, 2, 3) 
print(tuple1[1:]) 
print(tuple1[::-1]) 
print(tuple1[2:4])

#deleting a tuple 
tuple3 = ( 0, 1) 
del tuple3 
#print(tuple3)


#length of a tuple 
tuple2 = ('python', 'goeduhub') 
print(len(tuple2)) 

#converting a list and a string into a tuple 
list1 = [0, 1, 2] 
print(tuple(list1)) 
print(tuple('python')) # string 'python' 

#tuples in a loop 
tup = ('h','e','l','l','o') 
for i in tup:  
    print(i) 



num=int(input("Enter your number"))
while(num>=0):
    print(num)
    num=num-1
