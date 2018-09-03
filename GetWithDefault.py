d = {"cs":[106,107,110], "Math":[51,113]}
#d["COMPSCI"] ####Show me the keyerror

print(d)

#print(d.get("CS"))

english_classes = d.get("ENGLISH", [])
num_english = len(english_classes)
print(num_english)
