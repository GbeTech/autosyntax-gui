from .page import Page


class SetPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('"set" initiation specific hotkey:', 'set', *args, **kwargs)
		self.setup_groupbox()
