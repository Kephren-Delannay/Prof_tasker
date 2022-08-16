from PyQt5 import QtCore,QtGui, QtWidgets
import New_take

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.Subject_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Subject_comboBox.setObjectName("Subject_comboBox")

        for subject in New_take.SUBJECTS:
            self.Subject_comboBox.addItem(subject)
        self.Subject_comboBox.activated.connect(lambda : self.populate_table(self.Subject_comboBox.currentText()))


        self.verticalLayout_2.addWidget(self.Subject_comboBox)

        self.Save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Save_pushButton.setObjectName("Save_pushButton")
        self.Save_pushButton.clicked.connect(self.save)
        self.verticalLayout_2.addWidget(self.Save_pushButton)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        self.tableWidget.itemChanged.connect(self.update_values)

        self.horizontalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

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

        self.populate_table(self.Subject_comboBox.currentText())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Save_pushButton.setText(_translate("MainWindow", "Save"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Total"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("MainWindow", "Total"))

    def populate_table(self, subject):

        for i in range(2, self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        for i in range(1, self.tableWidget.columnCount()):
            self.tableWidget.removeColumn(i)

        serie = New_take.SUBJECTS_DF[subject].where(New_take.SUBJECTS_DF[subject] > 0.0).dropna()
        num_of_col = serie.size

        self.tableWidget.setColumnCount(num_of_col)
        for i in range(num_of_col):
            classe = serie.keys()[i]
            value = New_take.ASSIGNMENTS[classe].loc[subject].sum()

            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(classe))
            self.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(serie.iloc[i] - value)))
            self.tableWidget.item(0, i).setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.item(0, i).setBackground(QtGui.QColor(249, 96, 135))


        profs = New_take.PROFS_DF.where(New_take.PROFS_DF['Subject'] == subject).dropna()
        num_of_rows = 1 + len(list(profs.index))
        self.tableWidget.setRowCount(num_of_rows)
        for i in range(len(list(profs.index))):
            self.tableWidget.setVerticalHeaderItem(i+1, QtWidgets.QTableWidgetItem(list(profs.index)[i]))

        for i in range(num_of_col):
            for j in range(1, num_of_rows):
                classe = self.tableWidget.horizontalHeaderItem(i).text()
                value = New_take.ASSIGNMENTS.loc[(subject, list(profs.index)[j-1])].loc[classe]
                self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(value)))

    def update_values(self):
        item = self.tableWidget.currentItem()
        if item:
            try:
                prof = self.tableWidget.verticalHeaderItem(item.row()).text()

                value = float(item.text())
                classe = self.tableWidget.horizontalHeaderItem(item.column()).text()
                subject = self.Subject_comboBox.currentText()
                total = New_take.SUBJECTS_DF[subject][classe]
                s = []
                for i in range(1, self.tableWidget.rowCount()):
                    s.append(float(self.tableWidget.item(i, item.column()).text()))
                new_val = float("{:.2f}".format(total - sum(s)))

                self.tableWidget.item(0, item.column()).setText(str(new_val))

            except ValueError:
                print('error')
                value = 0.0
            finally:
                item.setText(str(value))
                New_take.set_hour(prof, value)
                print(New_take.PROFS_DF.loc[prof])

    def save(self):
        subject = self.Subject_comboBox.currentText()

        for i in range(1, self.tableWidget.rowCount()):
            prof = self.tableWidget.verticalHeaderItem(i).text()
            total = 0
            for j in range(self.tableWidget.columnCount()):
                classe = self.tableWidget.horizontalHeaderItem(j).text()
                value = float(self.tableWidget.item(i, j).text())
                New_take.ASSIGNMENTS.loc[(subject, prof)][classe] = value
                total += value
            New_take.set_hour(prof, total)


        try:
            New_take.save_to_csv(New_take.ASSIGNMENTS, 'Data/Assignments_out.csv')
            New_take.save_to_csv(New_take.PROFS_DF, 'Data/Profs_df_out.csv')
            print('data was saved')
        except Exception:
            print('something went wrong')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
