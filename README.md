# 为华龙SCID设计开发的工具

## 1. 开发记录

### openpyxl
打开一个Excel文件
```python
```

打开文件中的一个sheet


找到sheet页中的一个cell


获得一个sheet中的列

## 2. 工具使用

### 限制条件
1. 仅在`xlsx`，`xlsm`格式下测试通过；无`x`的Excel文件格式不要擅自尝试
1. SCID的数据库文件，放到`/target`文件夹
1. 设计院输入的xlsx文件，放到`/source`文件夹
1. 文件要解密