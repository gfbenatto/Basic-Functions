"""
For an N informed by the user, use a function that takes an integer N value and prints to the nth line.

"""


def sequence(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


result = sequence(7)
print(sequence)