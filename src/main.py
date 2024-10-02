import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit, QToolBar, QTabWidget, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from util import fetch_url

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python Web Browser')
        self.setGeometry(100, 100, 1024, 768)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.setCentralWidget(self.tabs)
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.address_bar = QLineEdit(self)
        back_button = QPushButton(QIcon('back_icon.png'), '', self)
        forward_button = QPushButton(QIcon('forward_icon.png'), '', self)
        refresh_button = QPushButton(QIcon('refresh_icon.png'), '', self)
        home_button = QPushButton(QIcon('home_icon.png'), '', self)
        new_tab_button = QPushButton(QIcon('new_tab_icon.png'), '', self)

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

    def add_tab(self):
        new_browser = QWebEngineView()
        new_browser.setUrl(QUrl('https://www.google.com'))

        tab_index = self.tabs.addTab(new_browser, 'New Tab')
        self.tabs.setCurrentIndex(tab_index)
        new_browser.urlChanged.connect(lambda url: self.update_address_bar(url, new_browser))

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
