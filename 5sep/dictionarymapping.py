def case_a():
    print('Option A chosen')

def case_b():
    print('Option B chosen')

def case_c():
    print('Option C chosen')

def case_default():
    print("Invalid choice")
    

choice = 'm'
switch = {
    'A': case_a,
    'B': case_b,
    'C': case_c,
}

# Call the function associated with the choice
switch.get(choice, case_default)()
