import itertools

string = input("String to be permutated: ")
result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))