ilist = [2,3,4,5,6,7,8,89,34,2,9,0]

ilist.sort(reverse=False)
print(ilist)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(reverse=False)
print(pairs)

ilist = ['a','t','u','u','u','u','o','i','e','w','s']

ilist.sort(reverse=True)
print(ilist)
ilist = "Gourio Prasad Mahapatra"
#sorted = ''.join(sorted(ilist, reverse=False))

t = sorted(ilist, reverse=False)
t = ''.join(t)
print(t)