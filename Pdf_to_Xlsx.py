import pdfplumber
import openpyxl
from openpyxl import Workbook

path = r"D:\1\Py_read\2006-全国投运城镇污水处理设施清单.pdf"
pdf_mt = pdfplumber.open(path)


all_pages = pdf_mt.pages
need_pages = all_pages 

MaxPage = 9999
for pdf_pg in all_pages[0:MaxPage]:
    print(pdf_pg.extract_text())
for pdf_pg in all_pages[0:MaxPage]:
    print(pdf_pg.extract_tables())

wb = Workbook()
ws = wb.active
for pdf_pg in all_pages[0:MaxPage]:
    for pdf_tb in pdf_pg.extract_tables():
        for row in pdf_tb:
            ws.append(row)
wb.save(r'D:\1\Py_output\2006.xlsx')
print('2006,Done!')