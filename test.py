#converting list to String

lst = ['3','5','6','7','8','9']

rtnString = ''.join(lst)
print(rtnString)

#Converting list into Tuple

tpl = tuple(lst)
print(tpl)

lSet = set(lst)
print(lSet)

days = ['S','M','W', 'M','M','F','S']

print(days.count('M'))
print(len(days))

for c in set(days) :
    print(c +" - "+str(days.count(c)))

