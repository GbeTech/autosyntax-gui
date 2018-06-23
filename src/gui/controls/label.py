from PyQt5.QtWidgets import QLabel

# from . import boilerplate
from src.utils import boilerplate


class Label(QLabel):
	def __init__(self, *args, **kwargs):
		super().__init__(*args)
		boilerplate(self, **kwargs)
		self.setText(kwargs['text'])

	def setStyleSheet(self, **kwargs):
		p_str = self._stylesheet.format()
		super().setStyleSheet(p_str)
