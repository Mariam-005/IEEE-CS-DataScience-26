sentence = input("enter yiur sentence ")
words = sentence.split()  

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word =", longest_word)

