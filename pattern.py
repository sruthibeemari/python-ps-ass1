#1.number increasing pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ========================================================

#2.zeor-one triangle
for i in range(1, 5): 
    for j in range(i):  
        print((i + j) % 2, end=" ")  
    print()  

# ============================================================

#3 solid rhombus:

n = 5 

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * n)  
 
# --------------------------------------------------------- 

#hollow rhombus:

n = 5  

for i in range(1, n + 1):  
    print(" " * (n - i), end="")  
    for j in range(1, n + 1):  
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")  
        else:
            print(" ", end=" ")  
    print()  
