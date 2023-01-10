import sys, random, os, subprocess
from sys import platform

try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtNetwork import *
except Exception:
    os.system('pip install PyQt5')
    os.system('pip install PyQtWebEngine')

__author__ = "XNUVERS007"
__version__ = "1.2.0"
__license__ = "MIT"

# Optimization for Windows
if sys.platform == 'win32':
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
elif sys.platform == 'darwin':
    appid = 'mycompany.myproduct.subproduct.version'
    subprocess.call(['defaults', 'write', appid, 'LSUIElement', '-bool', 'true'])
elif sys.platform == 'linux':
    appid = 'mycompany.myproduct.subproduct.version'
    subprocess.call(['xprop', '-f', '_NET_WM_PID', '32c', '-set', '_NET_WM_PID', '$$'])
    subprocess.call(['xprop', '-f', '_NET_WM_NAME', '8s', '-set', '_NET_WM_NAME', appid])
    subprocess.call(['xprop', '-f', '_NET_WM_ICON_NAME', '8s', '-set', '_NET_WM_ICON_NAME', appid])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QTabWidget and a QWebEngineView widget
        self.tabs = QTabWidget(self)
        self.view = QWebEngineView(self)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a web browser create by Python and PyQt5, privacy <b> 100% Secure </b>. This browser is still in development. If you find any bugs, please report them to the My GitHub repository.<br /> <center><font color='red'>© 2023 - 2023 XNUVERS007 - All Rights Reserved. <br />Last Updated : 01/06/2023 02:47:45</font></center>")
        msg.setWindowTitle("Web Browser")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        # Set the QWebEngineView as the central widget of the main window
        self.setCentralWidget(self.tabs)

        # Add the QWebEngineView to a new tab in the QTabWidget
        self.tabs.addTab(self.view, "Tab 1")

        # Set the URL of the QWebEngineView
        self.view.setUrl(QUrl("https://google.com"))

        # Create the "Go back" button
        self.back_button = QPushButton("Go back", self)
        self.back_button.clicked.connect(self.view.back)

        # Create the "Home" button
        self.home_button = QPushButton("Home", self)
        self.home_button.clicked.connect(self.go_home)

        # Create the "Refresh" button
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.view.reload)

        # Create the "New tab" button
        self.new_tab_button = QPushButton("New tab", self)
        self.new_tab_button.clicked.connect(self.add_new_tab)

        # Create the "Calendar" button
        self.calendar_button = QPushButton("Calendar", self)
        self.calendar_button.clicked.connect(self.show_calendar)

        # self.view.page().triggerAction(QWebEnginePage.InspectElement)
        # Create The "Inspect Element" button
        # self.inspect_element_button = QPushButton("Inspect Element", self)
        # self.inspect_element_button.clicked.connect(self.inspect_element)

        self.notepad_button = QPushButton("Notepad", self)
        self.notepad_button.clicked.connect(self.open_notepad)

        self.changeip_button = QPushButton("Change IP", self)
        self.changeip_button.clicked.connect(self.changeip)

        self.takescreenshot_button = QPushButton("Take Screenshot", self)
        self.takescreenshot_button.clicked.connect(self.takescreenshot)

        # self.paraip = [
        #     "38.49.128.114:999",
        #     "212.129.54.138:3128",
        #     "80.15.19.7:80",
        #     "192.227.194.54:3128",
        #     "31.14.131.201:81",
        #     "196.189.149.115:80"
        # ]

        # self.proxy = QNetworkProxy()
        # self.proxy.setType(QNetworkProxy.HttpProxy)
        # self.current_proxy_index = 0

        self.setWindowTitle("Web Browser")
        self.setGeometry(300, 300, 800, 600)
        self.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.view.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.tabs.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.back_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.home_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.refresh_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.new_tab_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.calendar_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        # self.inspect_element_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.notepad_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.changeip_button.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.setWindowIcon(QIcon('icon.jpg'))

        # Add the buttons to a QToolBar
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)
        self.toolbar.addWidget(self.back_button)
        self.toolbar.addWidget(self.home_button)
        self.toolbar.addWidget(self.refresh_button)
        self.toolbar.addWidget(self.new_tab_button)
        self.toolbar.addWidget(self.calendar_button)
        # self.toolbar.addWidget(self.inspect_element_button)
        self.toolbar.addWidget(self.notepad_button)
        self.toolbar.addWidget(self.changeip_button)
        self.toolbar.addWidget(self.takescreenshot_button)

        # Create Date time and cannot edit and run automatically
        self.date_time = QDateTimeEdit(self)
        self.date_time.setDateTime(QDateTime.currentDateTime())
        self.date_time.setDisplayFormat("dd/MM/yyyy hh:mm:ss")
        self.date_time.setReadOnly(True)
        self.date_time.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.toolbar.addWidget(self.date_time)        

        # Create the URL input line edit
        # auto https://
        self.url_input = QLineEdit(self)
        link = "https://" + self.url_input.text()
        self.url_input.setText(link)
        self.url_input.returnPressed.connect(self.load_url)
        self.url_input.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        self.toolbar.addWidget(self.url_input)

        # Create the status bar
        self.status = QStatusBar(self)
        self.setStatusBar(self.status)

        # Create the progress bar
        self.progress = QProgressBar(self)
        self.progress.setValue(0)

        # Add the progress bar to the status bar
        self.status.addPermanentWidget(self.progress)

        # Connect the QWebEngineView's loadProgress signal to the progress bar's setValue slot
        self.view.loadProgress.connect(self.progress.setValue)

        # Connect the QWebEngineView's loadFinished signal to the progress bar's hide slot
        self.view.loadFinished.connect(self.progress.hide)

        # Connect the QWebEngineView's loadStarted signal to the progress bar's show slot
        self.view.loadStarted.connect(self.progress.show)

        # Connect the QWebEngineView's titleChanged signal to the window's setWindowTitle slot
        self.view.titleChanged.connect(self.setWindowTitle)

        # Connect the QWebEngineView's urlChanged signal to the URL input's setText slot
        # self.view.urlChanged.connect(self.url_input.setText)

        # Connect the QWebEngineView's urlChanged signal to the status bar's showMessage slot
        # self.view.urlChanged.connect(self.status.showMessage)

        # Create the tab widget
        self.tabs = QTabWidget(self)
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.tabs.removeTab)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setStyleSheet('background-color: #2d2d2d; color: #c4c4c4;')
        
        # Add the QWebEngineView to the tab widget
        self.tabs.addTab(self.view, "Tab 1")

        # Set the tab widget as the window's central widget
        self.setCentralWidget(self.tabs)

    def takescreenshot(self):
        """Take screenshot."""
        self.view.loadFinished.connect(self.take_screenshot)
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save As', None, 'PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ')
        if file_path:
            self.view.page().view().grab().save(file_path)

    def take_screenshot(self):
        """Take screenshot."""
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save As', None, 'PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ')
        if file_path:
            self.view.page().view().grab().save(file_path)


    def changeip(self):
        """Change IP."""
        paraip = [
            "38.49.128.114:999",
            "212.129.54.138:3128",
            "80.15.19.7:80",
            "192.227.194.54:3128",
            "31.14.131.201:81",
            "196.189.149.115:80"
        ]
        config = QNetworkConfigurationManager().defaultConfiguration()
        session = QNetworkSession(config)
        if not session.isOpen():
            session.open()
        
        iface = session.interface()
        # QHostAddress get from paraip
        # get list of ip address from paraip
        # ipe = self.paraip[0:5]
        # for i in ipe:
        #     print(i)
        # print(ipe)
        ip_address = random.choice(paraip[0:5])
        if iface.addressEntries():
            iface.addressEntries()[0].setIp(QHostAddress(ip_address))
            print("IP Address Changed to: " + ip_address)
            # Visit browser with new ip
            # self.view.load(QUrl("https://whatismyipaddress.com/"))
            self.view.reload()
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Information)
            msg2.setTextFormat(Qt.RichText)
            # Create Icon
            icon = QIcon()
            icon.addPixmap(QPixmap("icon.jpg"), QIcon.Normal, QIcon.Off)
            msg2.setWindowIcon(icon)
            msg2.setText("IP Address Changed to: " + ip_address)
            msg2.setWindowTitle("IP Address Changed")
            msg2.setStandardButtons(QMessageBox.Ok)
            msg2.exec_()

        else:
            print("No IP Address Found")
            
        # if iface.addressEntries():
        #     iface.addressEntries()[0].setIp(QHostAddress(ip_address))
        #     print("IP Address Changed to: " + ip_address)
        # else:
        #     print("No IP Address Found")

        # global current_proxy_index
        # current_proxy_index = 0
        # self.proxy.setHostName(self.proxies[current_proxy_index] or self.proxies[self.current_proxy_index])
        # QNetworkProxy.setApplicationProxy(self.proxy)
        # current_proxy_index += 1
        # if current_proxy_index >= len(self.proxies):
        #     current_proxy_index = 0

    def load_url(self):
        """Load the URL in the URL input field."""
        url = self.url_input.text()
        if url == '':
            return
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        self.view.load(QUrl(url))

    def open_notepad(self):
        # self.notepad = subprocess.Popen(['notepad.exe'])
        # if windows open notepad, if linux open gedit, if mac open textedit
        if sys.platform == 'win32':
            self.notepad = subprocess.Popen(['notepad.exe'])
        elif sys.platform == 'linux':
            self.notepad = subprocess.Popen(['gedit'])
        elif sys.platform == 'darwin':
            self.notepad = subprocess.Popen(['open', '-a', 'TextEdit'])
        else:
            print('Unsupported OS')
        self.notepad.wait()

    def current_tab_changed(self, i):
        """Change the QWebEngineView when the current tab changes."""
        qwidget = self.tabs.currentWidget()
        self.view = qwidget

    def back(self):
        """Go back to the previous page."""
        self.view.back()

    def refresh(self):
        """Refresh the current page."""
        self.view.reload()

    # def inspect_element(self):
    #     self.view.page().triggerAction(QWebEnginePage.InspectElement)
    
    def go_home(self):
        self.view.setUrl(QUrl("https://google.com"))

    # def load_url(self):
    #     """Load the URL entered in the URL input line edit."""
    #     url = QUrl(self.url_input.text())
    #     if url.scheme() == "":
    #         url.setScheme("http")
    #     self.view.load(url)
        # self.view.load(QUrl(self.url_input.text()))

    def add_new_tab(self):
        # Create a new QWebEngineView
        view = QWebEngineView(self)
        # Add the view to the tab widget
        self.tabs.addTab(view, "Tab {}".format(self.tabs.count() + 1))
        # Load a default URL
        view.load(QUrl('https://www.google.com'))
        # add close tab
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        # self.tab_widget.setTabsClosable(True)
        # self.tab_widget.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index):
        # if there is only one tab, don't close it
        if self.tabs.count() == 1:
            return
        # remove the tab
        self.tabs.removeTab(index)

    def show_calendar(self):
        # subprocess.run(["calender"])
        calendar = QCalendarWidget(self)
        calendar.setMouseTracking(True)
        calendar.setMinimumSize(350, 350)
        calendar.setGridVisible(True)
        calendar.move(20, 20)

        calendar.setMinimumDate(QDate(1900, 1, 1))
        calendar.setMaximumDate(QDate(2100, 12, 31))

        calendar.setSelectedDate(QDate.currentDate())

        close_button = QPushButton("Close", calendar)
        close_button.clicked.connect(calendar.close)

        calendar.setLayout(QVBoxLayout())
        calendar.layout().addWidget(close_button)

        calendar.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    browser = MainWindow()
    browser.show()
    sys.exit(app.exec_())
