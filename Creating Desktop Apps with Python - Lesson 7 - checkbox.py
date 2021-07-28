import sys
from PyQt5 import QtWidgets
from checkbox import Ui_MainWindow

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cinema.stateChanged.connect(self.show_state)
        self.ui.reading.stateChanged.connect(self.show_state)
        self.ui.running.stateChanged.connect(self.show_state)
        self.ui.doctor.stateChanged.connect(self.show_state)
        self.ui.teacher.stateChanged.connect(self.show_state)
        self.ui.barber.stateChanged.connect(self.show_state)
        self.ui.get_hobby.clicked.connect(self.get_hobby)
        self.ui.get_job.clicked.connect(self.get_job)

    def get_job(self):
        result_text = ''
        items_job = self.ui.group_job.findChildren(QtWidgets.QCheckBox)
        for item_job in items_job:
            if item_job.isChecked():
                result_text += item_job.text() + '\n'
        self.ui.label_job.setText(result_text)
    def get_hobby(self):
        result_text = ''
        items_hobby = self.ui.group_hobby.findChildren(QtWidgets.QCheckBox)
        for item_hobby in items_hobby:
            if item_hobby.isChecked():
                result_text += item_hobby.text() + '\n'
        self.ui.label_hobby.setText(result_text)

    def show_state(self,value):
        cb = self.sender()
        if cb.isChecked():
            print(cb.text())


def app_create():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app_create()











































