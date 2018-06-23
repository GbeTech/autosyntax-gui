# from src.internals.expression import Expression
# autosyntax\tests\converters_tests\__init__.py
from src.internals import Expression


def get_expression(clp, keyword=None):
	is_indented = '\t' in clp or '    ' in clp
	line = Expression(clp, is_indented, keyword)
	result = line.finalize()
	return result
