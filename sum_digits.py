num=int(input("Enter the number:"))
sum_digit=0
num1=num
while(num>0):
    digit=num%10
    sum_digit+=digit
    num=num//10
print(f"Sum of digits of {num1} is {sum_digit}")    
