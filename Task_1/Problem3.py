# text = input("plz enter your string ")
# text = text.lower()

# count = (
#     text.count('a') +
#     text.count('o') +
#     text.count('i') +
#     text.count('e') +
#     text.count('u')
# )

# print("The number of vowels =", count)


text = input("plz enter your string") 
text = text.lower()

counter=0 
vowels = "aoeiu"

for char in text:
    if char in vowels:
     counter+=1

print(counter)    

