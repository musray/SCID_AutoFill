import re
def split_by_lang(message):
    # TODO 根据\n的位置，把message里的中文和英文分开
    # 规则：
    # 1. 连续英文、数字和空格
    # 2. 以`\n`或^开头
    # 3. 以`\n`或&结尾

    # 应对后英文先中文的情况
    pattern1 = r'(\n[a-zA-Z0-9 \n]+)$'
    # 应对先英文后中文的情况
    pattern2 = r'(^[a-zA-Z0-9 \n]+)\n'

    r1 = re.findall(pattern1, message)
    r2 = re.findall(pattern2, message)

    if r1:
        eng_message = r1[0]
        zh_message = re.sub(eng_message, '', message)
    elif r2:
        eng_message = r2[0]
        zh_message = re.sub(eng_message, '', message)
    else:
        eng_message = None
        zh_message = None

    return (eng_message, zh_message)

    

# message = 'A 列 ASG 给 SG1 补水不可用手动\n复位\nASG TRAIN A ON SG1\nUNUSABLE MANUAL RESET'
message = 'ASG TRAIN A ON SG1\nUNUSABLE MANUAL RESET\nA 列 ASG 给 SG1 补水不可用手动\n复位'
result = split_by_lang(message)
print(result)