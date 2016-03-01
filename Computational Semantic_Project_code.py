'''
import image

img = image.open()

for x in xrang(img.size[0]):
	for y in xrang(img.size[1]):
		r,g,b = img.getpixel((x,y))
		img.putpixel((x,y),(b,r,g))

img.show()

'''

from PIL import Image 
import sys
from PyQt4 import QtGui, QtCore
import os
from collections import defaultdict
import StringIO

'''
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle("PyQT Tuts!")

window.show()
'''
class Window(QtGui.QGraphicsPixmapItem):
	
	def __init__(self, pixmap=None, parent=None, scene=None):
		super(Window, self).__init__()
		self.startX, self.startY = -1, -1
		self.parent = parent
		self.radius = 10
		self.CornerList=[]
		self.rect = set()
		self.rectList = defaultdict(lambda : defaultdict(list))

		self.pen = QtGui.QPen(QtCore.Qt.SolidLine)
		self.pen.setColor(QtCore.Qt.yellow)
		self.pen.setWidth(2)

		self.brush = QtGui.QBrush(QtCore.Qt.yellow)



	def paint(self, painter, option, widget=None):
		painter.drawPixmap(0, 0, self.pixmap())
		painter.setPen(self.pen)
		painter.setBrush(self.brush)

		width = self.endX - self.startX
		height = self.endY - self.startY
		#void QPainter::drawRect(int x, int y, int width, int height)
		#painter.drawRect(self.startX, self.startY, width, height)
		#self.rectList[self.parent.imageList.currentItem().text()][self.parent.modelList.currentItem().text()] = [self.startX, self.startY, width, height]
		#for items in self.rectList[self.parent.imageList.currentItem().text()]:
		#	x,y,w,h = self.rectList[self.parent.imageList.currentItem().text()][items]
						
		#	rect = painter.drawRect(x, y, w, h)

		if self.startX >= 0 and self.startY >= 0:
			#painter.drawEllipse(self.x-self.radius, self.y-self.radius, 2*self.radius, 2*self.radius)
			painter.drawRect(self.startX-self.radius, self.startY-self.radius, width, height)
			#self.startX, self.startY = -1, -1

	def mousePressEvent (self, event):
		self.startX=event.pos().x()
		self.startY=event.pos().y()
		print("point at X{} Y{}".format(self.x,self.y))
		MainWindow.addToDict(self,self.x,self.y)
		
	def mouseMoveEvent (self, event):
		print ('mouse moving')
		self.endX=event.pos().x()
		self.endY=event.pos().y()            
		self.update()

	#def mouseReleaseEvent (self, event):
	#	print ('mouse moving')
	#	self.endX=event.pos().x()
	#	self.endY=event.pos().y()
	#	self.update()



