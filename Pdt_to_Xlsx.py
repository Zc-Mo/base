import pdfplumber
import openpyxl
from openpyxl import Workbook

path = r"D:\1\Py_read\2006-全国投运城镇污水处理设施清单.pdf"
pdf_mt = pdfplumber.open(path)

# 获取到数据所在页  list --> [第一页的对象,第二页的对象,...第n页的对象]
all_pages = pdf_mt.pages
need_pages = all_pages 

#读取范围,从第x页到第y页
MaxPage = 9999
for pdf_pg in all_pages[0:MaxPage]:
    print(pdf_pg.extract_text())
#
for pdf_pg in all_pages[0:MaxPage]:
    print(pdf_pg.extract_tables())

wb = Workbook()
ws = wb.active
for pdf_pg in all_pages[0:MaxPage]:
    # print(pdf_pg)
    # 获取每页的文本内容
    # print(pdf_pg.extract_text())

    # 获取表格内容 表格：二维 [[],[]]
    # print(pdf_pg.extract_tables())
    # 表格有行有列的二维数据，获取二维的列表

    for pdf_tb in pdf_pg.extract_tables():
        # print(pdf_tb)
        # 将数据一行一行的写入工作表
        for row in pdf_tb:
            ws.append(row)
wb.save(r'D:\1\Py_output\2006.xlsx')
print('2006,Done!')