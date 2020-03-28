#Iterative Form

def fibIte(n):
    a = 0
    b = 1

    for k in range(n):
        c = a + b
        a = b
        b = c

    return b

print("Result with Iterative Form: ")

for x in range(20):
    
    print(fibIte(x))

# Recursive Form

def fibRec(n):
    # fn = fn-1 + fn-2
    if n < 3:
        return n
    return fibRec(n-1) + fibRec(n-2)

print("Result with Recursive Form: ")

for x in range(20):
    
    print(fibRec(x))
    
   
