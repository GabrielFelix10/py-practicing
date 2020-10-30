phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


# MODIFICA A LISTA
for k in range(4):
    plist.pop()

plist.pop(0)

print(" ")

plist.remove("'")
print(plist)

plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print('--------------------------------')
print(plist)
print(new_phrase)