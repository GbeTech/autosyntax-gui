from .page import Page


class ListPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"list" initiation specific hotkey:', 'list', *args, **kwargs)
		self.setup_groupbox()
