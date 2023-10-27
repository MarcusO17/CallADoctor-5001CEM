import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QSplitter, \
    QStackedWidget


class CustomTabbedApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Tabbed Application")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget to hold the content pages
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()

        # Create a QSplitter to divide the space
        splitter = QSplitter()

        # Create a stacked widget to hold content pages
        self.stacked_widget = QStackedWidget()

        # Create a sidebar for tab buttons
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()

        button_page1 = QPushButton("Page 1")
        button_page2 = QPushButton("Page 2")

        button_page1.clicked.connect(self.show_page1)
        button_page2.clicked.connect(self.show_page2)

        sidebar_layout.addWidget(button_page1)
        sidebar_layout.addWidget(button_page2)

        sidebar.setLayout(sidebar_layout)

        splitter.addWidget(sidebar)
        splitter.addWidget(self.stacked_widget)
        splitter.setSizes([self.width() * 0.1, self.width() * 0.9])

        layout.addWidget(splitter)

        central_widget.setLayout(layout)

        self.current_page = None

    def show_page1(self):
        if self.current_page is not None:
            self.current_page.hide()
            self.current_page = None

        page1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel("This is Page 1")
        layout1.addWidget(label1)
        page1.setLayout(layout1)

        self.stacked_widget.addWidget(page1)
        self.stacked_widget.setCurrentWidget(page1)

        self.current_page = page1

    def show_page2(self):
        if self.current_page is not None:
            self.current_page.hide()
            self.current_page = None

        page2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel("This is Page 2")
        layout2.addWidget(label2)
        page2.setLayout(layout2)

        self.stacked_widget.addWidget(page2)
        self.stacked_widget.setCurrentWidget(page2)

        self.current_page = page2


def main():
    app = QApplication(sys.argv)
    window = CustomTabbedApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()