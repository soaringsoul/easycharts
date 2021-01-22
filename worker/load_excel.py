import pandas as pd
from PyQt5 import QtCore
import time





class LoadExcel(QtCore.QThread):

    finished_signal = QtCore.pyqtSignal(str)
    error_signal = QtCore.pyqtSignal(str)
    result_signal = QtCore.pyqtSignal(pd.DataFrame)
    progress_signal= QtCore.pyqtSignal(str)


    def __init__(self,excel_filepath):
        super(LoadExcel, self).__init__()
        self.excel_filepath = excel_filepath




    def run(self):

        # 拉取云端数据
        self.progress_signal.emit("正在读取Excel文件，请耐心等待")
        df = pd.read_excel(self.excel_filepath)
        self.result_signal.emit(df)
        self.progress_signal.emit("成功读取excel!")
        time.sleep(5)
        self.progress_signal.emit("done")

