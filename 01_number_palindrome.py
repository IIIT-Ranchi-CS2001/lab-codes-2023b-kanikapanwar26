sentence=input("Enter the sentence:")
words=sentence.split()
count=0
for word in words:
    clean_word = ''.join(char.lower() for char in word if char.isalnum())
    if clean_word==clean_word[::-1] and clean_word!="":
        count+=1
print(f"Number of palindrome words are {count} ")        

