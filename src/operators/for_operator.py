from src.operators.Operators import Operator
from src.utils import get_singular


class ForOperator(Operator, keyword='for'):
	def __init__(self):
		super().__init__(op_keyword='for')
		self.assignment_possible = False

	def _convert(self):
		# singular form devoid of ' / self. / *
		singular = get_singular(self.atoms[0].subject)
		converted = f'for {singular} in {self.atoms[0].result.replace("*","")}:\n\t'
		return converted

	def handle_atoms(self):
		return self._handle_single_atom()

	def _handle_single_atom(self):
		self.atoms[0].parenthesize_builtins()
		if self.atoms[0].is_dotted:
			self.atoms[0].stringify_subject()
		self.atoms[0].close_parenthesis(around=self.atoms[0].subject)
		return self._convert()
