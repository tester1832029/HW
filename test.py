import numpy as np
import openpyxl

wb=openpyxl.Workbook()
sheet=wb.active
path='result.txt'
data=np.random.randint(1,10,(100,20))
average=[np.mean(i) for i in data]

with open(path,mode='w') as w:
    for i in range(100):
        w.write(f"data{i+1}: {data[i]}  mean = {average[i]}\n")

for i,j in enumerate(average):
    sheet.cell(row=i//10+1,column=i%10+1,value=j)
wb.save('sample.xlsx')
