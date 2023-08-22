x = 10  # Binary:  1010
y = 6   # Binary:  0110

# Bitwise AND
result_and = x & y  # Result: 2 (Binary: 0010)
print(result_and)

# Bitwise OR
result_or = x | y   # Result: 14 (Binary: 1110)
print(result_or)

# Bitwise XOR
result_xor = x ^ y  # Result: 12 (Binary: 1100)
print(result_xor)

# Bitwise NOT
result_not_x = ~x   # Result: -11 (Binary: ...10101)
print(result_not_x)

n = 2

# Left Shift
result_left_shift = x << n  # Result: 40 (Binary: 101000)
print(result_left_shift)

# Right Shift
result_right_shift = x >> n  # Result: 2 (Binary: 0010)
print(result_right_shift)