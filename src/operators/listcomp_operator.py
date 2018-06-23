# from operators.Operators import Operator
from src.operators.Operators import Operator
from src.utils import get_singular


class ListCompOperator(Operator, keyword='lcomp'):
	def __init__(self):
		super().__init__(op_keyword='lcomp')

	# noinspection PyMethodOverriding
	def _convert(self, subject_singular):
		if self.atoms[0].is_dotted:
			self.atoms[0].stringify_subject()
		converted = f'[{self.atoms[0].result} for {subject_singular} in {self.atoms[0].subject}]'
		return converted

	def handle_atoms(self):
		return self._handle_single_atom()

	def _handle_single_atom(self):
		self.atoms[0].parenthesize_builtins()
		subject_singular = get_singular(self.atoms[0].subject)

		self.atoms[0].close_parenthesis(around=subject_singular)
		return self._convert(subject_singular)
