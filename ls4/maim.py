import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet['A1'] = "Full Name"
sheet['B1'] = "Subject"
sheet['C1'] = "Exam mark"

student_data = [
    ('Ann', 'Math', 90),
    ('Ann', 'History', 90),
    ('Ann', 'Geometry', 90),
    ('Ann', 'Chimy', 90),
]

for idx, (name, subject, mark) in enumerate(student_data, start=2):
    sheet[f'A{idx}'] = name
    sheet[f'B{idx}'] = subject
    sheet[f'C{idx}'] = mark

workbook.save('tabel.xlsx')
print("data saved")