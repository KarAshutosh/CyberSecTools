#!/user/bin/env python3

# code a web browser in python using pyqt5 with:
# 1) buttons to go forwards, backwards and reload 
# 2) a bar to the side with enable and disable cookies option also showing all cookies, disabled by default
# 3) a button to press to enable or disable download permissions, disabled by default
# 4) a button to press to enable or disable JavaScript, disabled by default
# 5) a button to press to enable or disable tor, disabled by default
# 6) buttons to enable or disable all other permissions, disabled by default

import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtWebEngineWidgets import QWebEngineProfile, QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Web Browser')

        # Create the web view
        self.view = QWebEngineView(self)
        self.view.setUrl(QUrl('https://www.example.com'))
        self.setCentralWidget(self.view)

        # Create the navigate button
        self.navigate_button = QPushButton('Go', self)
        self.navigate_button.clicked.connect(self.navigate)
        self.navigate_button.resize(self.navigate_button.sizeHint())
        self.navigate_button.move(10, 10)

        # Create the controls widget and layout
        self.controls_widget = QWidget(self)
        self.controls_layout = QVBoxLayout(self.controls_widget)
        self.controls_widget.setLayout(self.controls_layout)
        self.controls_widget.setFixedWidth(200)

        # Create the cookies label and check box
        self.cookies_label = QLabel('Cookies:', self.controls_widget)
        self.cookies_check_box = QCheckBox(self.controls_widget)
        self.cookies_check_box.setChecked(True)
        self.cookies_check_box.stateChanged.connect(self.toggle_cookies)
        self.cookies_layout = QHBoxLayout()
        self.cookies_layout.addWidget(self.cookies_label)
        self.cookies_layout.addWidget(self.cookies_check_box)
        self.controls_layout.addLayout(self.cookies_layout)

        # Create the download permissions label and check box
        self.download_permissions_label = QLabel('Download permissions:', self.controls_widget)
        self.download_permissions_check_box = QCheckBox(self.controls_widget)
        self.download_permissions_check_box.setChecked(True)
        self.download_permissions_check_box.stateChanged.connect(self.toggle_download_permissions)
        self.download_permissions_layout = QHBoxLayout()
        self.download_permissions_layout.addWidget(self.download_permissions_label)
        self.download_permissions_layout.addWidget(self.download_permissions_check_box)
        self.controls_layout.addLayout(self.download_permissions_layout)

        # Create the JavaScript label and check box
        self.javascript_label = QLabel('JavaScript:', self.controls_widget)
        self.javascript_check_box = QCheckBox(self.controls_widget)
        self.javascript_check_box.setChecked(True)
        self.javascript_check_box.stateChanged.connect(self.toggle_javascript)
        self.javascript_layout = QHBoxLayout()
        self.javascript_layout.addWidget(self.javascript_label)
        self.javascript_layout.addWidget(self.javascript_check_box)
        self.controls_layout.addLayout(self.javascript_layout)

        # Create the Tor label and check box
        self.tor_label = QLabel('Tor:', self.controls_widget)
        self.tor_check_box = QCheckBox(self.controls_widget)
        self.tor_check_box.stateChanged.connect(self.toggle_tor)
        self.tor_layout = QHBoxLayout()
        self.tor_layout.addWidget(self.tor_label)
        self.tor_layout.addWidget(self.tor_check_box)
        self.controls_layout.addLayout(self.tor_layout)

        # Create the all permissions label and check box
        self.all_permissions_label = QLabel('All permissions:', self.controls_widget)
        self.all_permissions_check_box = QCheckBox(self.controls_widget)
        self.all_permissions_check_box.setChecked(True)
        self.all_permissions_check_box.stateChanged.connect(self.toggle_all_permissions)
        self.all_permissions_layout = QHBoxLayout()
        self.all_permissions_layout.addWidget(self.all_permissions_label)
        self.all_permissions_layout.addWidget(self.all_permissions_check_box)
        self.controls_layout.addLayout(self.all_permissions_layout)

        # Set the controls widget to the right of the web view
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.view)
        self.splitter.addWidget(self.controls_widget)
        self.setCentralWidget(self.splitter)

    def navigate(self):
        # Load a web page
        self.view.setUrl(QUrl('https://www.example.com'))

    def toggle_cookies(self, state):
        # Enable or disable cookies
        if state == Qt.Checked:
            self.view.page().profile().setPersistentCookiesPolicy(QWebEngineProfile.AllowPersistentCookies)
        else:
            self.view.page().profile().setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)

    def toggle_download_permissions(self, state):
        # Enable or disable download permissions
        if state == Qt.Checked:
            self.view.page().profile().setPermissionRequestHandler(self.download_permission_handler)
        else:
            self.view.page().profile().setPermissionRequestHandler(None)

    def toggle_javascript(self, state):
        # Enable or disable JavaScript
            if state == Qt.Checked:
            self.view.page().settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        else:
            self.view.page().settings().setAttribute(QWebEngineSettings.JavascriptEnabled, False)

    def toggle_tor(self, state):
        # Enable or disable the use of Tor
        if state == Qt.Checked:
            # TODO: Set the appropriate proxy settings to use Tor
            pass
        else:
            # TODO: Reset the proxy settings to the default
            pass

    def toggle_all_permissions(self, state):
        # Enable or disable all permissions
        if state == Qt.Checked:
            self.cookies_check_box.setChecked(True)
            self.download_permissions_check_box.setChecked(True)
            self.javascript_check_box.setChecked(True)
            # TODO: Enable all other permissions as needed
        else:
            self.cookies_check_box.setChecked(False)
            self.download_permissions_check_box.setChecked(False)
            self.javascript_check_box.setChecked(False)
            # TODO: Disable all other permissions as needed

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())



