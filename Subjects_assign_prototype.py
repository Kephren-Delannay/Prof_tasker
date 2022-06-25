
from PyQt5 import QtCore, QtWidgets
import New_take

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # region table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(len(New_take.SUBJECTS))

        self.init_table()

        self.verticalLayout.addWidget(self.tableWidget)

        # endregion

        self.multiline_edit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.multiline_edit_pushButton.setObjectName("multiline_edit_pushButton")
        self.multiline_edit_pushButton.clicked.connect(self.multi_edit)
        self.verticalLayout.addWidget(self.multiline_edit_pushButton)

        # region save button

        self.Save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Save_pushButton.setObjectName("Save_pushButton")
        self.Save_pushButton.clicked.connect(self.save_button)
        self.verticalLayout.addWidget(self.Save_pushButton)

        # endregion

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Save_pushButton.setText(_translate("MainWindow", "Save"))
        self.multiline_edit_pushButton.setText(_translate("MainWindow", "Edit"))

    def init_table(self):
        for i in range(len(New_take.SUBJECTS)):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(New_take.SUBJECTS[i]))
        self.tableWidget.setRowCount(len(New_take.CLASSES))
        for i in range(len(New_take.CLASSES)):
            self.tableWidget.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem(New_take.CLASSES[i]))

        for i in range(len(New_take.CLASSES)):
            for j in range(len(New_take.SUBJECTS)):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str((New_take.SUBJECTS_DF.iloc[i, j]))))

    def save_button(self):
        for i in range(len(New_take.CLASSES)):
            for j in range(len(New_take.SUBJECTS)):
                New_take.SUBJECTS_DF.iloc[i, j] = eval(self.tableWidget.item(i, j).text())
        New_take.save_to_csv(New_take.SUBJECTS_DF, 'Data/Subjects_df_out.csv')
        msg = QtWidgets.QMessageBox()
        msg.information(self.centralwidget, "Saved data", "Your data has been successfully saved")

    def multi_edit(self):
        value, ok = QtWidgets.QInputDialog().getDouble(self.centralwidget, "Edit hours", "Value", 0, 0, 100, 2)

        if ok and value:
            for item in self.tableWidget.selectedItems():
                item.setText(str(value))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
