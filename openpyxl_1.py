import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

for i in range(10):
    ws.append([i,i+1,i+2])

wb.save("test.xlsx")

