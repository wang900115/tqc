# k = int(input())
# for i in range(k):
#     s=set()
#     for char in input().strip():
#         s.add(char)
#     print(len(s)>=26)

count = eval(input())

alpha = 26

for _ in range(count):
    sentence = input()
    set1 = set(sentence)
    if ' ' in set1:
        set1.remove(' ')

    if len(set1)>=26:
        print('True')
    else:
        print('False')