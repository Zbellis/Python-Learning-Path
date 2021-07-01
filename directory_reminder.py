import openpyxl
import os

os.chdir('h:\\My Documents\GRO\PythonAutomation')
workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.get_sheet_by_name('Sheet2')


def printValues():
    for i in range(1,8):
        values = (i, sheet.cell(row=i, column=2).value)
        print(values)
        
printValues()


def getKey(item):
    return item[0]

