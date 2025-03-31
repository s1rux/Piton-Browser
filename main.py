import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Piton Browser")
        self.setGeometry(100, 100, 1200, 800)
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Введите URL и нажмите Enter")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        self.back_button = QPushButton("←")
        self.back_button.setFixedWidth(40)
        self.back_button.clicked.connect(self.browser.back)
        
        self.forward_button = QPushButton("→")
        self.forward_button.setFixedWidth(40)
        self.forward_button.clicked.connect(self.browser.forward)
        
        self.reload_button = QPushButton("⟳")
        self.reload_button.setFixedWidth(40)
        self.reload_button.clicked.connect(self.browser.reload)
        
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addWidget(self.forward_button)
        top_layout.addWidget(self.reload_button)
        top_layout.addWidget(self.url_bar)
        
        main_widget = QWidget()
        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addWidget(self.browser)
        
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        
        print("[ OK ] successful loaded")
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

        print(f"[ OK ] successful loaded url {url}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec())
