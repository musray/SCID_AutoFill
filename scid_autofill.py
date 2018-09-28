# -*- coding: utf-8 -*-
import os
import traceback
import collections
from openpyxl import load_workbook
from load_source import load_source

def long_str_split(message):
    
    chunk = ''
    strict = 22  # SCID设计人员要求 
    l_final = []
    origin_list = message.split()

    for index, word in enumerate(origin_list):
        if len(chunk + ' ' + word) < strict:
            chunk += (' ' + word)
            # print(chunk)
        else:
            # chunk += (' ' + word)
            l_final.append(chunk.strip())
            chunk = word 

        if index == len(origin_list) -1:
            l_final.append(chunk.strip())

    # print('l_final', l_final)
    return l_final

def main(target_file):

    ####### 在这里做一些设定 #######
    sheet_titles = ['OWP', 'ACP', 'RSS', 'DTC'] # SCID Excel数据库文件固定的sheet页名称
    lang_selector = 0   # 1 for Chinese, 0 for English; 1和0的含义，跟load_source函数中return的结果有关系

    source_pool = load_source()
    source_ids = [element[0].strip() for element in source_pool]
    # print(source_ids)
    target_wb = load_workbook(target_file, keep_vba=True)

    # print(source_pool)
    for sheet in target_wb:
        # 在target.xlsm文件里，肉眼只能看见4张sheet
        # 但用代码读取的时候，能看见n多张sheet
        # 所以写了下面这一行，限制一下：
        
        if sheet.title in sheet_titles:
            # 看一看H列都有多少行
            # print('len of column %s: %s' % (sheet.title ,len(sheet['H'])) )

            # values = [(cell.value, ) for cell in sheet['H']]
            iteror = 7
            # target_cells = []
            # 对于当前sheet，H列(点名)的每个cell来说
            for cell in sheet['H'][7:]:
                if cell.value and (cell.value.strip() in source_ids):
                    # 从source_pool里拿出与点名对应的描述
                    description = source_pool[source_ids.index(cell.value.strip())][1]
                    for index, item in enumerate(long_str_split(description[lang_selector])):
                        sheet['K'+str(iteror+1+index)].value = item 
                iteror += 1

    target_wb.save(os.path.join('./output/', os.path.basename(target_file)))
    target_wb.close()

if __name__ == '__main__':
    # print(os.getcwd())
    input('确认 source, target, output 三个文件夹是否存在\n回车开始....')
    try:
        input('工作中....请稍等....')
        target_files = [file for file in os.listdir('./target') if file.endswith(('xlsm', 'xlsx'))]
        for file in target_files:
            main(os.path.join('./target', file))
    except Exception as e:
        with open('log.txt', 'w') as f:
            f.write(str(e))
            f.write(traceback.format_exc())
        print('有错误发生，转换终止，错误信息参考 log.txt')
    
    input('转换完成，在 output 文件夹中查看新生成的文件\n回车退出....')
        