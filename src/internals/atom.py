from abc import ABC, abstractmethod

from src.utils import stringify_if_not_builtin_const_or_digit, stringify


# from utils.internals_utils import stringify, stringify_if_not_builtin_const_or_digit


def atom_factory(**kwargs):
	""":returns: Defaulted (additional startswith .)/Typed (additional)/Complex (3 args)"""
	try:
		if kwargs['additional'].startswith('.'):
			return DefaultedAtom(subject=kwargs['subject'],
			                     default=kwargs['additional'])
		else:
			return TypedAtom(subject=kwargs['subject'],
			                 typing=kwargs['additional'])
	except KeyError:
		return ComplexAtom(subject=kwargs['subject'],
		                   default=kwargs['default'],
		                   typing=kwargs['typing'])


class AbsAtom(ABC):

	@abstractmethod
	def __init__(self, subject=''):
		"""set subject and is_dotted 20.4.18"""
		self.is_dotted = False
		self.has_self = False
		self.subject = subject

	@property
	def subject(self):
		return self.__subject

	@subject.setter
	def subject(self, value):
		if value.startswith('.'):
			self.__subject = value[1:]
			self.is_dotted = True
		elif value.startswith('self.'):
			self.has_self = True
			self.__subject = value
		else:
			if 'kwargs' in value:
				value = '**' + value if '*' not in value else value
			elif 'args' in value:
				value = '*' + value if '*' not in value else value
			self.__subject = value


class Atom(AbsAtom):
	def __init__(self, subject='', builtins=None):
		self.builtins = builtins if builtins is not None else []
		self.result = ''
		super().__init__(subject)

	def _is_digit(self):
		return self.subject.isdigit()

	def has_builtins(self):
		return bool(self.builtins)

	def digit_or_builtins_or_self(self):
		return self.has_builtins() or self._is_digit() or self.has_self

	def dotted_or_builtins_or_self(self):
		return self.is_dotted or self.has_builtins() or self.has_self

	def close_parenthesis(self, *, around):
		self.result += around + ')' * len(self.builtins)

	def stringify_subject(self, dblquote=False):
		self.subject = stringify(self.subject, dblquote)

	def parenthesize_builtins(self):
		for builtin in self.builtins:
			self.result += builtin + '('

	def __str__(self):
		ret = f'subject: {self.subject}'
		ret += f'builtins: {",".join(self.builtins)}' if self.has_builtins() else ''
		ret += f'result: {self.result}' if self.result != '' else ''
		return ret


class TypedAtom(AbsAtom):
	def __init__(self, subject='', typing=''):
		self.typing = typing
		super().__init__(subject)

	def __str__(self):
		return f'subject: {self.subject} typing: {self.typing}'


class DefaultedAtom(AbsAtom):
	def __init__(self, subject='', default=''):
		self.default = default
		super().__init__(subject)

	@property
	def default(self):
		return self.__default

	@default.setter
	def default(self, value):
		value = self._undot_default(value)
		# noinspection PyAttributeOutsideInit
		self.__default = stringify_if_not_builtin_const_or_digit(value)

	@staticmethod
	def _undot_default(default):
		return default[1:] if default.startswith('.') else default

	def __str__(self):
		return f'subject: {self.subject} default: {self.default}'


class ComplexAtom(DefaultedAtom):

	def __init__(self, subject='', default='', typing=''):
		self.typing = typing
		super().__init__(subject, default)

	def __str__(self):
		return f'subject: {self.subject} typing: {self.typing} default: {self.default}'
