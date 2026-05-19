import math

students_data = {"Mark": 88, "Alice": 92, "David": 90, "Jane": 97, "Mike": 87}

scores = []
for i in students_data:
    scores.append(students_data[i])

sum_of_scores = sum(scores)
average = sum_of_scores/5
print("The average value is:", average)

top_scorer = max(scores)
bottom_scorer = min(scores)
print("Top scorer marks:", top_scorer)
print("Bottom scorer marks:", bottom_scorer)

for i in students_data:
    name = input(str("Enter a student name: "))
    if name == "Mark":
        print("The score of Mark was: ", 88)
    if name == "Alice":
        print("The score of Mark was: ", 92)
    if name == "David":
        print("The score of Mark was: ", 90)
    if name == "Jane":
        print("The score of Mark was: ", 97)
    if name == "Mike":
        print("The score of Mark was: ", 87)
