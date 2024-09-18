n=int(input("Enter the number of terms:"))
a,b=0,1
count=0
if n==1:
    print(f"Fibonacci sequence upto {n} :")
    print(a)
else:
    print("Fibonacci sequence: ")   
    while count<n:
        print(a,end=" ") 
        temp=a+b
        a=b
        b=temp
        count+=1