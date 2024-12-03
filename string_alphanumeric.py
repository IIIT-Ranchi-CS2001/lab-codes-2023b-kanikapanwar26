str=input("Enter the string :")
for char in str:
    if not char.isalnum():
       print(False)
       break
else:
    print(True)