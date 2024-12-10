import json 
 #you are given a json file name students.json,which contains informations about student and their rates.your task is to
        #read the json file 
        #display the name of all students who scopped about 75
        #add the new student repost to the find
        #save the updated data back to the json file 



def read_students(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def display_top_students(data):
    print("Students who scored above 75:")
    for student in data['students']:
        if student['score'] > 75:
            print(f"- {student['name']}")


def add_new_student(data):

    name = input("Enter the new student's name: ")
    address =input("input your address")
    score = int(input(f"Enter {name}'s score: "))
    new_student = {"name": name,"address": address, "score": score}
    data['students'].append(new_student)
    print(f"Added {name} with a score of {score}.")
    return data

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {file_name} successfully.")

    file_name="pythonFOlders/textFOlders/studentsData"


while True:
    print("\n----Score manager----")
    print("1-View students")
    print("2-Add student")
    print("3-view top Scores students")
    try:
        press = int(input("Enter your choice: "))
        if press == 1:
            read_students()
        elif press == 2:
            add_new_student()
        elif press == 3:
           display_top_students()
        elif press == 4:
            print("end")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")