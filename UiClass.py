


from PyQt5 import QtCore, QtGui, QtWidgets

import time
class Ui_MainWindow(object):

    def changetext(self,text):
        self.querytextfield.setText(text)   


    def scrolled(self, value):
        scrollBar.setSliderPosition(value)

    def add_label(self,label,text):
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit.insertPlainText(text)
        strl=len(text)
        if strl > 27:
            if (strl/27)%1==0:
                strl=strl-1
            strl=(int(strl/27)+1)*35
            self.plainTextEdit.setMinimumSize(QtCore.QSize(270,strl))
            self.plainTextEdit.setMaximumSize(QtCore.QSize(270,strl))
        else:
            strl=int(strl*11.5)
            self.plainTextEdit.setMinimumSize(QtCore.QSize(strl,50))
            self.plainTextEdit.setMaximumSize(QtCore.QSize(strl,50))
        if label=="user":
            self.plainTextEdit.setStyleSheet("background-color:#07adf8;\n"
    "border-radius:7px;\n"
    "padding:5px;\n"
    "color:white;\n")
            self.verticalLayout.addWidget(self.plainTextEdit,alignment=QtCore.Qt.AlignRight)
        else:
            self.plainTextEdit.setStyleSheet("background-color:#296dcc;\n"
    "border-radius:7px;\n"
    "padding:5px;\n"
    "color:white;\n")
            self.verticalLayout.addWidget(self.plainTextEdit)

    


#ui starts here
    def setupUi(self, MainWindow):
        #mainwindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(385, 495)
        MainWindow.setMinimumSize(QtCore.QSize(385, 495))
        MainWindow.setMaximumSize(QtCore.QSize(385, 495))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet(
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"

"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 2px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 2px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"

"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"

"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(C:/Users/shoaibshahid/Downloads/FYP/images/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(C:/Users/shoaibshahid/Downloads/FYP/images/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(C:/Users/shoaibshahid/Downloads/FYP/images/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(C:/Users/shoaibshahid/Downloads/FYP/images/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"

"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        #button
        self.microbutton = QtWidgets.QPushButton(self.centralwidget)
        self.microbutton.setGeometry(QtCore.QRect(330, 410, 41, 41))
        self.microbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.microbutton.setStyleSheet("QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    outline: none; \n"
"}\n"

"\n"
"QPushButton:hover {\n"
"    border: 4px solid #78879b;\n"
"    color: silver;\n"
"    background-color:#296dcc;\n"
"}")
        self.microbutton.setText("")
        self.microbutton.setIcon(icon)
        self.microbutton.setIconSize(QtCore.QSize(50, 50))
        self.microbutton.setShortcut("")
        self.microbutton.setObjectName("microbutton")


        #textfield
        self.querytextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.querytextfield.setGeometry(QtCore.QRect(10, 410, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.querytextfield.setFont(font)
        self.querytextfield.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.querytextfield.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    border: 3px solid white;    \n"
"    border-radius: 4px;\n"
"}")
        self.querytextfield.setInputMask("")
        self.querytextfield.setText("")
        self.querytextfield.setMaxLength(32767)
        self.querytextfield.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.querytextfield.setClearButtonEnabled(True)
        self.querytextfield.setObjectName("querytextfield")


        #scrollview
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 385, 401))
        self.scrollArea.setMinimumSize(QtCore.QSize(385, 401))
        self.scrollArea.setMaximumSize(QtCore.QSize(385, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setObjectName("scrollArea")
        global scrollBar
        scrollBar = self.scrollArea.verticalScrollBar()
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 385, 401))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #vlayout
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 385, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.addStretch(1)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)


        #menubar
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 385, 35))
        self.menuBar.setObjectName("menuBar")
        self.menuLanguage = QtWidgets.QMenu(self.menuBar)
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionUrdu = QtWidgets.QAction(MainWindow)
        self.actionUrdu.setObjectName("actionUrdu")
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionUrdu)
        self.menuBar.addAction(self.menuLanguage.menuAction())

        self.retranslateUi(MainWindow)
        scrollBar.valueChanged.connect(lambda value: self.scrolled(value))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gouti: A Voice Assistant"))
        self.microbutton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Talk to Gouti</p></body></html>"))
        self.querytextfield.setPlaceholderText(_translate("MainWindow", "Type Your Query Here"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionUrdu.setText(_translate("MainWindow", "Urdu"))
    



