# noinspection PyMethodOverriding,PyArgumentList
from PyQt5.QtWidgets import QTabWidget

# from . import boilerplate
from src.utils import boilerplate


# noinspection PyUnusedLocal
class TabGroup(QTabWidget):
	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent)
		boilerplate(self, **kwargs)

	# noinspection PyMethodOverriding
	def addTab(self, tab, tab_text):
		# tab = QWidget()
		# tab.setObjectName(tab_name)
		super().addTab(tab, '')
		self.setTabText(self.indexOf(tab), tab_text)
