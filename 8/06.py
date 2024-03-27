string = input()
dict = {}
for char in string:
    dict[char]=dict.get(char,0)+1

char = input()

print("{} occurs {} time(s)".format(char,dict[char]))