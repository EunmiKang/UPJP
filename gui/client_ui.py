
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from signature.generator import Gen
from signature.detector import Detector


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

        addBtn = QPushButton("추가", self)
        deleteBtn = QPushButton("삭제", self)
        checkBtn = QPushButton("검사", self)

        addBtn.clicked.connect(self.openFileDialog)
        deleteBtn.clicked.connect(self.deleteBtnClicked)
        checkBtn.clicked.connect(self.chkBtnClicked)

        layout_tab1.addRow(self.filelist)
        layout_tab1.addRow(addBtn, deleteBtn)
        layout_tab1.addRow(checkBtn)

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
            Detector.ruleMatchFile(target)

        self.filelist.clearSelection()
