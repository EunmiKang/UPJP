
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from UPJP.signature.generator import Gen


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self._init_ui()
        self.gen = Gen()

    def _init_ui(self):
        self._init_widget()

        self.setCentralWidget(self.table_widget)

        self.setGeometry(300, 300, 600, 400)
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

        self.filelist = QListWidget()
        self.filelist.setWindowTitle('Example List')
        self.filelist.setSelectionMode(QAbstractItemView.MultiSelection)

        btn1 = QPushButton("추가", self)
        btn2 = QPushButton("삭제", self)
        btn3 = QPushButton("검사", self)

        btn1.clicked.connect(self.openFileDialog)
        btn2.clicked.connect(self.subBtnClicked)
        btn3.clicked.connect(self.chkBtnClicked)

        layout_tab1.addRow(self.filelist)
        layout_tab1.addRow(btn1, btn2)
        layout_tab1.addRow(btn3)

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
            print(item)
            self.filelist.addItem(item)

    def subBtnClicked(self):
        items = self.filelist.selectedItems()
        for item in items:
            self.filelist.removeItemWidget(item)
            self.filelist.takeItem(self.filelist.row(item))

    def chkBtnClicked(self):

        for index in range(self.filelist.count()):
            print(self.filelist.item(index).text())

        self.filelist.clearSelection()

    def buttonClicked(self):
        # sender = self.sender()
        # self.statusBar().showMessage(sender.text() + ' was pressed')
        raise NotImplementedError

