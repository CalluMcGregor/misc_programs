#Initialise an empty dictionary
my_dict: dict = dict()

#Create a dictionary with key value pairs
populated_dict: dict = {
    "callum" : "engineer",
    "lachlan" : "student"
}

#update the populated dictionary with a new KVP
populated_dict.update({"nathan" : "software engineer"})
#update the populated dictionary with a new value for a specified key
populated_dict.update({"callum" : "software engineer"})

print(f"Populated dictionary: {populated_dict}\n")

#directly update the value of a key pair
populated_dict["callum"] = "coder"
print(f"Populated dictionary: {populated_dict}\n")

# print(f"Populated dictionary items: {populated_dict.items()}\n")

# print(f"Populated dictionary keys: {populated_dict.keys()}\n")

# print(f"Populated dictionary values: {populated_dict.values()}\n")

#extract keys with l in the key
keys = [key for key in populated_dict.keys() if "l" in key]

#update keys with l in the name to have a value of l holder
for key in keys:
    populated_dict.update({key : "l holder"})

print(populated_dict)