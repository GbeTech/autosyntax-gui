from configuration import ConfigMgr

# from gui.pages.page import Page
from .page import Page


class GeneralPage(Page):

	def __init__(self, *args, **kwargs):
		super().__init__('Main Hotkey:', *args, **kwargs)
		self.hotkey_edit.setKeySequence(ConfigMgr.hotkeys.global_hotkey)
