import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


print(wrap("ABCDEFGHIKLMNOPQ", 3))

print(textwrap.wrap("ABCDEFGHIKLMNOPQ", 3))
