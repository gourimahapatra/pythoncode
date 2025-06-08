# for i in range(3,10):
#     print(i)

stra = "Gouri Prasad"

# for i in stra:
#     print(i)

lst = ['jhg','khj','lkijh']

# for l in lst:
#     print(l + "-" + l[0:2])


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active','Gouri':'Active','Gouri2':'inactive'}

for user, status in users.copy().items():
    if status == 'inactive':
        print(user, status)
        del users[user]
print(users)
print(users['Gouri'])

for i in range(len(lst)):
    print (str(i) +" : "+ lst[i])

#We can use Break, pass and continue