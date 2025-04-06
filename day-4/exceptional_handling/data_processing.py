def process_data(data, index):
    try:
        int_data = [int(x) for x in data]
        divisor = int_data[index]
        result = int_data[0] / divisor
        return result

    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError:
        return "Error: Invalid value for conversion to int"
    except IndexError:
        return "Error: Index out of range"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 2))  
print(process_data(["10", "abc", "30"], 1))  
print(process_data([10, 20], 5))  
