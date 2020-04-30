'''
This is to demonstrate the usage of dictionaries
'''

customer = {
    "name": "Shrenik",
    "age": 12,
    "is_verified": True
}

print(customer["name"])
print(customer.get("name"))
print(customer.get("Name"))     #keys are case-sensitive, return None if it does not match

customer["DoB"] = "09-08-2008"

print(customer)