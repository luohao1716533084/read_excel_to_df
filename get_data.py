#coding:utf-8

from functools import reduce
from pandas_excel import *
from sheet_cols import *
from relate_operate import *
import os


class getDataSheet():
    def __init__(self, excel_dict):
        self.excel_dict = excel_dict
        self.path_list = self._get_excel_path()
        self.header_num = excel_dict['n']
        for path in self.path_list:
            if ".csv" in path:
                self.csv_type = True
            else:
                self.csv_type = False

        self.df_csv = []
        self.df_xlsx = []

    def _get_excel_path(self,):
        # 获取当前文件夹所有文件路径
        current_path = os.getcwd()
        file_path_list = []
        for root, dirs, files in os.walk(current_path):
            for name in files:
                file_path_list.append(os.path.join(root, name))
        # 匹配文件名关键字，返回包含关键字的文件路径
        excel_name = self.excel_dict['excelName']
        res = []
        for i in file_path_list:
            if excel_name in i:
                res.append(i)
        print(res)
        return res

    def _get_sheet_data(self, excelPath):
        sheet_name, columns_list, n, flag = self.excel_dict['sheetName'], self.excel_dict['cols'], self.excel_dict['n'], self.excel_dict['flag']
        dataframe = OpenExcel(excelPath, sheet_name, columns_list)
        if flag == "A":
            df = dataframe.pre_process_typeA(n)
        else:
            df = dataframe.pre_process_typeB(n)
        return df

    def _read_csv(self,):
        columns_list = self.excel_dict['cols']
        for path in self.path_list:
            try:
                df = pd.read_csv(path, encoding="utf-8", header=self.header_num)[columns_list]
            except UnicodeDecodeError:
                df = pd.read_csv(path, encoding="gb18030", header=self.header_num)[columns_list]
            self.df_csv.append(df)

    def _merge_df_csv(self,):
        self._read_csv()
        merged_df = pd.concat(self.df_csv, ignore_index=True)
        return merged_df

    def _read_xlsx(self,):
        for path in self.path_list:
            df = self._get_sheet_data(path)
            self.df_xlsx.append(df)

    def _merge_df_xlsx(self):
        self._read_xlsx()
        merged_df = pd.concat(self.df_xlsx, ignore_index=True)
        return merged_df

    def get_excel_df(self):
        if self.csv_type:
            return self._merge_df_csv()
        else:
            return self._merge_df_xlsx()

    # def reColName(self, df):
    #     df.columns = self.excel_dict['colsAlias']
    #     return df



