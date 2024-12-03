str_input=input("Enter the string:")
char_to_count=input("Enter the character to count:")
count=0
for char in str_input:
    if char==char_to_count:
        count+=1
print(f"The character {char_to_count} appears {count} times in the string")        
