def add_bonus_point(input_grades: list, bonus_point: float) -> dict:
    output = []
    for i in input_grades:
        new_grade = i["grade"] + bonus_point
        if new_grade > 10:
            new_grade = 10.0
        i["grade"] = new_grade
        output.append(i)

    return output


input_0 = [{"name": "anna", "grade": 7}, {"name": "bob", "grade": 10}]
input_1 = [{"name": "anna", "grade": 4}]
input_2 = [{"name": "anna", "grade": 5}, {"name": "bob", "grade": 6}]
input_3 = [{"name": "anna", "grade": 8}, {"name": "bob", "grade": 10}]
input_str = input_3
print(add_bonus_point(input_str, 2.5))
