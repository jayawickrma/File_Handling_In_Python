import json 
 #you are given a json file name students.json,which contains informations about student and their rates.your task is to
        #read the json file 
        #display the name of all students who scopped about 75
        #add the new student repost to the find
        #save the updated data back to the json file 


name=input("Enter Your Name :")
address = input("Enter your address :")
age=input("enter your age :")

studentData ={
    "Name ": name,
    "Address " : address,
    "Age ": age
}
with open("pythonFOlders/textFOlders/studentsData",'w')as file:
    student = json.dumps(studentData)
    file.write(student)

with open("pythonFOlders/textFOlders/studentsData",'r')as file:
    read_student =json.load(file)
    print(read_student)