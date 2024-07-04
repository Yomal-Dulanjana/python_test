def sort_dict_by_values(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1]))

print(sort_dict_by_values({"a": 2, "b": 1, "c": 3}))
