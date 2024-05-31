import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Create a QPushButton
        self.button = QPushButton("Click Me", self)
        
        # Set the initial button's color using style sheets
        self.button.setStyleSheet(
            """
            QPushButton {
                background-color: #3498db;  /* Initial button background color */
                color: white;  /* Text color */
                border-radius: 10px;  /* Rounded corners */
                padding: 10px;  /* Padding */
            }
            """
        )

        # Create a QLabel
        self.label = QLabel("did u clicked?", self)
        self.label.setVisible(False)  # Initially hidden

        # Connect the button's clicked signal to the toggleFeatures method
        self.button.clicked.connect(self.toggleFeatures)

        # Add the label and button to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # Set the layout for the main window
        self.setLayout(self.layout)

        # Set window properties
        self.setWindowTitle("PyQt6 Button Color and Label Example")
        self.setGeometry(100, 100, 300, 200)

        # Variable to track the toggle state
        self.isClicked = False

    def toggleFeatures(self):
        if self.isClicked:
            # Change the button's color and hide the label
            self.button.setStyleSheet(
                """
                QPushButton {
                    background-color: #3498db;  /* Initial button background color */
                    color: white;  /* Text color */
                    border-radius: 10px;  /* Rounded corners */
                    padding: 10px;  /* Padding */
                }
                """
            )
            self.label.setVisible(False)
        else:
            # Change the button's color and show the label
            self.button.setStyleSheet(
                """
                QPushButton {
                    background-color: #1abc9c;  /* New button background color */
                    color: white;  /* Text color */
                    border-radius: 10px;  /* Rounded corners */
                    padding: 10px;  /* Padding */
                }
                """
            )
            self.label.setVisible(True)

        # Toggle the state
        self.isClicked = not self.isClicked

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

