import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QToolBar, QTabWidget, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QCursor
from util import fetch_url
from PyQt5.QtWidgets import QTabBar
from PyQt5.QtGui import QFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python Web Browser')
        self.setWindowIcon(QIcon('browser_icon.png'))
        self.setGeometry(100, 100, 1024, 768)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.setCentralWidget(self.tabs)
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.address_bar = QLineEdit(self)
        self.address_bar.setMinimumHeight(35)
        self.address_bar.setStyleSheet("""
            QLineEdit{
                border: 1px solid grey;
                border-radius: 10px;
                padding:  5px;  
                font-family: Verdana; 
                font-size: 9pt; 
                color: grey;
                margin: 5px;
            }
                                       
            QLineEdit::selection {
            background-color: lightgray;  
            color: white;  
        }
        """)



        back_button = self.create_button(QIcon(os.path.join(BASE_DIR, 'back_icon.png')))
        forward_button = self.create_button(QIcon(os.path.join(BASE_DIR, 'forward_icon.png')))
        refresh_button = self.create_button(QIcon(os.path.join(BASE_DIR, 'refresh_icon.png')))
        home_button = self.create_button(QIcon(os.path.join(BASE_DIR, 'home_icon.png')))
        new_tab_button = self.create_button(QIcon(os.path.join(BASE_DIR, 'new_tab_icon.png')))



   
        self.toolbar.addWidget(back_button)
        self.toolbar.addWidget(forward_button)
        self.toolbar.addWidget(refresh_button)
        self.toolbar.addWidget(home_button)
        self.toolbar.addWidget(self.address_bar)
        self.toolbar.addWidget(new_tab_button)


        back_button.clicked.connect(self.back)
        forward_button.clicked.connect(self.forward)
        refresh_button.clicked.connect(self.refresh)
        home_button.clicked.connect(self.go_home)
        new_tab_button.clicked.connect(self.add_tab)
        self.address_bar.returnPressed.connect(self.load_page)

       
        self.add_tab()

    def create_button(self, icon):
        button = QPushButton(icon, '', self)
        button.setFixedSize(30, 30)
        
        button.setStyleSheet("""
            QPushButton {
                border: 1px solid grey;
                border-radius: 10px; 
                background-color: white; 
            }
            QPushButton:hover {
                background-color: lightgray;
            }
            QPushButton:pressed {
                background-color: darkgray; 
            }
        """) 
        
        button.setCursor(QCursor(Qt.PointingHandCursor)) 
        return button
    
    def add_tab(self):
        new_browser = QWebEngineView()
        new_browser.setUrl(QUrl('https://www.google.com'))

        tab_index = self.tabs.addTab(new_browser, 'New Tab')
        self.tabs.tabBar().setStyleSheet("""
            QTabBar::tab {
                margin: 5px;
                padding: 7px 10px;  
                font-size: 9pt;
                font-family: Verdana;
                text-align: left;
                min-width: 100px;  
                min-height: 15px;  
                color: #222;
                border-radius: 10px;
            }
            
            QTabBar::tab:hover {
                background-color: #999; 
            }
                                         
            QTabBar::tab:selected {
            background-color: white;
            border: none;
            border-radius: 13px;  
    }
         """)
        
       
        for i in range(self.tabs.count()):
             tab_widget = self.tabs.widget(i)
             if tab_widget:
                 tab_widget.setMinimumWidth(120)  
        self.tabs.setCurrentIndex(tab_index)
        new_browser.urlChanged.connect(lambda url: self.update_address_bar(url, new_browser))

        close_button = QPushButton("X") 
        close_button.setFixedSize(20, 25)
        close_button.setStyleSheet("border: none; color: grey; font-weight: bold;")

        close_button.clicked.connect(lambda: self.close_tab(tab_index))
        self.tabs.tabBar().setTabButton(tab_index, QTabBar.RightSide, close_button)


    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def load_page(self):
        url = self.address_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        current_browser = self.tabs.currentWidget()
        current_browser.setUrl(QUrl(url))

    def update_address_bar(self, url, browser):
        if browser == self.tabs.currentWidget():
            self.address_bar.setText(url.toString())

    def back(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.back()

    def forward(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.forward()

    def refresh(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.reload()

    def go_home(self):
        current_browser = self.tabs.currentWidget()
        if current_browser:
            current_browser.setUrl(QUrl('https://www.google.com'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
