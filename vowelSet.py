vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Escolha uma palavra ")
found = {}

found = vowels.intersection(set(word))


for result in sorted(found):
    print(result)

