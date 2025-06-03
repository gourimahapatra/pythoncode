lst = ['Gouri', 'Prasad', 'Mahapatra']
print(lst[-1:])
pr = lambda x : x[0:-1]

res =  sorted(lst, key=lambda x : x[0:-1])
print(pr(lst))
print(res)