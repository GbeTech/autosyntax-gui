from .page import Page


class StrPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"str" assignment specific hotkey:', 'str', *args, **kwargs)
		self.setup_groupbox()
