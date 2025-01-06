def output_sorted_names(input_events: list) -> list:
    return sorted({i["name"] for i in input_events})


input_0 = [
    {"name": "carl", "time": "06:00:00"},
    {"name": "carl", "time": "07:00:00"},
    {"name": "bob", "time": "07:00:00"},
]
input_1 = [
    {"name": "carl", "time": "06:00:00"},
    {"name": "anna", "time": "07:00:00"},
    {"name": "bob", "time": "07:00:00"},
    {"name": "bob", "time": "07:00:00"},
]
input_str = input_1
print(output_sorted_names(input_str))
