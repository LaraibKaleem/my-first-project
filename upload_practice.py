# Practice Upload File
# Author: Laraib Kaleem
# Purpose: Learning to upload files from computer to GitHub

def calculate_average(numbers):
    """Calculate average of a list of numbers"""
    return sum(numbers) / len(numbers)

def main():
    # Sample data
    scores = [85, 90, 78, 92, 88]
    
    print("Student Scores:", scores)
    print(f"Average Score: {calculate_average(scores):.2f}")
    print("\n✅ File uploaded successfully from my computer!")

if __name__ == "__main__":
    main()