class MainWindow(QtGui.QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		#QtCore.QCoreApplication.addLibraryPath(path.join(path.dirname(QtCore.__file__), "plugins"))
		self.coordDict = defaultdict(list)
		self.initUI()

	def initUI(self):
		self.DRAW = []
		self.modelList = QtGui.QListWidget(self)
		indir = 'images'
		self.imageList = QtGui.QListWidget(self)
		for root, dirs, filenames in os.walk(indir):
				for f in filenames:
					if f.endswith('jpg'):
						self.imageList.addItem(f)
		self.imageList.setCurrentRow(0)
		self.imageList.currentItemChanged.connect(self.loadImage)

		self.scene = QtGui.QGraphicsScene()
		self.scene.setSceneRect(0, 0, 800, 600)
		self.imagePanel = Window(scene = self.scene, parent = self)
		self.scene.addItem(self.imagePanel)

		self.view = QtGui.QGraphicsView(self.scene)

		#self.modelList = QtGui.QListWidget(self)
		self.loadImage()

		self.layout = QtGui.QHBoxLayout()
		self.layout.addWidget(self.imageList)
		self.layout.addWidget(self.view)
		self.layout.addWidget(self.modelList)

		self.setLayout(self.layout)    

		self.setGeometry(100, 100, 1200, 650)
		self.setWindowTitle('image annotation')    

	def loadImage(self):	
		self.DRAW = []
		
		path = str('newImages_files/' + self.imageList.currentItem().text())
		im = Image.open(path)
		
		#buf= StringIO.StringIO('images/' + self.imageList.currentItem().text()[:-4] + '.png')
		#im.save(buf,format ='PNG')
		im.save(str('newImages_files/' + self.imageList.currentItem().text()[:-4] + '.jpg'))
		
		pixmap = QtGui.QPixmap('newImages_files/' + self.imageList.currentItem().text()[:-4] + '.jpg')
		#pixmap = pixmap.scaledToWidth(600)
		self.imagePanel.setPixmap(pixmap)
		self.modelList.clear()
		with open('newmodels/' + self.imageList.currentItem().text()[:-4] + '.mod') as f:
			for line in f.readlines():
				if ',n_' in line:
					self.modelList.addItem(line.strip())
		

	def addToDict(self,x,y):
		print(x,y)

	def getCurrentModelItem(self):
		return self.modelList.currentItem().text()


	"""
class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.coordDict=defaultdict(list)
		self.Qlist = QListWidget(self)
		
		self.scene = QGraphicsScene()
		self.scene.setSceneRect(0, 0, 800, 600)

		pixmap, modpath=self.openImage()
		with open(modpath) as f:
			data = f.readlines()
		for line in data:
			if ',n_' in line:
				self.Qlist.addItem(line.strip())

		self.imagePanel = ImageDrawPanel(scene = self.scene)
		self.imagePanel.setPixmap(pixmap)
		self.scene.addItem(self.imagePanel)

		self.view = QGraphicsView(self.scene)

		self.edit = QTextEdit()
		self.edit.setText("Please indicate the coordinates \nof corners per item by clicking clockwise,\n starting topleft")

		layout = QHBoxLayout()
		layout.addWidget(self.view)
		layout.addWidget(self.Qlist)
		layout.addWidget(self.edit)

		self.Qlist.currentItemChanged.connect(self.on_item_changed)

		self.widget = QWidget()
		self.widget.setLayout(layout)
		self.entry = QLineEdit(self.widget)
		self.entry.setGeometry(QRect(10,10, 250, 20))
		self.entry.setObjectName("lineEdit")


		self.setCentralWidget(self.widget)
		self.setWindowTitle("Image Draw")
	
	def addToDict(self,x,y):
		print(x,y)
		

	def openImage(self):
		picpath = QFileDialog.getOpenFileName(self, "Open image", ".", "Image Files (*.bmp *.jpg *.png *.xpm)")
		modpath=picpath[:-4]+'.mod'
		return QPixmap(picpath),modpath

	def on_item_changed(self, curr):
		self.d=curr.text()
		self.entry.setText("Click corners of {}".format(self.d))

	"""

		#extractAction = QtGui.QAction("&xxx", xxx)
		#extractAction.setShortcut("Ctrl+Q")
		#extractAction.setStatusTip('Leave The App')
		#extractAction.triggered.connect(self.close_application)

		#self.statusBar()
		#mianMenu = self.menuBar()
		#fileMenu = mianMenu.addMenu('&File')
		#fileMenu.addAction (extractAction)

		#self.home()

	"""
	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		btn.resize(100,100)
		#btn.resize(btn.sizeHint())
		#btn.resize(btn.minimumSizeHint())
		btn.move(0,100)

		#extractAction = QtGui.QAction(QtGui.QIcon(''))

		self.show()

	def close_application(slef):
		print("what's that!")
		sys.exit()
		#self.setWindowTitle("PyQT Tuts")
	"""



def run():

	app = QtGui.QApplication(sys.argv)
	IMG = MainWindow()
	IMG.show()

	GUI = Window()

	sys.exit(app.exec_())

run()