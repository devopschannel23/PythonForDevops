import json
# 1: Serialization: Python Dict to JSON String
userdata = {
    "name": "Alice",
    "age": 30,
    "active": True,
    "marks": {
        "maths": 90,
        "science": 85
    }
}
#dumps -> python -> JSON
json_string = json.dumps(userdata, indent=4)
# print((json_string))

#Deserialization: JSON string to Python Dict
parsed_data = json.loads(json_string)
# print(parsed_data)
# print(type(parsed_data))
# print(parsed_data["skills"])
print(parsed_data["marks"]["maths"])


