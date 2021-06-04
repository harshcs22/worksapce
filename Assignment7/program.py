#f="C:\\Users\\HP\\Desktop\\g.txt"
f="C:\\Users\\hArSH\\Desktop\\py\\Assignment7\\hello.txt"
file = open ( f, "r" )  # in-built library for file handling
a=[]                    #declare list variable a
b={}                    #declare dict variable b

# Frequency Calculator
for i in file:
    for j in range(0,len(i)):
        a.append(i[j])
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)

#Type of file checker 
c=f.split(".")
if c[1]=="txt":
    print("\n\nit is a text file")
elif c[1]=="cpp":
    print("\n\nit is a c++ file")
else:
   print("\n\nit is a c file")