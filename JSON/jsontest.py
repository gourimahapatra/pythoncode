import json

x = '{"name":"Ram", "age":50, "City":"Tokyo"}'
y = json.loads(x)
print(y["City"])

x = {
    "name":"John",
    "salary":500000
}
y = json.dumps(x)
print(y)

print(json.dumps("hello"))