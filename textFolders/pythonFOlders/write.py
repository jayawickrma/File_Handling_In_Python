with open("textFolders/myFile1",'w')as file:
    list =["hello python \nthis is out python class"]  #sending values to the text file as a list type
    # list.append("\nappend the text using append ")    # append the new line to the text file
    file.writelines(list)                              #write the list type value in the text file

with open("textFolders/myFile1",'a')as file:        # 'a' this is the append mode in the file handling
    file.write("\noiiiiiiiiiiiiiiiiiii")            # add a new text in to that textfile



