# encoding = utf-8
# =====================================================
#   Copyright (C) 2019 All rights reserved.
#
#   filename : easy_pie.py
#   version  : 0.1
#   author   : gongzi.xu / 95168339@qq.com
#   date     : 2021/01/09
#   desc     :
# =====================================================

import os, json
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from ui.Ui_main import Ui_MainWindow
from ui.ImageWindow import ImageWindow
from worker.load_excel import LoadExcel
from worker.update_check import UpdateCheck
from charts.render_pie import RenderPie
from charts.color_schemes import color_schemes

import webbrowser

from ui import images_rc

CURRENT_VERSION = 0.1
SETTINGS_JSON_PATH = "./settings/settings.json"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.comboBox_format_data.hide()
        self.tab_data.hide()
        self.init_sign()
        self.init_data()
        self.label_progress.setOpenExternalLinks(True)

    def init_data(self):
        self.df = None
        # 初始化颜色选择窗
        self.color_schemes = color_schemes
        self.comboBox_select_color.addItems(self.color_schemes.keys())
        self.init_charts_comboBox()
        self.settings_json = self.read_local_json(fp=SETTINGS_JSON_PATH)
        # 从云端拉取settings_json
        self.update = UpdateCheck(current_verison=CURRENT_VERSION)
        self.update.result_signal.connect(self.refresh_settings_json)
        self.update.start()

    def refresh_settings_json(self, settings_json):
        self.settings_json = settings_json
        self.check_update_version(is_start=True)

    def read_local_json(self, fp):
        with open(fp, 'r', encoding='utf8')as f:
            _json = json.load(f)
            return _json

    def init_charts_comboBox(self):
        self.label_style_formatters = {
            "仅名称": "{b}",
            "仅数值": "{c}",
            "仅百分比": "{d}",
            "名称和数值": "{b}: {c}",
            "名称和百分比": "{b}: {d}%"
        }

        self.comboBox_style_label.addItems(self.label_style_formatters.keys())

    def init_sign(self):
        self.tabWidget.currentChanged.connect(self.change_tab)
        self.action_help.triggered.connect(self.help)
        self.action_aboutme.triggered.connect(self.about)
        self.action_check_update.triggered.connect(self.check_update_version)

        self.toolButton_update.clicked.connect(self.check_update_version)
        self.toolButton_help.clicked.connect(self.help)
        combo_lst = [self.comboBox_select_col, self.comboBox_select_color, self.comboBox_style_label]
        for combo in combo_lst:
            combo.activated.connect(self.render_pie)
        checkbox_lst = [self.checkBox_donut, self.checkBox_legend, self.checkBox_rose, self.checkBox_label_place]
        for checkbox in checkbox_lst:
            checkbox.clicked.connect(self.render_pie)
        txt_edit_lst = [self.lineEdit_title, self.textEdit_color]
        for txt_edit in txt_edit_lst:
            txt_edit.textChanged.connect(self.render_pie)

        # 添加关注公众号弹窗
        self.support_me_window = ImageWindow(':/main/img/supportme.jpg', '支持我一下吧！')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/charts.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.support_me_window.setWindowIcon(icon)
        self.toolButton_supportme.clicked.connect(self.show_support_me)

    @pyqtSlot()
    def on_toolButton_load_clicked(self):

        self.fp = self.open_file_dialog()
        print("获取到的filepath:%s" % self.fp)
        if self.fp not in [None, ""]:
            self.load_excel(fp=self.fp)

    def show_support_me(self):
        self.support_me_window.show()

    def open_file_dialog(self):
        fileName, fileType = QFileDialog.getOpenFileName(self,
                                                         "选择文件",
                                                         r"%s" % os.getcwd(),
                                                         "文件类型(*.xlsx;*.xls);")  # 设置文件扩展名过滤

        fileName = fileName.replace('/', '\\')  # windows下需要进行文件分隔符转换
        return (fileName)

    def closeEvent(self, QCloseEvent):
        reply = MyQMessageBox('温馨提示', '确定要退出吗？', '确定退出', '再看看吧')
        if reply == 16384:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def load_excel_done(self, df):
        self.df = df
        # 下拉框中添加列名
        self.comboBox_select_col.clear()
        self.comboBox_select_col.addItem("选择列")
        self.comboBox_select_col.addItems(df.columns)

    # def load_excel_
    def load_excel(self, fp):
        self.load = LoadExcel(excel_filepath=fp)
        self.load.result_signal.connect(self.load_excel_done)
        self.load.progress_signal.connect(self.show_progress)
        self.load.start()

    def messageBox_error_warn(self, error_str):
        QMessageBox.information(self, "错误警告", "%s" % error_str, QMessageBox.Yes)

    def show_progress(self, _str):
        if "done" in _str:
            self.label_progress.setVisible(False)
        else:
            self.label_progress.setVisible(True)
            self.label_progress.setText(_str)

    def show_html_progress(self, _str):
        self.label_html.setText(_str)

    def about(self):

        if "about_me_url" in self.settings_json.keys():
            reply = QMessageBox.information(self, "关于", "当前版本号：%s\n作者：夜雨微寒 \n需要访问作者的个人主页吗？" % CURRENT_VERSION,
                                            QMessageBox.No, QMessageBox.Yes)
            if reply == 16384:
                webbrowser.open(self.settings_json.get("about_me_url"))
            else:
                pass
        else:

            QMessageBox.information(self, "关于", "当前版本号：%s\n作者：gongli.xu " % CURRENT_VERSION,
                                    QMessageBox.Yes)

    def check_update_version(self, is_start=False):

        latest_version = self.settings_json.get("latest_version")
        print(latest_version)
        latest_release_url = self.settings_json.get("latest_release_url")
        if latest_version > CURRENT_VERSION and latest_release_url != "":
            details = self.settings_json.get("update_details")

            reply = QMessageBox.information(self, "温馨提示", "发现新的版本，需要跳转到下载页面吗？" + "\n" + "更新内容：\n %s" % details,
                                            QMessageBox.No, QMessageBox.Yes)
            print(reply)
            if reply == 16384:
                self.visit_latest_version_url(latest_release_url)
        else:
            if not is_start:
                QMessageBox.information(self, "温馨提示", "已经是最新版本了哦！", QMessageBox.Yes)

    def help(self):

        if 'help_url' in self.settings_json.keys():
            help_url = self.settings_json.get("help_url")
        else:
            help_url = "https://mp.weixin.qq.com/mp/homepage?__biz=Mzg5NzIyODU3Mg==&hid=5&sn=66156a443cc3adfc7e0bd37c83e3d7a7&scene=18&uin=&key=&devicetype=Windows+10+x64&version=63010043&lang=zh_CN&ascene=7&fontgear=2"
        webbrowser.open(help_url)

    def visit_latest_version_url(self, latest_release_url):
        webbrowser.open(latest_release_url)
        print(latest_release_url)

    def change_tab(self):

        if self.tabWidget.currentIndex() == 0:
            pass
        elif self.tabWidget.currentIndex() == 1:
            pass

    def render_pie(self):
        col_name = self.comboBox_select_col.currentText()
        if self.df is not None and self.comboBox_select_col.currentIndex()!=0:

            is_donut = self.checkBox_donut.isChecked()
            is_rose = self.checkBox_rose.isChecked()
            show_legend = self.checkBox_legend.isChecked()
            title = self.lineEdit_title.text()
            label_position = self.checkBox_label_place.isChecked()
            label_formatter = self.comboBox_style_label.currentText()
            if label_formatter == '选择标签样式':
                # 默认使用数据项名称+百分比
                label_formatter = list(self.label_style_formatters.keys())[-1]
            color_scheme_item = self.comboBox_select_color.currentText()
            if color_scheme_item == "选择配色":
                color_scheme_item = list(self.color_schemes.keys())[0]
            color_scheme = self.color_schemes[color_scheme_item]
            try:
                customized_colors = eval(self.textEdit_color.toPlainText())
                # 如果列表不为空
                if isinstance(customized_colors, list) and len(customized_colors) > 0:
                    color_scheme = customized_colors
                    self.show_progress("当前图表已经使用了您的自定义颜色！")
            except:
                if self.textEdit_color.toPlainText().strip() != "":
                    self.show_progress("您输入的自定义颜色格式不正确哦！<a href='%s'>点击查看帮助文档</a>"%self.settings_json.get("help_url"))

            # 如果有用户自定义的颜色，则优先使用

            self.render_pie = RenderPie(df=self.df,
                                        col_name=col_name,
                                        is_donut=is_donut,
                                        is_rose=is_rose,
                                        show_legend=show_legend,

                                        title=title,
                                        label_position=label_position,
                                        label_formatter=self.label_style_formatters[label_formatter],
                                        color_scheme=color_scheme

                                        )
            self.render_pie.result_signal.connect(self.show_charts)
            self.render_pie.progress_signal.connect(self.show_progress)
            self.render_pie.charts_data_signal.connect(self.show_charts_data)
            try:
                self.render_pie.start()
                self.tabWidget.setCurrentIndex(0)
            except Exception as e:
                self.show_progress("好像哪里不对！错误详情：%s" % e)

    def show_charts(self, render_embed_str):
        self.web_view.setHtml(render_embed_str)

    def show_charts_data(self, charts_data):
        # self.tableWidget_data.setHorizontalHeaderLabels(('第一列', '第二列'))
        row_count = 0
        self.tableWidget_data.setRowCount(len(charts_data))
        for data in charts_data:
            print(data)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 无法编辑
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(str(data[0]))
            self.tableWidget_data.setItem(row_count, 0, item)

            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 无法编辑
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(str(data[1]))
            self.tableWidget_data.setItem(row_count, 1, item)

            row_count += 1


