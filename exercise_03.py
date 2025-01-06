def calculate_average(input_grades: list) -> float:
    n = len(input_grades)
    total = 0
    for i in input_grades:
        total += i["grade"]
    return total / n


input_0 = [{"name": "anna", "grade": 7}, {"name": "bob", "grade": 10}]
input_1 = [{"name": "anna", "grade": 4}]
input_2 = [{"name": "anna", "grade": 5}, {"name": "bob", "grade": 6}]
input_3 = [
    {"name": "anna", "grade": 8},
    {"name": "bob", "grade": 10},
    {"name": "carl", "grade": 9},
]
input_str = input_3
print(calculate_average(input_str))
