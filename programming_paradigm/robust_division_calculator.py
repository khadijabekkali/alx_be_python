# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling.

    Args:
        numerator: The numerator (can be string or number)
        denominator: The denominator (can be string or number)

    Returns:
        Result of division or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
