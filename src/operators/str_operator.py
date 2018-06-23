from . import PrintOperator


class StrOperator(PrintOperator, keyword='str'):
	def __init__(self):
		super().__init__()
		self.create_line = lambda x, f: f"{f}'{x}'"

	# don't remove, doesn't handle single atom differently than multiple
	def handle_atoms(self):
		return self._handle_multiple_atoms()
