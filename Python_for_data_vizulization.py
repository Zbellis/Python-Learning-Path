import os
import openpyxl

os.chdir('H:\\My Documents\\GRO\\PythonAutomation')

workbook = openpyxl.load_workbook('runs_c.xlsx')
sheet = workbook.get_sheet_by_name('result')


def printValues():
    for i in range(1,8):
        values = (i, sheet.cell(row=i, column=2).value)
        print(values)
        
printValues()


def getKey(item):
    return item[0]
