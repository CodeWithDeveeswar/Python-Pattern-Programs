# Repeated Numbers In Each Row

"""
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5
"""

for i in range(1, 6):
    for _ in range(i):
        print(i, end=" ")
    print()