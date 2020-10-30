phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

on_tap = ''.join(plist[1: 3])

# METODO JOIN transforma uma lista em String , por isso o join([])
result = on_tap + ''.join([plist[5] , plist[4], plist[7], plist[6]])

#
# new_phrase = ''.join(plist)
print('--------------------------------')
print(plist)
print(result)