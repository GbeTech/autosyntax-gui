from typing import List

from src.internals import Atom, Indentation
from src.utils import ignore

from . import DefOperator


class ClassOperator(DefOperator, keyword='class'):
	def __init__(self):
		super().__init__(op_keyword='class')
		self.name: Atom = None
		self.inheritances: List[str] = []
		self.init_operator = DefOperator()
		self.init_indented: Indentation
		self.assignment_possible = False

	@staticmethod
	def _create_super(indentation):
		# init_args = [atom.subject for atom in self.init_operator.atoms]
		super_indentation = indentation.next(depth=2)
		super_indentation.add_line('super().__init__(')
		# for arg in init_args:
		# 	super_indentation.add_word_to_last_line([arg, ', '])
		# self._close_line_w_parenthesis(super_indentation, line_idx=-1, colon=False)
		super_indentation.close_line_w_parenthesis(line_idx=-1, colon=False)
		return indentation

	def _handle_multiple_atoms(self):
		indentation = Indentation(f'class {self.name.subject}')
		self._set_inheritance_signature(indentation)
		with ignore(AttributeError):
			indentation.set_nested_indentation(self.init_indented)
			if self.inheritances:
				indentation = self._create_super(indentation)
		return indentation

	def _set_inheritance_signature(self, indentation):
		if self.inheritances:
			indentation.add_word_to_last_line('(')
			for supercls in self.inheritances:
				indentation.add_word_to_last_line([supercls, ', '])

			indentation.close_line_w_parenthesis(colon=False)
		indentation.add_word_to_last_line(':')

	def _set_inheritances(self, items_raw):
		with ignore(IndexError):
			while items_raw[0] != 'init':
				self.inheritances.append(items_raw[0])
				items_raw = items_raw[1:]

		return items_raw

	def _set_init_method(self, items_raw):
		with ignore(IndexError):
			if items_raw[0] == 'init':
				self.init_operator.set_is_within_class(True)
				self.init_operator.construct_atoms(items_raw)
				self.init_indented = self.init_operator._handle_multiple_atoms()
		return items_raw

	def construct_atoms(self, items_raw):
		items_raw = super()._set_untyped_name(items_raw)
		items_raw = self._set_inheritances(items_raw)
		self._set_init_method(items_raw)

	# noinspection PyMethodOverriding
	# @staticmethod
	# def _convert(indentation):
	# 	r_side = indentation.convert()
	# 	return r_side

	"""def _convert(self):
		indentation_lvls = [[f'class {self.name}']]
		if self.inheritances:
			indentation_lvls[0].append('(')
			for supercls in self.inheritances:
				indentation_lvls[0].append(supercls)
				indentation_lvls[0].append(', ')
			indentation_lvls[0].append(')')
		indentation_lvls[0].append(':')
		# r_side += '('
		# r_side += ', '.join([supercls.subject for supercls in self.inheritances]) + ')'
		# r_side += ':\n\t'
		with ignore(AttributeError):
			indentation_lvls.append([self.init_operator.name.result])
		# r_side += self.init_operator.name.result
		r_side = self._format_indentation_lvls(indentation_lvls)
		return r_side"""

# def _set_name(self, items_raw):
# 	self.name = items_raw[0]
# 	return items_raw[1:]
