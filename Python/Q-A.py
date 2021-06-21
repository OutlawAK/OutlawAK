string = input('Enter The string')
string = 'BAhFkitflGoErl'
if len(string) < 10:
    print("invalid Length of string")

list = []


def encode(string):
    for i in range(0, len(string)):
        if string[i].islower():
            A = string[i].upper()
            list.append(A)

        else:
            A = string[i].lower()
            list.append(A)

    for i in range(0, len(list)-1, 2):
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
    return ''.join(list)


print(encode(string))
