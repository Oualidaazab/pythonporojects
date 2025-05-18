def isperfect(n) :
    s=0 #2
    for i in range(2, n//2 +1) : #2 TO 3 
        if n%i == 0 : 
            s+=i 
    return s==n
print(isperfect(6))
