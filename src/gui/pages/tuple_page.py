from .page import Page


class TuplePage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"tuple" initiation specific hotkey:', 'tuple', *args, **kwargs)
		self.setup_groupbox()
