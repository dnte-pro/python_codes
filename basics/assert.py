#change the value to -10 to see changes
age = 10

def check_age(val):
    assert val > 0, "age cannot be less than or equal to zero"
    print(f"age is valid: {age}")
check_age(age)