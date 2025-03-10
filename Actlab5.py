def assign_grade(score):
    try:
        score = int(score)
        if 0 <= score <= 100:
            if score >= 90:
                return "A"
            elif score >= 80:
                return "B"
            elif score >= 70:
                return "C"
            elif score >= 60:
                return "D"
            else:
                return "F"
        else:
            return "Invalid score! Please enter a value between 0 and 100."
    except ValueError:
        return "Invalid input! Please enter an integer."


# Test cases
print(assign_grade(95))  
print(assign_grade(85))  
print(assign_grade(75))  
print(assign_grade(65))  
print(assign_grade(55))  
print(assign_grade(105)) 
print(assign_grade("abc")) 

# User input
score_str = input("Enter the student's score (0-100): ")
grade = assign_grade(score_str)
print(f"The grade is: {grade}")