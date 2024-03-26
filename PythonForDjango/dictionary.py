myDict = {
    'key1': "Simnata",
    'key2': "paul"
}
myDict = {}
myDict = dict()
myDict['name'] = 'mohabbat'
myDict['id'] = '4508'
# del myDict['name']
print(myDict)

#another aproch to declare dictionary usnig dict():
a = dict(key1 = "Mohabbat" , mh = "Bohubrihi", key3 = "22")

b = {
    'key1': "mhr"
}
c = dict(zip(['key1','key2'],['Mohabbat','Hridoy']))
d = dict(
    [
        ('key','Mohabbat'),
        ('key1','Ridoy')
    ]
)

e = dict({'key1': "mhr", 'key2':'ridoy'},key3 = "hfdfg",key4 = "sfdg",key5 = "dfg")
print(a)
print(b)
print(c)
print(d)
print(e)
print(e.pop('key2'))
keyOfE = list(e)
print(keyOfE)