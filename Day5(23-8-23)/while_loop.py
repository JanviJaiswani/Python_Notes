# While loop
i = 1
while i <= 5:
    print(i)  # Output: 1 2 3 4 5
    i += 1

# Continue statement
i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)  # Output: 1 3 5 7 9 11

# Break statement
i = 1
while i < 5:
    if i == 3:
        break
    print(i)  # Output: 1 2
    i += 1

# Else with while loop
i = 1
while i < 4:
    print(i)  # Output: 1 2 3
    i += 1
else:
    print(i)  # Output: 4
