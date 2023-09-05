import os
import csv
import datetime
import time

def check_date_format(string,test):
    try:
        current_year = time.localtime().tm_year
        # print(string)
        # print(current_year)
        date1 = datetime.datetime.strptime(string, "%d/%m/%Y")
        # print(date1.year)
        # print(current_year - date1.year - 1)
        # print(type(test))
        # print(test)
        if(current_year - date1.year - 1) == int(test):
            return True
    except ValueError:
        return False

files = os.listdir('RAW_DIR/')


correct = []
errot = []
for f1 in files:
    # print(f1)
    file_size = os.path.getsize("RAW_DIR/"+f1)
    # print(file_size)
    if file_size == 0:
        # print("The file is empty")
        continue
    else:
        # print("The file is not empty")
        # print(f1)
        with open("RAW_DIR/"+f1, "r") as f:
            reader = csv.reader(f)
            next(reader)
            # print(reader)
            # print(f1)
            for row in reader:
                str1 = row[0]
                if str1.isdigit():
                    errot.append(row)
                else:
                    if(int(row[1]) > 0 and int(row[1]) < 99):
                        if(check_date_format(row[2],row[1])):
                            correct.append(row)
                        else:
                            errot.append(row)
                    else:
                        errot.append(row)
                          

with open("Cleaned_Data.csv", "a", newline="") as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['Name','Age','Date'])

    # Write the data rows
    for row in correct[1:]:
        writer.writerow(row)


with open("Error_Data.csv", "a", newline="") as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['Name','Age','Date'])

    # Write the data rows
    for row in errot[1:]:
        writer.writerow(row)
