from PyQt5.QtWidgets import QApplication
import sys
from login_window import LoginWindow

app=QApplication(sys.argv) #Qapplication function uses argv to det. which operating system the app will run on
mainwindow = LoginWindow()

try:
    sys.exit(app.exec_())
except:
    print("exiting") #makes sure that while exiting if some functionality is still open it would not cause any error
#it will print exiting and wait for any background processes to close