# from gui.pages.page import Page
from .page import Page


class AboutPage(Page):
	def __init__(self, *args, **kwargs):
		super().__init__('About text', *args, **kwargs)
