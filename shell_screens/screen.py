from typing import List, Union


def align(msgs: dict) -> List[str]:
	longest_key_len = max([len(key) for key in msgs.keys()])

	tabs_max = int(longest_key_len / 8)
	# Limits `tabs_max` to minimum 1, not 0
	tabs_max = tabs_max if tabs_max != 0 else 1
	ret = []
	for key, value in msgs.items():
		# ONLY NEEDED IN PYCHARM?
		# tabs_difference = int((longest_key_len - len(key)) / 8)

		tabs_num = tabs_max - int(len(key) / 8) + 1
		tabs = '\t' * tabs_num
		ret.append(f'{key}{tabs}{value}')
	return ret


def _underline(line) -> str:
	return '\n'.join([f'{line}',
	                  '-' * len(line)])


from abc import ABC, abstractmethod


class Screen(ABC):
	@abstractmethod
	def __init__(self, title, subtitle=None, *args):
		self.title = f'\n{_underline(title)}\n'
		if subtitle is not None:
			self.title += f'  *{subtitle}\n'

	def display(self):
		print(f'{self}\n')


class Subscreen(Screen):
	def __init__(self, title, msgs: dict, subtitle=None):
		super().__init__(title, subtitle)
		self.msgs: [] = align(msgs)

	def __str__(self):
		return '\n'.join([self.title, *self.msgs])


class MainScreen(Screen):
	def __init__(self, title, subtitle=None):
		super().__init__(title, subtitle)

		self.subscreens: List[Subscreen] = []

	def __str__(self):
		subscreens_pretty = [ss.__str__() for ss in self.subscreens]
		return '\n'.join([self.title,
		                  *subscreens_pretty])

	def add_subscreen(self, subscreen: Subscreen):
		self.subscreens.append(subscreen)
