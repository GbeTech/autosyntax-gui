from .page import Page


class ForPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"for" initiation specific hotkey:', 'for', *args, **kwargs)
		self.setup_groupbox()
