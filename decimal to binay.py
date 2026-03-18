num = int(input("enter a number: "))

bit_num = ""
while 0 < num:
    binary = num % 2
    bit_num  = str(binary) + bit_num  
    num = num//2
    
print(bit_num)
