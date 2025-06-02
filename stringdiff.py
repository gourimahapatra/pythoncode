
str1 = "abcdef"
str2 = "abdfgh"

diff1 = set(str1) - set(str2)
diff2 = set(str2) - set(str1)

print("In str1 but not in str2:", diff1)
print("In str2 but not in str1:", diff2)

st1 = "GouriPrasadMahapatra unit9"
st2 = "dfjdf Gouee aids "

diff1 = set(st1) - set(st2)
diff2 = set(st2) - set(st1)
print(diff1)
print(diff2)