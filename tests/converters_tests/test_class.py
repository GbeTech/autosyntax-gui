from . import get_expression

tri_quote = '"""'


def test_0():
	assert get_expression(f'class foo') == f'class foo:\n\t'


def test_1():
	assert get_expression(f'class foo Super') == f'class foo(Super):\n\t'


def test_2():
	expected = f"""class foo:
	def __init__(self):
	"""
	assert get_expression(f'class foo init') == expected


def test_3():
	expected = f"""class foo:
	def __init__(self, name):
		self.name = name
	"""
	assert get_expression(f'class foo init name') == expected


def test_4():
	expected = f"""class foo:
	def __init__(self, name):
		{tri_quote}
		:type name: str
		{tri_quote}
		self.name = name
	"""
	assert get_expression(f'class foo init name str') == expected


def test_5():
	expected = f"""class foo(Super):
	def __init__(self):
		super().__init__()
	"""
	assert get_expression(f'class foo Super init') == expected


def test_6():
	expected = f"""class foo(Super):
	def __init__(self, name):
		self.name = name
		super().__init__()
	"""
	assert get_expression(f'class foo Super init name') == expected


def test_7():
	expected = f"""class foo(Super):
	def __init__(self, name='moshe'):
		self.name = name
		super().__init__()
	"""
	assert get_expression(f'class foo Super init name .moshe') == expected


def test_8():
	expected = f"""class foo(Super):
	def __init__(self, name):
		{tri_quote}
		:type name: str
		{tri_quote}
		self.name = name
		super().__init__()
	"""
	assert get_expression(f'class foo Super init name str') == expected


def test_9():
	expected = f"""class foo(Super, Hi):
	"""
	assert get_expression(f'class foo Super Hi') == expected


def test_10():
	expected = f"""class foo(Super, Hi):
	def __init__(self):
		super().__init__()
	"""
	assert get_expression(f'class foo Super Hi init') == expected


def test_11():
	expected = f"""class Foo(Super, Hi):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		super().__init__()
	"""
	assert get_expression(f"class Foo Super Hi init name age") == expected


def test_12():
	expected = f"""class Foo(Super, Hi):
	def __init__(self, name):
		{tri_quote}
		:type name: str
		{tri_quote}
		self.name = name
		super().__init__()
	"""
	assert get_expression(f"class Foo Super Hi init name str") == expected


def test_13():
	expected = f"""class Foo(Super):
	def __init__(self, *args, **kwargs):
		super().__init__()
	"""
	assert get_expression(f"class Foo Super init args kwargs") == expected


def test_14():
	expected = f"""class Foo(Super):
	def __init__(self, *args, **kwargs):
		super().__init__()
	"""
	assert get_expression(f"class Foo Super init *args **kwargs") == expected


def test_15():
	expected = f"""class Foo(Super):
	def __init__(self, age=3):
		self.age = age
		super().__init__()
	"""
	assert get_expression(f"class Foo Super init age .3") == expected
