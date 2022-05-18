# Importing JSON to encode and decode JSON strings to Python and vice-versa

import json


user = {"name" : "Cristian", "age": 30, "city": "Rio de Janeiro", "hobbies": ["Video games", "Cinema", "Music"]}

# Converting into JSON: (Serialization, Encode)
# json.dumps -> convert to string (shows in terminal)
# json.dump -> Better to export to a file.json

user_json = json.dumps(user, indent=4)  # with indent=4 convert to a JSON most common viewd format
#print(user_json)

# Coverting to a file using method open

with open ('user.json', 'w') as file:
    json.dump(user, file, indent=4)



# Converting JSON into Python: (Deserialization, Decode)

user2_json = """
{
    "name": "Cristian",
    "age": 30,
    "city": "Rio de Janeiro",
    "hobbies": [
        "Video games",
        "Cinema",
        "Music"
    ]
}
"""

ser2 = json.loads(user2_json) # This method will show on terminal the list.
# print(user2) 

# Loading a json file and convert to Python list is easy

with open ('user.json', 'r') as file2:
    user2 = json.load(file2)
    print(user2)
