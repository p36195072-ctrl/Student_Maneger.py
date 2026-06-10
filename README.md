Student Manager with Dictionary

A beginner-friendly Python project that demonstrates how to store and manage student information using dictionaries.

📌 Description

This program:

Takes a student's name as input
Takes the student's age
Stores the data in a dictionary
Displays all saved students
Shows the total number of students
Stops when the user enters "exit"

🧠 Concepts Used

Dictionaries
Key-Value Pairs
while True loop
User Input
String Methods (strip(), lower())
Conditional Statements (if)
continue
len() function

💻 Code

student = {}

while True:
    name = input("Enter your student name:")
    name = name.strip()

    if name.lower() == "exit":
        break

    if name.strip() == "":
        print("Cannot be empty")
        continue

    age = int(input("Enter the students age:"))

    student[name] = age

    print(student)
    print("done")
    print("Total number of students:", len(student))

▶️ Example Output

Enter your student name: Rahul
Enter the students age: 16

{'Rahul': 16}
done
Total number of students: 1

Enter your student name: Aman
Enter the students age: 15

{'Rahul': 16, 'Aman': 15}
done
Total number of students: 2

Enter your student name: exit

🎯 Learning Outcome

By building this project, you will learn:

How to use dictionaries
How to store data as key-value pairs
How to take multiple inputs
How to validate user input
How to count dictionary entries using len()
