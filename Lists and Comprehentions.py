"""numbers = [1,2,3,4,5]

even = [x for x in numbers if x%2 == 0]
print("The even numbers are:", even)"""

"""myDict = {str(x): x**2 for x in [1,2,3,4,5]}
print("The squares are:", myDict)"""

#activity 1
"""numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

def sq(n):
    return n*n

nums = [1,2,3,4,5]
squares = map(sq, nums)
print(list(squares))"""

#activity 2
"""s1 = [1,2,3]
s2 = ["b","a","c"]
s3 = list(zip(s1,s2))
print(s3)

list1 = [10,20,30,40]
list2 = [100,200,300,400]

for x, y in zip(list1, list2[::-1]):
    print(x,y)"""