def MyQMessageBox(title, text, button1, button2=None):
    messageBox = QMessageBox()
    messageBox.setWindowTitle(title)
    messageBox.setWindowIcon(QtGui.QIcon(':/icon/img/charts.png'))
    messageBox.setText(text)
    if button2:
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = messageBox.button(QMessageBox.Yes)
        buttonY.setText(button1)
        buttonN = messageBox.button(QMessageBox.No)
        buttonN.setText(button2)
    else:
        messageBox.setStandardButtons(QMessageBox.Yes)
        buttonY = messageBox.button(QMessageBox.Yes)
        buttonY.setText(button1)

    messageBox.exec_()
    if messageBox.clickedButton() == buttonY:
        return 16384
    else:
        return 0


def show_loading():
    # 创建QSplashScreen对象实例
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":/main/img/EasyCharts.png"))
    # 设置画面中的文字的字体
    splash.setFont(QFont('Microsoft YaHei UI', 10))
    # 显示画面
    splash.show()
    # 显示信息
    splash.showMessage("启动中……", QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.finish(MainWindow)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    with open("./themes/MacOS.qss", 'r', encoding='utf8') as f:
        style = f.read()
    MainWindow.setStyleSheet(style)
    show_loading()  # 显示启动加载页面
    # MainWindow.setStyleSheet(qss_style)
    # MainWindow.setWindowIcon(QtGui.QIcon("./favicon.ico"))
    MainWindow.show()  # 当主界面显示后销毁启动画面
    sys.exit(app.exec_())
