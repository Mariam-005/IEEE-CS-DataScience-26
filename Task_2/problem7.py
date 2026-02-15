
filename = input("plz enter file_nme ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    target_words = [word for word in words if len(word) > 5]

    counter = len(target_words)
    print("n of target words =", counter)

except FileNotFoundError:
    print("Error! The file was not found")
except Exception as e:
    print("error!", e)
