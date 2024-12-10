import csv

csv_file_path ="Json/customers-100.csv"
with open(csv_file_path,newline="")as csv_file:
    csv=csv.reader(csv_file)            #csv.reader by uing this we can read the csv files 
    print(csv,type(csv))


  