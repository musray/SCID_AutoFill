import os
# import collections
from openpyxl import load_workbook

files = os.listdir('./source')
col_keyword = '功能描述'
# Cell = collections.namedtuple('Cell', ['ID', 'description'])

pool = []
for file in files:
    wb = load_workbook(os.path.join(os.getcwd(), 'source', file)) 
    ws = wb.active
    # id_des = [(row[3].value, [row[3].value]) for row in ws]
    id_des = []
    double_description_col = col_keyword in ws['D1'].value
    for row in ws.rows:
        # print(row)
        id = row[0].value
        description = [row[2].value]
        if double_description_col:
            description.append(row[3].value)
        id_des.append((id, description))
    pool.extend(id_des)    

print(pool)