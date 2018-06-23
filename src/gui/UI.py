from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal

# from gui.controls import KeySequenceEdit, TabGroup
from .pages import *
from .controls import KeySequenceEdit, TabGroup


# noinspection PyArgumentList
class UI(QObject):
	has_focus = pyqtSignal(bool)
	win_id = pyqtSignal(object)

	def setupUi(self, main_window):
		# main window properties
		self.main_window = main_window
		self.main_window.setFixedSize(650, 550)
		self.main_window.setWindowTitle('autosyntax')

		# enter / leave signal definitions
		self.main_window.enterEvent = lambda e: self.has_focus.emit(True)
		self.main_window.leaveEvent = lambda e: self.has_focus.emit(False)
		self.has_focus.connect(KeySequenceEdit.set_gui_has_focus)

		# set main operators tabs
		self.setup_tabs()

		QtCore.QMetaObject.connectSlotsByName(self.main_window)

	def setup_tabs(self):
		self.tabs_main = TabGroup(parent=self.main_window,
		                          geometry=(20, 20, 600, 481),
		                          )

		self.general_page = GeneralPage()
		self.class_page = ClassPage()
		self.def_page = DefPage()
		self.dict_page = DictPage()
		self.for_page = ForPage()
		self.list_page = ListPage()
		self.list_comp_page = ListCompPage()
		self.set_page = SetPage()
		self.tuple_page = TuplePage()
		self.print_page = PrintPage()
		self.str_page = StrPage()
		self.about_page = AboutPage()

		self.tabs_main.addTab(self.general_page, 'General')
		self.tabs_main.addTab(self.class_page, 'class')
		self.tabs_main.addTab(self.def_page, 'def')
		self.tabs_main.addTab(self.dict_page, 'dict')
		self.tabs_main.addTab(self.for_page, 'for')
		self.tabs_main.addTab(self.tuple_page, 'tuple')
		self.tabs_main.addTab(self.set_page, 'set')
		self.tabs_main.addTab(self.list_page, 'list')
		self.tabs_main.addTab(self.print_page, 'print')
		self.tabs_main.addTab(self.str_page, 'str')
		self.tabs_main.addTab(self.list_comp_page, 'list comprehension')
		self.tabs_main.addTab(self.about_page, 'About')
