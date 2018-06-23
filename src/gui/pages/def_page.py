from .page import Page


class DefPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"def" initiation specific hotkey:', 'def', *args, **kwargs)
		self.setup_groupbox()
