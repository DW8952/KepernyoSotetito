import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

# Read the alpha value (0-255) from the file
with open('hasznal.txt', 'r') as file:
    lines = file.readlines()
    # Ensure the value is an integer between 0 and 255
    try:
        megadott = int(lines[-1].strip()) if lines else 0
        megadott = max(0, min(255, megadott))
    except ValueError:
        megadott = 0

app = QApplication(sys.argv)
window = QWidget()

# Required for click-through and frameless
window.setWindowFlags(
    Qt.FramelessWindowHint |
    Qt.WindowTransparentForInput |
    Qt.WindowStaysOnTopHint
)
# Required for transparency support
window.setAttribute(Qt.WA_TranslucentBackground)

# Override the paintEvent to draw the semi-transparent background manually
def paintEvent(event):
    painter = QPainter(window)
    # Create a color with the desired alpha (RGBA: 0, 0, 0, alpha)
    color = QColor(0, 0, 0, megadott)
    painter.fillRect(window.rect(), color)

window.paintEvent = paintEvent

window.showFullScreen()
sys.exit(app.exec_())   