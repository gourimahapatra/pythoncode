import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print(x.group())


match = re.search(r"cat", "A cat is here.")
if match:
    print("Found:", match.group())


matches = re.findall(r"\d+", "There are 3 cats and 4 dogs.")
print(matches) # Output: ['3', '4']


result = re.sub(r"cat", "dog", "The cat sat on the cat.")
print(result) # Output: The dog sat on the dog


parts = re.split(r"\s+", "Split this sentence by spaces.")
print(parts)


match = re.search(r"(\d+)-(\d+)", "Phone: 123-4567")
if match:
    print("Area:", match.group(1))
    print("Number:", match.group(2))


pattern = re.compile(r"\b\w{4}\b") # Words with exactly 4 letters
print(pattern.findall("This line has some four-letter words."))
