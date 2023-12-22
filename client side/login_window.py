from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from settings_window import SettingsWindow
import webbrowser
import requests
import json


class LoginWindow(QMainWindow):
    def __init__(self): #constructor, this will be called when the mainwindow object is created in main.py file
        super(LoginWindow, self).__init__() #first window that should open is the login window
        loadUi('UI/login_window.ui', self)
    #in login file we have login and register button

        self.register_button.clicked.connect(self.go_to_register_page)
        self.login_button.clicked.connect(self.login)

        self.popup = QMessageBox()
        self.popup.setWindowTitle("Failed")

        #with this code we connect clicks with the methods gotoregisterpage and opensettingswindow

        self.show() #show function login window will be displayed

    def go_to_register_page(self):
        webbrowser.open('http://127.0.0.1:8000/register/')

    def login(self):
            try:
                url = 'http://127.0.0.1:8000/api/get_auth_token/'
                response = requests.post(url, data={'username': self.username_input.text(),'password': self.password_input.text()})
                json_response = json.loads(response.text)

			    # HTTP 200
                if response.ok:
				    # Open settings window 
                    self.open_settings_window(json_response['token'])
			        # Bad response
                else:
				    # Show error
                    self.popup.setText("Username or Password is not correct")
                    self.popup.exec_()
            except:
			# Unable to access server
               self.popup.setText("Unable to access server")
               self.popup.exec_()

    def open_settings_window(self, token):
        #settings window object to open settings window after the login page
        self.settings_window=SettingsWindow(token) #this will create a settings window object therefore the constructor will be called automatically
        self.settings_window.displayInfo() #display the window
        self.close() #closes the login window

       


