'''
This is to play around with excel file editiong
'''

import openpyxl as xl
from openpyxl.chart import BarChart, Reference
import random

wb = xl.load_workbook('Exotica_Sales.xlsx')

sheet = wb['Sales Data']
sheet.cell(1,4).value = 'Discount'
sheet.cell(1,5).value = 'Actual Price'

for row in range(2,sheet.max_row + 1):
    sheet.cell(row,4).value = random.randint(10,20)
    sheet.cell(row,5).value = (sheet.cell(row,2).value) * (sheet.cell(row,3).value) * (100 - sheet.cell(row,4).value)/100

values = Reference(sheet, min_row=2, max_row=sheet.max_row + 1, min_col=4, max_col=4)

chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, 'f5')

wb.save('Exotica_Sales_Updated.xlsx')
wb.close()

