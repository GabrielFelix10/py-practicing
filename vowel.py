vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Escolha uma palavra ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for result in found:
    print(result)

