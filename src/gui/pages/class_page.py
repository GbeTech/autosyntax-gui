from .page import Page


class ClassPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"class" declaration specific hotkey:', 'class', *args, **kwargs, )
		self.setup_groupbox()

# noinspection PyArgumentList
# def setup_groupbox(self):
# 	super().setup_groupbox()

# self.tab_var_detection = QWidget()
#
# self.tabs.addTab(self.tab_var_detection,
#                  'tab_var_detection', 'Variable Detection')
#
# self.tab_typings_detection = QWidget()
# self.tabs.addTab(self.tab_typings_detection,
#                  'tab_typings_detection',
#                  'Typings Detection')
