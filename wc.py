import string
import pprint
with open(r"C:\Users\eusha\PycharmProjects\learn\weather.txt","r") as f:
    content = f.read()
#print(content)
#print(type(content))
content = " ".join(content.split("\n")).lower()
new_content = ""
for letter in content:
    if letter in string.ascii_lowercase + " ":
        new_content += letter
content = new_content
print(content)

content_words = {}
for word in content.split(" "):
    content_words[word] = content_words.get(word,0)+1
#pprint.pprint(content_words)
#print(string.ascii_lowercase)
sorted_content = dict(sorted(content_words.items(), key=lambda items: items[1], reverse=True))
pprint.pprint(sorted_content)