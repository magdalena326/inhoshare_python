text = "Abracadabra"
replaced = ""
#replaced += x
#for char in text:
#    print(char)
#for idx, _ in enumerate(text):
#    print(idx, text[idx])

#new_text = text.replace("a", "A")
#print(new_text)

for idx, _ in enumerate(text):
    if idx % 2:
        replaced += text[idx]
    else:
        replaced += text[idx].upper()
print(replaced)


