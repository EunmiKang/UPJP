
from PyQt5.QtWidgets import *

from signature.generator import *
from signature.detector import Detector


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self._init_ui()

    def _init_ui(self):
        self._init_widget()

        self.setCentralWidget(self.table_widget)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('UPJP')
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

        self.tabs.addTab(self.tab1, "홈")
        self.tabs.addTab(self.tab2, "환경설정")

    def tab1ui(self):
        layout_tab1 = QFormLayout()
        layout_btn = QFormLayout()

        filelist = QListWidget()
        filelist.setWindowTitle('Example List')
        filelist.setSelectionMode(QAbstractItemView.MultiSelection)

        filelist.setFixedSize(500, 300)

        addBtn = QPushButton("추가", self)
        deleteBtn = QPushButton("삭제", self)
        checkBtn = QPushButton("검사", self)

        addBtn.setFixedSize(100, 30)
        deleteBtn.setFixedSize(100, 30)
        checkBtn.setFixedSize(100, 30)

        addBtn.clicked.connect(lambda: self.addBtnClicked(filelist))
        deleteBtn.clicked.connect(lambda: self.deleteBtnClicked(filelist))
        checkBtn.clicked.connect(lambda: self.chkBtnClicked(filelist))

        layout_btn.addRow(addBtn)
        layout_btn.addRow(deleteBtn)
        layout_btn.addRow(checkBtn)
        layout_tab1.addRow(filelist, layout_btn)

        self.tab1.setLayout(layout_tab1)

    def tab2ui(self):
        layout_tab2 = QFormLayout()
        layout_btn = QFormLayout()

        filedir = QTextEdit()
        filedir.setReadOnly(True)

        filedir.setFixedSize(500, 30)

        filelist = QListWidget()
        filelist.setWindowTitle('Example List')
        filelist.setSelectionMode(QAbstractItemView.MultiSelection)

        filelist.setFixedSize(500, 280)

        addBtn = QPushButton("추가", self)
        addToWhiteBtn = QPushButton("생성", self)

        addBtn.setFixedSize(100, 30)
        addToWhiteBtn.setFixedSize(100, 30)

        addBtn.clicked.connect(lambda: self.addWithDirectoryBtnClicked(filedir, filelist))
        addToWhiteBtn.clicked.connect(lambda: self.createWhiteBtnClicked(filedir))

        layout_btn.addRow(addToWhiteBtn)
        layout_tab2.addRow(filedir, addBtn)
        layout_tab2.addRow(filelist, layout_btn)

        self.tab2.setLayout(layout_tab2)

    def addBtnClicked(self, filelist):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        items, _ = QFileDialog.getOpenFileNames(self, "Select file", "~/",
                                                "All Files (*);;Python Files (*.py)", options=options)
        for item in items:
            print("* add file :", item)
            filelist.addItem(item)

    def deleteBtnClicked(self, filelist):
        items = filelist.selectedItems()
        for item in items:
            filelist.removeItemWidget(item)
            filelist.takeItem(filelist.row(item))

    def chkBtnClicked(self, filelist):
        items = filelist.selectedItems()
        for item in items:
            target = item.text()
            print("\n검사하려는 파일 :", target)
            Detector.ruleMatchFile(target)

        filelist.clearSelection()

    def addWithDirectoryBtnClicked(self, filedir, filelist):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dir = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)

        filedir.setText(dir)
        filelist.clear()
        filelist.addItems(getFileList(dir))


    def createWhiteBtnClicked(self, filedir):

        Generater.extractStringsWithDB(Generater(), filedir.toPlainText())



