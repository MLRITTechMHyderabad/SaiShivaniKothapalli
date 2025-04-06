def calculator(a, b, operator):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Invalid input type")
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero")
            return a / b
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError("Modulo by zero")
            return a % b
        elif operator == "**":
            return a ** b
        else:
            raise ValueError("Unsupported operator")

    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"
    except ValueError:
        return "Error: Unsupported operator"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"
