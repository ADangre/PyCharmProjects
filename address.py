book = {}
book["Amit"]={ "name":"Amit", "address":"Zapska 1161 Nehvizdy", "Phone":"739500934"}
book["Krishna"]={"name":"Krishna", "address":"Andel 1123, Prague", "Phone":"739500933"}
# print(book)
for key, value in book.items():
    print("The key is:",key, "\nThe value is:",value)

import json
convertedjson = json.dumps(book, indent=4)
# print("The converted json is mentioned below")
print(convertedjson)

