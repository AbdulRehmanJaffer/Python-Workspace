"""i = 1
while(i < 6):
    print(i)
    i += 1"""
#activity 1
"""n = int(input("Enter a random number: "))
sum = 0

i = 1
while(i <= n):
    sum = sum + i
    i += 1
    print(sum)"""
#activity 2
"""i = 0
while(i <= 0):
    print("I WILL RUN FOREVER")"""
#activity 3
"""num = int(input("Enter a number: "))
sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print("It is an armstrong numer")
else:
    print("It is not an armstrong number")"""
#activity 4
"""num = int(input("Enter a number: "))
i = 0

while(i <= 10):
    result = i * num
    print(result)
    i += 1"""

#submission

counta=0                            #variable counts the nuber of times 'a' appears in string
name = input("Enter a name: ")      #taking input string from user
print(name)                         # prints the input string
length1 = len(name)                 # counts the length of str --> number of char in string
i = 0                               # starting index of the search in the string 
while(i<=(length1-1)):              # search the string from index [0] till end of string --> [length - 1]
    #char_to_check = name[i]   
    if name[i] == 'a':              # check if the current char is 'a'
        counta=counta+1             # if the char is 'a' -> increment the count
    i= i+1                          # increment loop index
print (counta)                      # print the count of chr 'a' in the string 