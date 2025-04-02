d1 = {}
d2 = {}
n = int(input("Enter the number of key-value pairs: "))
def merge_dict():
    for i in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        d1[key] = value  
    return d1
print("1st dictionary")
d1=merge_dict()
print("2nd dictionary")
d2=merge_dict()
merged_dict={**d2, **d1}  
print("Merged dict: " , merged_dict)
