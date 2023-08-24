class math:
    @staticmethod
    def add(x, y):
        return x + y
    

# without creating instances
sum_result = math.add(5, 3)


print("Sum:", sum_result)         # Output: Sum: 8

a = math()
print("Sum:",a.add(2,3))           # Output: Sum: 5

