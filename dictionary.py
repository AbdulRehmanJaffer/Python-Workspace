"""my_dict = {"Name": "Zara", "Age": 7, "Class": "First"}
my_dict["Age"] = 6
my_dict["Gender"] = "Female"

print(my_dict)"""

#activity 1
"""country_code = {"Pakistan": +92, "Australia": +13, "Japan": +67}

x = country_code.get("Pakistan", "Not Found")
print(x)"""

#activity 2

student_data = {
    "id1":{"Name": "Zara", "Class": "V", "Subject_Integration": "maths, science, english"},
    "id2":{"Name": "David", "Class": "V", "Subject_Integration": "maths, science, english"},
    "id3":{"Name": "Alizah", "Class": "V", "Subject_Integration": "maths, science, english"},
    "id4":{"Name": "Surya", "Class": "V", "Subject_Integration": "maths, science, english"},
    "id5":{"Name": "Zara", "Class": "V", "Subject_Integration": "maths, science, english"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["Name"], details["Class"], details["Subject_Integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for i, j in result.items():
    print(i, ":", j)

