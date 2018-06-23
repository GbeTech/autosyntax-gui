from typing import List

from . import Operator
from src.internals import (Atom, TypedAtom,
                           atom_factory, BUILTIN_TYPES,
                           MAGIC_FUNCTIONS,
                           Indentation)
from src.utils import ignore, surround_with


class DefOperator(Operator, keyword='def'):
	def __init__(self, op_keyword='def'):
		super().__init__(op_keyword=op_keyword)
		self.assignment_possible = False
		self._is_within_class = False
		self.name: Atom = None
		self.magic_args: List[str] = []

	def handle_atoms(self):
		indentation = self._handle_multiple_atoms()
		r_side = self._convert(indentation)
		return r_side

	def set_is_within_class(self, is_within_class):
		self._is_within_class = is_within_class
		if is_within_class:
			self.magic_args.append('self')

	def _set_name(self, items_raw):
		with ignore(IndexError):
			if items_raw[1] in BUILTIN_TYPES:
				self.name = TypedAtom(items_raw[0], items_raw[1])
				items_raw = items_raw[2:]
				return items_raw
		items_raw = self._set_untyped_name(items_raw)
		return items_raw

	def _set_untyped_name(self, items_raw):
		self.name = Atom(items_raw[0])
		items_raw = items_raw[1:]
		return items_raw

	def _set_magic_args(self):
		if self._is_within_class:
			if self.name.subject in MAGIC_FUNCTIONS:
				for m_arg in (MAGIC_FUNCTIONS[self.name.subject]):
					self.magic_args.append(m_arg)
				self.name.subject = surround_with('__', self.name.subject)

	def construct_atoms(self, items_raw):
		i = 0
		items_raw = self._set_name(items_raw)
		self._set_magic_args()
		rev_items = list(reversed(items_raw))
		items_len = len(items_raw)
		while i < items_len:
			if rev_items[i] in BUILTIN_TYPES or rev_items[i].startswith('.'):
				if rev_items[i + 1] in BUILTIN_TYPES:
					atom = atom_factory(subject=rev_items[i + 2],
					                    typing=rev_items[i + 1],
					                    default=rev_items[i])
					i += 3
				else:
					atom = atom_factory(subject=rev_items[i + 1],
					                    additional=rev_items[i])

					i += 2
			else:
				atom = Atom(subject=rev_items[i])
				i += 1
			self.atoms.append(atom)

		self.atoms = list(reversed(self.atoms))

	# noinspection PyMethodOverriding
	@staticmethod
	def _convert(indentation):
		r_side = indentation.convert()
		return r_side

	def _handle_multiple_atoms(self) -> Indentation:
		tri_quote = '"""'
		indentation = Indentation(f'def {self.name.subject}(')
		indentation.add_indented_line(tri_quote)

		for mag_arg in self.magic_args:
			indentation.add_word_to_last_line([mag_arg, ', '])
		# indentation.add_word_to_last_line(', ')

		for atom in self.atoms:
			indentation.add_word_to_last_line(atom.subject)
			with ignore(AttributeError):
				indentation.add_word_to_last_line(f'={atom.default}')
			with ignore(AttributeError):
				indentation.next().add_line(f':type {atom.subject}: {atom.typing}')
			indentation.add_word_to_last_line(', ')

		else:
			# self._close_line_w_parenthesis(indentation)
			indentation.close_line_w_parenthesis()

		with ignore(AttributeError):
			# noinspection PyUnresolvedReferences
			indentation.next().add_line(f':rtype: {self.name.typing}')

		if indentation.next().is_word_in_any_line('type'):
			indentation.next().add_line(tri_quote)
		else:
			indentation.next().lines = []

		if self.name.subject == '__init__':
			for atom in self.atoms:
				if 'args' not in atom.subject:
					indentation.next().add_line(f'self.{atom.subject} = {atom.subject}')

		return indentation

	""" NO USAGE
	@staticmethod
	def _close_line_w_parenthesis(indentation, *, line_idx=0, colon=True):
		closing_char = '):' if colon else ')'
		if indentation.lines[line_idx].words[-1] == ', ':
			indentation.lines[line_idx].words[-1] = closing_char
		else:
			indentation.add_word_to_last_line(closing_char)
	
	# NO USAGE
	@staticmethod
	def _format_indentation_lvls(indentation_lvls):
		lvl0 = ''.join(indentation_lvls[0])
		lvl1 = ''.join(f'\t{line}\n' for line in indentation_lvls[1])
		return f'{lvl0}\n{lvl1}\t'

	# NO USAGE
	def _add_instance_variables(self, indentation_lvls):
		for atom in self.atoms:
			indentation_lvls[1].append(f'self.{atom.subject} = {atom.subject}')
		return indentation_lvls

	# NO USAGE
	def _create_instance_variables(self):
		inst_vars = ''
		for atom in self.atoms:
			inst_vars += f'self.{atom.subject} = {atom.subject}\n\t'
		return inst_vars if 'self' in inst_vars else ''
"""
