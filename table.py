def multiplication_table(num,lim):
    
    print(f"Multiplication table of {num}")
    for i in range(1,lim+1):
        print(f"{num}x{i}={num*i}")
num=int(input("Enter the number:"))
lim=int(input("Enter the limit:"))
multiplication_table(num,lim)        
    

