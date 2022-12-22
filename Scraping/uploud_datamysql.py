import xlrd
import mysql.connector
from openpyxl import Workbook, load_workbook

conn = mysql.connector.connect(host='localhost',user='root',password='', database='imagesimilaarity')
cur=conn.cursor()
print("database connected")
loc=('C://Users//Tegar//Documents//Github//tokopedia_scrap//dataset.xlsx')
l=list()
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,21):
    l.append(tuple(sheet.row_values(i)))
    print(l)
    q="insert into dataset(Images,)values(%s)"
    cur.executemany(q,l)
    conn.commit()
    conn.close()