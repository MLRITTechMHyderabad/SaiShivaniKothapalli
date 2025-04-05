        
n = int(input("Enter number of customers: "))
customers = []

def process_discounts(customers):
    eligible_customers = list(filter(lambda c: c["age"] <= 40, customers))

    def calculate_discount(customer):
        if 18 <= customer["age"] <= 25:
            rate = 0.10
        elif 26 <= customer["age"] <= 40:
            rate = 0.05
        else:
            rate = 0
        final_amount = round(customer["purchase"] * (1 - rate), 2)
        return {
            "customer": customer["name"],
            "age": customer["age"],
            "final_purchase": final_amount
        }

    discounted_customers = list(map(calculate_discount, eligible_customers))
    no_discount_customers = list(filter(lambda c: c["age"] > 40, customers))

    print("Discount Applied:")
    for dc in discounted_customers:
        print(f"{dc['customer']} (Age {dc['age']}) : {dc['final_purchase']}")

    print("No Discount:")
    for nc in no_discount_customers:
        print(f"{nc['name']} (Age {nc['age']}) : {nc['purchase']}")

for i in range(n):
    print(f"\nEnter details for customer {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    purchase = float(input("Total Purchase Amount: "))
    customers.append({"name": name, "age": age, "purchase": purchase})

process_discounts(customers)
