import csv
import os

f = open("sales_data.csv","r")
# print(f.read())

for i in f:
    reader = csv.reader(f)
    def display():
        print(i)
    def calculate_sales():
        sum = 0
        for col in reader:
            product = float(col[1])*int(col[2])
            sum += product
        print(sum)
    def maximum_sales():
        max_sales = 0
        max_product = ''
        for col in reader:
            product = float(col[1])*int(col[2])
            if product > max_sales:
                max_sales = product
                max_product = col[0]
        print(max_product,max_sales)
    def avg_sale():
        sum = 0
        count = 0
        for col in reader:
            product = float(col[1])*int(col[2])
            sum += product
            count += 1
        avg = sum/count
        print(avg)
    avg_sale()
    