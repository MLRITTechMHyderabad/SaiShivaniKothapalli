import numpy as np

resources = np.random.randint(15, 51, (6, 3))
resource_names = ["Oxygen", "Water", "Food"]
print("resources = np.array([")
for row in resources:
    print(f"    {row.tolist()},")
print("])")
total = np.sum(resources, axis=0)
print("Total resource consumption (tons):")
for i in range(3):
    print(f"{resource_names[i]}: {total[i]}")
max_value = np.max(resources)
max_month, max_resource_index = np.unravel_index(np.argmax(resources), resources.shape)
print(f"Highest consumption recorded: {max_value} tons in Month {max_month+1}, Resource: {resource_names[max_resource_index]}")
min_val = np.min(resources)
max_val = np.max(resources)
normalized = (resources - min_val) / (max_val - min_val)
print("Normalized Resource Matrix:")
print(np.round(normalized, 2))
print("Risky Consumption Months (any resource below 25 tons):")
for i, row in enumerate(resources):
    risky = row[row < 25]
    if risky.size > 0:
        print(f"Month {i+1}: {risky.tolist()}")
