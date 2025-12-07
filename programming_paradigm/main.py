# main.py
import sys

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling zero division and invalid inputs.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        return num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Invalid number."

def main():
    # Check that exactly two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function
    result = safe_divide(numerator, denominator)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
