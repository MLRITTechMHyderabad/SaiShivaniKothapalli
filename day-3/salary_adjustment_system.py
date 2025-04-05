n = int(input("Enter the number of employees: "))
employees = []

for i in range(n):
    print(f"Enter details for Employee {i+1}:")
    name = input("Name: ")
    salary = float(input("Salary: "))
    rating = int(input("Performance Rating (1 to 5): "))
    employees.append({"name": name, "Salary": salary, "rating": rating})

print("Original Employee Data:")
for emp in employees:
    print(f"{emp['name']} - Salary: {emp['Salary']}, Rating: {emp['rating']}")

adjust_salary = lambda emp: {
    "name": emp["name"],
    "Salary": round(emp["Salary"] * 1.10, 2) if emp["rating"] in [4, 5] else
              round(emp["Salary"] * 1.05, 2) if emp["rating"] == 3 else
              round(emp["Salary"] * 0.97, 2),
    "rating": emp["rating"]
}
updated_employees = list(map(adjust_salary, employees))

print("Updated Employee Salaries:")
for emp in updated_employees:
    print(f"{emp['name']}'s new salary: {emp['Salary']} (Rating: {emp['rating']})")
