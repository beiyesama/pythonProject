import xlrd
class ExcelRead:
    def __init__(self,path,sheetname):
        self.data = xlrd.open_workbook(path)
        self.table = self.data.sheet_by_name(sheetname)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.nrows = self.table.nrows
        #获取总列数
        self.ncols = self.table.ncols
    def get_data(self):
        data = []
        if self.nrows <= 1:
            print("没有参数数据")
        else:
            for i in range(self.nrows-1):
                row_data = self.table.row_values(i+1)
                rows_data = {}
                for x in range(self.ncols):
                    rows_data[self.keys[x]] = row_data[x]
                data.append(rows_data)
        return data

