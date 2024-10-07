# Structures dictionary are an unordered set of pairs key:value, when have a primary key
people = {
    "name": "Olga", 
    "age": 22
}

people = dict(name="Olga", age=22) 

# Getting the value
people["name"]

# Edition
people["name"] = "Maria"

# Nested dictionary
contacts = {
    "email0@com.br": {"name": "Olga", "Phone": "12345678"},
    "email1@com.br": {"name": "Maria", "Phone": "12345678"},
    "email2@com.br": {"name": "Jose", "Phone": "12345678"}
}

for key, value in contacts.items(): 
    print(key, value)

''' 
Methods

.clear()
.copy()
.fromkeys -> make news values where the keys are  None or predefinition
.get("key") -> take value from key
.items() -> return a lista of tuple 
.keys() -> return only keys
.values() -> return only values
.pop("key") -> remove from key
.popitem() -> remove the last item
.setdefault() -> create a new key:value if don't exist
.update() -> Modify the data from the key
in -> verify if a key exist in the dict
del people["key"] -> delete exactly key informed
'''