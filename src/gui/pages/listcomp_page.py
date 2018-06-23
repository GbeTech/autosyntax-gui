from .page import Page


class ListCompPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('List Comprehension assignment specific hotkey:', 'lcomp', *args, **kwargs)
		self.setup_groupbox()
