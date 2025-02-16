def update_grade_category(input_grades: list) -> list:
    output = []
    for i in input_grades:
        grade = i["grade"]
        if grade >= 8:
            category = "A"
        elif grade >= 5:
            category = "B"
        else:
            category = "C"
        i["grade_category"] = category
        output.append(i)
    return output


input_0 = [{"name": "anna", "grade": 4}]
input_1 = [{"name": "anna", "grade": 7}, {"name": "bob", "grade": 10}]
input_2 = [{"name": "anna", "grade": 5}, {"name": "bob", "grade": 6}]
input_3 = [{"name": "anna", "grade": 10}, {"name": "bob", "grade": 3}]
input_str = input_3
print(update_grade_category(input_str))
