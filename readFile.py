# file_1 =open("filehandling.txt",'r')   # open method in python,in the bracket you must add the file path

# # content =file_1.read()                 # in build command to read the content 
# # content1 =file_1.readline()            # in this method print the only one line
# readlines =file_1.readlines()            # return the text like a List
# file_1.close()                           #close the text file
# print(readlines)                         # print the content



with open("filehandling.txt",'r')as file:
    content =file.read()
    print(content)