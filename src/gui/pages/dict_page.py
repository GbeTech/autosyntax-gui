from .page import Page


class DictPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"dict" initiation specific hotkey:', 'dict', *args, **kwargs)
		self.setup_groupbox()
