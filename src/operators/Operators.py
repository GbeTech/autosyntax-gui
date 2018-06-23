from src.internals import Atom, BUILTIN_FUNCTIONS
from src.utils import xnor

# from internals.consts import BUILTIN_FUNCTIONS

# from utils.internals_utils import xnor

WRAPPERS = {
	'list':  ('[', ']'),
	'tuple': ('(', ')'),
	'set':   ('{', '}'), }


class Operator:
	_operators = {}

	def __init__(self, *, op_keyword):
		self.assignment_possible = True
		self.op_keyword = op_keyword
		self.atoms = []

	def __init_subclass__(cls, **kwargs):
		cls._operators[kwargs['keyword']] = cls

	@classmethod
	def by_keyword(cls, keyword):
		return cls._operators[keyword]()

	def _convert(self):
		"""
		:rtype: str
		"""
		r_side = ''
		wrapper = WRAPPERS[self.op_keyword]
		for atom in self.atoms:
			r_side += f'{atom.result}, '
		converted = f'{wrapper[0]}{r_side.strip()[:-1]}{wrapper[1]}'
		return converted

	def _handle_single_atom(self):
		""":rtype: str"""
		self._parenthesize_stringify(condition=lambda a: a.is_dotted)

		return f'{self.op_keyword}({self.atoms[0].result})'

	def _handle_multiple_atoms(self):
		self._parenthesize_stringify()
		return self._convert()

	def _parenthesize_stringify(self, condition=None):
		if isinstance(self.atoms, list):
			for atom in self.atoms:
				self._parenthesize_stringify_single(atom, condition)
		else:
			self._parenthesize_stringify_single(self.atoms[0], condition)

	@staticmethod
	def _parenthesize_stringify_single(atom, condition, dblquote=False):
		# KEEP STATIC AND ATOM AS PARAMETER
		if condition is None:
			condition = lambda a: xnor(a.digit_or_builtins_or_self(),
			                           a.is_dotted)

		atom.parenthesize_builtins()
		if condition(atom):
			atom.stringify_subject(dblquote)
		atom.close_parenthesis(around=atom.subject)

	def handle_atoms(self):
		if len(self.atoms) == 1:
			return self._handle_single_atom()
		else:
			return self._handle_multiple_atoms()

	def __eq__(self, other):
		return other == self.op_keyword

	@staticmethod
	def _construct_atom_with_builtins(items_raw, i):
		"""Add preceding builtins and set subject. Return atom"""
		atom = Atom(builtins=[items_raw[i]])
		j = i + 1
		while items_raw[j] in BUILTIN_FUNCTIONS:
			atom.builtins.append(items_raw[j])
			j += 1
		atom.subject = items_raw[j]
		i = j + 1
		return atom, i

	def construct_atoms(self, items_raw):
		"""Set atom.subject, atom.is_dotted, atom.has_builtins, atom._is_digit for each atom. No any string
		manipulation"""

		# atoms = []
		items_len = len(items_raw)
		i = 0
		while i < items_len:
			if items_raw[i] in BUILTIN_FUNCTIONS:
				atom, i = self._construct_atom_with_builtins(items_raw, i)
				self.atoms.append(atom)
				continue

			else:
				self.atoms.append(Atom(subject=items_raw[i]))
				i += 1
				continue


# return atoms


class SetOperator(Operator, keyword='set'):
	def __init__(self):
		super().__init__(op_keyword='set')


class TupleOperator(Operator, keyword='tuple'):
	def __init__(self):
		super().__init__(op_keyword='tuple')


class ListOperator(Operator, keyword='list'):
	def __init__(self):
		super().__init__(op_keyword='list')
