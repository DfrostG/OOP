str = input("Enter message : ")
print(str)

l = 0
u = 0

for n in range(len(str)):
    if str[n].islower():
        l += 1
    elif str[n].isupper():
        u += 1
    
print(l)
print(u)