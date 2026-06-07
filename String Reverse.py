class reverse:
    def __init__(self, s):
        self.s = s

    def getting_reversed(self):
        return self.s[::-1]

userinput = input("enter a string : ")

reverser = reverse(userinput)

reverser_result = reverser.getting_reversed()
print(reverser_result)
