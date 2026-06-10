student = {}
while True:
    name = input("Enter your student name:")
    name = name.strip()

    if name.lower() == "exit":
        break

    if name.strip() == "":
        print("Cannot be emty")
        continue

    age = int(input("Enter the students age:"))
    if name.strip() == "":
    
        print("Cannot be emty")
        continue

    
        


    student[name]= age
    
    print(student)
    print ("done")
    print("Total number of students:", len(student))


    