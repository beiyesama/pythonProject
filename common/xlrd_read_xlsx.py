import xlrd
class ExcelRead:
    def r(self,path,sheetname):
        self.data = xlrd.open_workbook(r"path")
        self.table = self.data.sheet_by_name()