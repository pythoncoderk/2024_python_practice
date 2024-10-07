import openpyxl

wb = openpyxl.load_workbook("excel003.xlsx")
sheet = wb.active

for row in range(3, 14):
    sheet.row_dimensions[row].height = 5

for col in range(3, 14):
    letter = openpyxl.utils.get_column_letter(col)
    sheet.column_dimensions[letter].width = 1

wb.save("tmp.xlsx")