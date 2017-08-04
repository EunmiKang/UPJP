
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import tkinter
from tkinter import messagebox

from signature.generator import Gen
from signature.detector import Detector


class Main(QMainWindow):

    #hide main window (alert window)
    root = tkinter.Tk()
    root.withdraw()

    result_massage = "악성코드로 의심되는 파일 목록\n\n"

    def __init__(self):
        super().__init__()

        self._init_ui()
        self.gen = Gen()

    def _init_ui(self):
        self._init_widget()

        self.setCentralWidget(self.table_widget)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('UPJP')
        # self.setWindowIcon(QIcon('1.png'))
        self.statusBar()
        self.show()

    def _init_widget(self):
        self._init_tab()
        self.table_widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        self.table_widget.setLayout(layout)

    def _init_tab(self):
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tab1ui()
        self.tab2ui()

        self.tabs.addTab(self.tab1, "호오오오오오오오오오옴")
        self.tabs.addTab(self.tab2, "환경설정")

    def tab1ui(self):
        layout_tab1 = QFormLayout()
        layout_btn = QFormLayout()

        self.filelist = QListWidget()
        self.filelist.setWindowTitle('Example List')
        self.filelist.setSelectionMode(QAbstractItemView.MultiSelection)

        self.filelist.setFixedSize(500, 300)

        addBtn = QPushButton("추가", self)
        deleteBtn = QPushButton("삭제", self)
        checkBtn = QPushButton("검사", self)

        addBtn.setFixedSize(100, 30)
        deleteBtn.setFixedSize(100, 30)
        checkBtn.setFixedSize(100, 30)

        addBtn.clicked.connect(self.openFileDialog)
        deleteBtn.clicked.connect(self.deleteBtnClicked)
        checkBtn.clicked.connect(self.chkBtnClicked)

        layout_btn.addRow(addBtn)
        layout_btn.addRow(deleteBtn)
        layout_btn.addRow(checkBtn)
        layout_tab1.addRow(self.filelist, layout_btn)

        self.tab1.setLayout(layout_tab1)

    def tab2ui(self):
        layout = QFormLayout()

        self.tab2.setLayout(layout)

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        items, _ = QFileDialog.getOpenFileNames(self, "Select file", "~/",
                                                "All Files (*);;Python Files (*.py)", options=options)
        for item in items:
            print("* add file :", item)
            self.filelist.addItem(item)

    def deleteBtnClicked(self):
        items = self.filelist.selectedItems()
        for item in items:
            self.filelist.removeItemWidget(item)
            self.filelist.takeItem(self.filelist.row(item))

    def chkBtnClicked(self):
        items = self.filelist.selectedItems()
        for item in items:
            target = item.text()
            print("\n검사하려는 파일 :", target)
            self.result_massage += Detector.ruleMatchFile(target)

        messagebox.showwarning("Warning!", self.result_massage)
        self.filelist.clearSelection()
