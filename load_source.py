import os
from openpyxl import load_workbook

files = os.listdir('./source')

signal_pool = []
for file in files:
    wb = load_workbook(os.path.join(os.getcwd(), 'source', file)) 
    ws = wb.active
    print(ws.title)