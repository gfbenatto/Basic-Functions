"""
For an N informed by the user, use a function that takes an integer N value and prints to the nth line.

"""

def sequence2(n):
    for i in range(1, n+1):
        for j in range(i):
            print(str(j) * j)

result = sequence2(10)