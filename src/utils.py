# Utility Functions
# Author: Laraib Kaleem

# *Why:* Keep your actual code files organized
# *What goes here:* Python scripts, modules, classes
# *Example:* model.py, utils.py, data_processing.py

def print_separator(char="-", length=50):
    """Print a separator line"""
    print(char * length)

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

def calculate_percentage(part, total):
    """Calculate percentage"""
    return (part / total) * 100

# Test functions
if __name__ == "__main__":
    print_separator()
    print("Utility Functions Test")
    print_separator()
    print(format_currency(1234.56))
    print(f"Percentage: {calculate_percentage(25, 100):.1f}%")
