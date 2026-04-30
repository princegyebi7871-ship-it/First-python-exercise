# 1Requirement for passing an exam is that, student must pass the exam by a score of 25 or more and
# must also pass the assessment by 15 or more to get a
# certificate.
exam_score = int(input("Enter the exam score: "))
assessment_score = int(input("Enter the assessment score: "))
if exam_score >= 25 and assessment_score >= 15:
    print("Congratulations! You have passed the exam and assessment. You are eligible for a certificate.")


#  2. If a student score a total grade of 39 both grading component (i.e. if only a student score exam 25 and
# assessment 14 totaling 39, or exam 24 and assessment 15 totaling 39), the student is condoned.
total_score = exam_score + assessment_score       
if total_score == 39:
    print("You have been condoned.")

# 3. If a student satisfy either Requirement 1 or Requirement. 2 and have paid their fees in full (where fee is 100), they are issued with a certificate.
fee_paid = int(input("Enter the fee paid: "))       
if (exam_score >= 25 and assessment_score >= 15) or total_score == 39:
    if fee_paid == 100:
        print("Congratulations! You have been issued a certificate.")
    else:
        print("Please pay the full fee to receive your certificate.")
# 4. A student is deemed to have failed if he/she does not meet Requirement. 1 or Requirement. 2
if exam_score < 25 and assessment_score < 15 and total_score != 39:
    print("You have failed the exam and assessment.")   

# 5. However, your program must inform a student which component he/ she passed/failed.       
if exam_score >= 25:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")

if assessment_score >= 15:
    print("You have passed the assessment.")
else:
    print("You have failed the assessment.")
# 6. Where a student fail both components he/she is repeated.
if exam_score < 25 and assessment_score < 15:
    print("You have failed both components. You will be repeated.") 

# NOTE: The program should accept data(input) from the user.
full_name = input("Enter your full name: ")
print(f"Student Name: {full_name}")

# a. Python does not provide a switch case statement, but it offers few workarounds to make this statement work like The (if-else conditions).
grade = input("Enter your grade (A, B, C, D, F): ") 
if grade == "A":
    print("Excellent!")
elif grade == "B":
    print("Good job!")
elif grade == "C":
    print("Well done!")
elif grade == "D":
    print("You passed.")
elif grade == "F":
    print("Better luck next time.")
else:
    print("Invalid grade entered.")

#c. Let your program generate summary of the student report including the students full name.
print("\nStudent Report Summary:")  
print(f"Name: {full_name}")
print(f"Exam Score: {exam_score}")
print(f"Assessment Score: {assessment_score}")
print(f"Total Score: {total_score}")
print(f"Grade: {grade}")

#d. The program should be able to handle invalid input gracefully.
try:
    exam_score = int(input("Enter the exam score: "))
    assessment_score = int(input("Enter the assessment score: "))   
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()      
    

