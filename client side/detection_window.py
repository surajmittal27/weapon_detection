from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from detection import Detection

class DetectionWindow(QMainWindow):
    def __init__(self): #this will be called once class object is created from settings window class
        super(DetectionWindow, self).__init__()
        loadUi('UI/detection_window.ui', self)
        #mapping the button
        self.stop_detection_button.clicked.connect(self.close) #when button is clicked the close function is called that is already present in qmainwindow which is super class therefore the close function need not be created

    def create_detection_instance(self, token, location, receiver):
        #here we create the detection class object
        self.detection= Detection(token, location, receiver)

    @pyqtSlot(QImage) #decorator allow to add functionality to function, pyqtslot decorator allows to map the camera's output to label
    def setImage(self, image):
        self.label_detection.setPixmap(QPixmap.fromImage(image))
        #setPixmap function will load the image from the camera to the label, QPixmap.fromImage(image) will handle the image received from the detection class

    #method for starting the detection
    def start_detection(self):
        self.detection.changePixmap.connect(self.setImage)
        self.detection.start()
        self.show()

    #when we close the detection window, when we close the window we will start the detection algo
    def closeEvent(self, event):
        #this method is triggered when the application is closing
        self.detection.running=False
        event.accept()
