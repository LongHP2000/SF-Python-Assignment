#---------------------------------------------------
#------On 10/02/2025 by Long Pham
#------Elizabeth School of London and Bath Spa University
#------Course      : BSc Computing Foundation year, Semester 2, 2024 to 2025
#------Description : Module Software Foundation, tutorial week 4 Python file handling tutorial 
#------Description : Module Computational Reasoning, tutorials week 2 to 7 on how to create Excel formulas
#----------------------------------------------------

#-----Checked Students.csv file for spelling errors in headings and names-----
#-----Check numbers are integers and not floats-----
import csv  # Import the Students.CSV module for file handling

#-----Define Functions-----
def calculate_average(scores):
    """
    Calculate the average score from a list of scores.
    Ensures division by zero does not occur if the list is empty.
    """
    return sum(scores) / len(scores) if scores else 0  # Prevents division by zero

def assign_grade(average):
    """
    Assign a grade based on the calculated average score.
    If equal to or over 85, grade is A etc.  
    """
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

#-----Import Student Data-----
students = []  # List to store processed student data

try:
    # Open the Students.csv file and read the contents
    with open('Students.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)  # Create a CSV reader object
        
        # Read the header row, which are Name, Art, English, Maths (first row in the file)
        header = next(reader)
        
        # Check if the file contains enough columns (at least one name and some scores)
        if len(header) < 4:
            raise ValueError("CSV file does not contain enough columns.")

        # Iterate through each student record in the file
        for row in reader:
            try:
                name = row[0]  # First column is the student's name
                scores = list(map(int, row[1:]))  # Convert score columns to integers
                average = calculate_average(scores)  # Calculate the average score
                grade = assign_grade(average)  # Assign a grade based on the average
                students.append([name] + scores + [average, grade])  # Store processed data
            except ValueError:
                print(f"Skipping invalid row: {row}")  # Skip rows with invalid data (non-numeric values)

    #-----Create a new file named Student_Results.CSV and save Results to this new file-----
    with open('Student_Results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)  # Create a CSV writer object

        #-----Writing the new header with additional columns (Average & Grade)
        #-----Display results in Student_Results.csv file
        writer.writerow(header + ['Average', 'Grade'])
        writer.writerows(students)  # Write the processed student data

# Confirm successful execution of python coding
    print('Results successfully saved to Student_Results.csv')  

# Error handling display a message
except FileNotFoundError:
    print("Error: The file 'Students.csv' was not found.")  # Error message if file is missing
except Exception as e:
    print(f"An error occurred: {e}")  # General error handling for unexpected issues

#-----Program Ends Successfully-----