#---------------------------------------------------
#------On 10/02/2025 by Long Pham
#------Elizabeth School of London and Bath Spa University
#------Course      : BSc Computing Foundation year, Semester 2, 2024 to 2025
#------Description : Module Software Foundation, tutorial week 4 Python file handling tutorial 
#------Description : Module Computational Reasoning, tutorials week 2 to 7 on how to create Excel formulas
#------Program     : Python program to find out what grade according to grades between 0 to 100 marks.
#----------------------------------------------------
def grade_calculator():
    while True:
        # Prompt the user for input
        user_input = input("Enter the student's numerical grade (0-100), or type 'exit' to quit: ").strip().lower()
        
        # Check if the user wants to exit
        if user_input == 'exit':
            print("Thank you for using Student grade program.  Goodbye!") # Display goodbye message
            break
        
        try:
            # Accept converted the input float number and still display grade
            score = float(user_input)
            
            # Validate the score range
            if 0 <= score <= 100:
                # Determine the grade by letter
                if score >= 90:
                    grade = 'A'
                elif score >= 80:
                    grade = 'B'
                elif score >= 70:
                    grade = 'C'
                elif score >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                
                # Display the result onto screen
                print(f"The student's grade is: {grade}")
            else:
                print("Error: The score must be between 0 and 100.") # Error Handling non-numeric input
        except ValueError:
            # Error handling non-numeric input. Invalid input can be words, numbers over 100, minus numbers
            # Error handling, non-numeric input. Mistyped float ie 78'4, 65;1 etc
            print("Invalid input! Please enter a valid numerical grade or type 'exit' to quit.")

# Run the grade calculator
grade_calculator()
