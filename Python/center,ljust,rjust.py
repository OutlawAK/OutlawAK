
N = 11
M = 33

for i in range(1, N, 2):
    print((i * ".|.").center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))
