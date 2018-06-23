from .page import Page


class PrintPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"print" initiation specific hotkey:', 'print', *args, **kwargs)
		self.setup_groupbox()
