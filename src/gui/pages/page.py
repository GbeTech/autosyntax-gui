from PyQt5.QtWidgets import QWidget

# from . import KeySequenceEdit, Label, TabGroup, GroupBox


# noinspection PyArgumentList
from src.gui.controls import Label, KeySequenceEdit, GroupBox, TabGroup


class Page(QWidget):

	def __init__(self, hotkey_label_text=None, op_keyword=None, *args, **kwargs):
		"""
		:param hotkey_label_text: If given, self.setup_hotkey_stuff is called
		:param op_keyword: Passed to self.hotkey_edit:KeySequenceEdit, eventually to Expression
		:type op_keyword: str
		"""
		super().__init__(*args, **kwargs)
		if hotkey_label_text is not None:
			self.setup_hotkey_stuff(hotkey_label_text, op_keyword)

	def setup_hotkey_stuff(self, label_text, op_keyword):
		self.hotkey_label = Label(
			self,
			geometry=(10, 20, 170, 16),
			text=label_text,
			)

		self.hotkey_edit = KeySequenceEdit(
			self,
			op_keyword=op_keyword,
			geometry=(200, 20, 150, 20),
			focus=True,
			)
		"""self.is_admin_button = QPushButton(self)
		self.is_admin_button.setGeometry(QRect(310, 70, 150, 16))
		self.is_admin_button.setText('is admin')
		self.is_admin_button.setToolTip(str(check_if_admin()))"""
		self.press_esc_to_clear = Label(
			self,
			geometry=(310, 70, 150, 16),
			text='*Press ESC to clear',
			)

	def setup_groupbox(self):
		self.groupbox = GroupBox(self,
		                         geometry=(10, 90, 411, 330),
		                         )

		self.tabs = TabGroup(parent=self.groupbox,
		                     geometry=(20, 30, 371, 301),
		                     )
		# noinspection PyArgumentList
		self.tab_var_detection = QWidget()

		self.tabs.addTab(self.tab_var_detection,
		                 'tab_var_detection')

		# noinspection PyArgumentList
		self.tab_typings_detection = QWidget()
		self.tabs.addTab(self.tab_typings_detection,
		                 'tab_typings_detection',
		                 )
