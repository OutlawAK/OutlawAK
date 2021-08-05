
N = 11
M = 33

for i in range(1, N, 2):
    print((i * ".|.").center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))


def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(w, ' '), str(oct(i)[2:]).rjust(w, ' '), str(hex(i)[
            2:].upper())          .rjust(w, ' '), str(bin(i)[2:]).rjust(w, ' '), sep=' ')


print_formatted(18)
