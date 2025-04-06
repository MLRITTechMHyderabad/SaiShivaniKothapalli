import numpy as np
resources = np.random.randint(15, 51, (6, 3))
resource_names = ["Oxygen", "Water", "Food"]
print("resources = np.array([")
for row in resources:
    print(f"    {row.tolist()},")
print("])")
total = np.sum(resources, axis=0)
print(f"\nTotal resources needed (tons): Oxygen: {total[0]}, Water: {total[1]}, Food: {total[2]}")
max_value = np.max(resources)
max_month, max_resource_index = np.unravel_index(np.argmax(resources), resources.shape)
print(f"Highest consumption in a month: {resource_names[max_resource_index]} ({max_value} tons in month {max_month + 1})")
std_dev = np.std(resources, axis=0)
print(f"Standard deviation of consumption: Oxygen: {std_dev[0]:.1f}, Water: {std_dev[1]:.1f}, Food: {std_dev[2]:.1f}")
transposed = resources.T
print("Transposed matrix:")
print(transposed)
