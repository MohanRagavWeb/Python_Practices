#43. Use a lambda in dictionary sorting (e.g., by value or key).
data = {"Mohan": 85, "Rahul": 90, "Anu": 78}

sorted_by_key = sorted(data.items(), key=lambda x: x[0])
print(sorted_by_key)

sorted_by_value = sorted(data.items(), key=lambda x: x[1])
print(sorted_by_value)
