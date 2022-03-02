from PyQt5.QtGui import QIcon,QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,QPrintPreviewDialog
from PyQt5.uic import loadUiType
import sys
import MySQLdb as mdb

FORM_CLASS,_ = loadUiType('main.ui')
class window(QMainWindow, FORM_CLASS):
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        self.ui_changes()
        self.controllers()

    def ui_changes(self):
        ###in the beginning
        self.menubar.setEnabled(False)
        self.menubar.setStyleSheet('''background-color:black;''')
        self.textEdit = QTextEdit()
        self.textEdit.setVisible(False)

    def controllers(self):
        self.pushButton.clicked.connect(self.login)
        self.pushButton_7.clicked.connect(self.addstudent)
        self.pushButton_4.clicked.connect(self.get_data)
        self.pushButton_5.clicked.connect(self.edit_student)
        self.pushButton_6.clicked.connect(self.delete_student)

        ###menubar:
        self.menubar.triggered[QAction].connect(self.menubar_fun)

        ### print receipt
        self.pushButton_33.clicked.connect(self.Btn_Print_Click)

##################################################{menubar actions}#####################################################
    def addstudent(self):
        ## fetch data from input lineEdits or combobox
        Registration_number = self.lineEdit_3.text()
        Full_name = self.lineEdit_4.text()
        Gender = self.comboBox_2.currentText()
        Date_of_Birth = self.lineEdit_6.text()
        Age = self.lineEdit_7.text()
        Address = self.lineEdit_9.text()
        Phone = self.lineEdit_8.text()
        Email = self.lineEdit_10.text()
        Stage = self.comboBox.currentText()

        ## add fetched data to database
        db = mdb.connect(host = 'localhost', user = 'root', password = '', db = 'school')
        cr = db.cursor()
        cr.execute('''INSERT INTO student(registration_number, full_name, gender, date_of_birth, age, address, phone, email, stage) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(Registration_number, Full_name, Gender, Date_of_Birth, Age, Address, Phone, Email, Stage))
        db.commit()
        db.close()

        ## clear_linEdits
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.comboBox_2.setCurrentText('')
        self.lineEdit_6.setText('Male')
        self.lineEdit_7.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_8.setText('')
        Email = self.lineEdit_10.setText('')
        Stage = self.comboBox.currentText('1st year')
##################################################{menubar actions}#####################################################
    def get_data(self):
        ## fetch data from input lineEdits or combobox
        Registration_number = self.lineEdit_15.text()
        list_1 = []
        ## add fetched data to database
        db = mdb.connect(host='localhost', user='root', password='', db='school')
        cr = db.cursor()
        cr.execute('''SELECT * FROM student WHERE Registration_number='{}' '''.format(Registration_number))
        a = cr.fetchall()
        for n in a[0]:
            list_1.append(n)
        db.commit()
        db.close()

        ##dstplay data in LineEdits
        self.lineEdit_5.setText(list_1[1])
        self.comboBox_3.setCurrentText(list_1[2])
        self.lineEdit_13.setText(list_1[3])
        self.lineEdit_16.setText(list_1[4])
        self.lineEdit_11.setText(list_1[5])
        self.lineEdit_12.setText(list_1[6])
        self.lineEdit_14.setText(list_1[7])
        self.comboBox_4.setCurrentText(list_1[8])

##################################################{menubar actions}#####################################################
    def edit_student(self):
        ## fetch data from input lineEdits or combobox
        Registration_number = self.lineEdit_15.text()
        Full_name = self.lineEdit_5.text()
        Gender = self.comboBox_3.currentText()
        Date_of_Birth = self.lineEdit_13.text()
        Age = self.lineEdit_16.text()
        Address = self.lineEdit_11.text()
        Phone = self.lineEdit_12.text()
        Email = self.lineEdit_14.text()
        Stage = self.comboBox_4.currentText()
        ## add fetched data to database
        db = mdb.connect(host='localhost', user='root', password='', db='school')
        cr = db.cursor()
        cr.execute('''UPDATE student SET full_name='{}', gender='{}', date_of_birth='{}', age='{}', address='{}', phone='{}',email='{}',stage='{}' WHERE registration_number='{}' '''
                   .format(Full_name, Gender, Date_of_Birth, Age, Address, Phone, Email, Stage, Registration_number))
        db.commit()
        db.close()

        ## clear LinEdits
        self.lineEdit_15.setText('')
        self.lineEdit_5.setText('')
        self.comboBox_3.setCurrentText('Male')
        self.lineEdit_13.setText('')
        self.lineEdit_16.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_14.setText('')
        self.comboBox_4.setCurrentText('1st year')

##################################################{menubar actions}#####################################################

##################################################{menubar actions}#####################################################
    def delete_student(self):
        ## fetch data from input lineEdits or combobox
        Registration_number = self.lineEdit_15.text()
        ## add fetched data to database
        db = mdb.connect(host='localhost', user='root', password='', db='school')
        cr = db.cursor()
        cr.execute(
            '''DELETE FROM student WHERE registration_number='{}' '''.format(Registration_number))
        db.commit()
        db.close()

        ## clear LinEdits
        self.lineEdit_15.setText('')
        self.lineEdit_5.setText('')
        self.comboBox_3.setCurrentText('Male')
        self.lineEdit_13.setText('')
        self.lineEdit_16.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_14.setText('')
        self.comboBox_4.setCurrentText('1st year')
##################################################{menubar actions}#####################################################
    def menubar_fun(self, q):
        print(q.text())
        ##students_menu
        if q.text()== 'Add Student':
            self.tabWidget.setCurrentIndex(0)
        if q.text() == 'Edit_Delete students':
            self.tabWidget.setCurrentIndex(1)

        ## marks_menu
        if q.text() == 'Add_Add_Edit_Delete marks':
            self.tabWidget.setCurrentIndex(2)

        ## attendance_menu
        if q.text() == 'Add_Edit_Delete attendance':
            self.tabWidget.setCurrentIndex(3)

        ## fees_menu
        if q.text() == 'Add_Edit_Delete fee':
            self.tabWidget.setCurrentIndex(4)

        ## reports_menu
        if q.text() == 'Student reports':
            self.tabWidget.setCurrentIndex(5)
        if q.text() == 'Marks reports':
            self.tabWidget.setCurrentIndex(5)
        if q.text() == 'Attendance reports':
            self.tabWidget.setCurrentIndex(5)
        if q.text() == 'Fee reports':
            self.tabWidget.setCurrentIndex(5)

        ## actionPrint
        if q.text()== 'Print':
            self.tabWidget.setCurrentIndex(6)

##############################################{login}#########################################################
    def login(self):
        self.name = self.lineEdit.text()
        self.password = self.lineEdit_2.text()

        if self.name=='admin' and self.password=='admin':
            self.menubar.setEnabled(True)
            self.menubar.setStyleSheet('''QMenuBar{background-color:rgb(255,0,255);color:black;font: 13pt "MS Shell Dlg 2";}''')
            self.stackedWidget.setCurrentIndex(1)
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle('Authentification Message')
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText('make sure you enter correct Username and Password')
            msg.exec_()
########################################################################################################
    def Btn_Print_Click(self):
        # Print options
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Portrait)
        printer.setPaperSize(QPrinter.A4)
        printer.setPageSize(QPrinter.A4)
        printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)
        printer.setFullPage(True)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("testfile.pdf")

        # Render/Paint it
        painter = QPainter()
        painter.begin(printer)

        # Establish scaling transform
        scaleX = printer.pageRect().width() / self.groupBox_13.rect().width()
        scaleY = printer.pageRect().height() / self.groupBox_13.rect().height()
        useScale = min(scaleX, scaleY)
        painter.scale(useScale, useScale)

        self.groupBox_13.render(painter)
        painter.end()
########################################################################################################
app = QApplication(sys.argv)
window = window()
window.show()
app.exec_()
