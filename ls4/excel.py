import openpyxl

workbook = openpyxl.load_workbook('tabel.xlsx')
sheet = workbook.active

data = []
for row in sheet.iter_rows(values_only=True):
    data.append(row)

print(data)
