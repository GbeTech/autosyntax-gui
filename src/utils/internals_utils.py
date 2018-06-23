from contextlib import contextmanager


def _is_builtin_const(target):
	return target in ['None', 'True', 'False']


def delete_many(src, *args):
	for arg in args:
		src = src.replace(arg, '')
	return src


def get_singular(clp):
	clp = delete_many(clp, "'", 'self.', '*')
	if len(clp) >= 2 and clp.endswith('s'):
		return clp[:-1]
	elif clp.startswith('i'):
		return 'item'
	else:
		return clp[0]


@contextmanager
def ignore(*exceptions):
	try:
		yield
	except exceptions:
		pass


def stringify(target, dblquote=False):
	surround = '"' if dblquote else "'"
	return surround_with(surround=surround, to_surround=target)


def stringify_if_not_builtin_const_or_digit(target):
	if not target.isdigit() and not _is_builtin_const(target):
		return stringify(target)
	else:
		return target


def surround_with(surround, to_surround):
	return f'{surround}{to_surround}{surround}'


def xnor(a, b):
	return not a ^ b


import types


def log(print_doc=False):
	def real_decorator(func: types.MethodType):
		def wrapper(*args, **kwargs):
			print(f'{func.__qualname__}')
			if print_doc:
				doc = func.__doc__
				if doc is not None:
					print(f'\tdoc: {doc}\n')

			func(*args, **kwargs)

		return wrapper

	return real_decorator


def class_logger(cls):
	class Wrapper:

		def __init__(self, *args, **kwargs):
			self.wrapped = cls(*args, **kwargs)

		def __getattr__(self, name):
			attr = getattr(self.wrapped, name)
			is_method = type(attr) == types.MethodType
			if is_method:
				return log(attr)
			else:
				return attr

	return Wrapper
