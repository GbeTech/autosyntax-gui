import pytest

from src.internals import MAGIC_FUNCTIONS
from . import get_expression

tri_quote = '"""'


def test_0():
	assert get_expression(f'def foo') == f'def foo():\n\t'


def test_1():
	assert (get_expression(f'def foo p1') ==
	        f'def foo(p1):\n\t')


def test_2():
	assert (get_expression(f'def foo p1 p2') ==
	        f'def foo(p1, p2):\n\t')


def test_3():
	expected = f"""def foo(self, p1, p2):
	"""
	assert (get_expression('\tdef foo p1 p2') ==
	        expected)


def test_3_andahalf():
	assert (get_expression("""    def foo p1 p2""") ==
	        f'def foo(self, p1, p2):\n\t')


def test_4():
	assert (get_expression(f'def foo p1 .None') ==
	        f'def foo(p1=None):\n\t')


def test_5():
	assert (get_expression(f'def foo p1 .None p2') ==
	        f'def foo(p1=None, p2):\n\t')


def test_6_a():
	assert (get_expression(f'def foo p1 .False p2') ==
	        f'def foo(p1=False, p2):\n\t')


def test_6_b():
	assert (get_expression(f'def foo p1 .True p2') ==
	        f'def foo(p1=True, p2):\n\t')


def test_6_c():
	assert (get_expression(f'def foo p1 .1 p2') ==
	        f'def foo(p1=1, p2):\n\t')


def test_7():
	expected = f"""def foo(p1):
	{tri_quote}
	:type p1: str
	{tri_quote}
	"""
	assert (get_expression(f'def foo p1 str') == expected)


def test_8():
	expected = f"""def foo(p1):
	{tri_quote}
	:rtype: str
	{tri_quote}
	"""
	assert (get_expression(f'def foo str p1') == expected)


def test_9():
	expected = f"""def foo(p1):
	{tri_quote}
	:type p1: str
	:rtype: str
	{tri_quote}
	"""
	assert (get_expression(f'def foo str p1 str') == expected)


def test_10():
	assert (get_expression(f'def foo p1 .default p2') ==
	        "def foo(p1='default', p2):\n\t")


def test_11():
	expected = f"""def foo(p1='default', p2):
	{tri_quote}
	:type p2: str
	{tri_quote}
	"""
	assert (get_expression(f'def foo p1 .default p2 str') == expected)


def test_12():
	assert (get_expression(f'my = def foo p1 .default p2 str') ==
	        f'my = def foo p1 .default p2 str')


def test_13():
	for mag_fn in MAGIC_FUNCTIONS:
		mandatory_args = ', '.join(['self'] + MAGIC_FUNCTIONS[mag_fn])
		assert (get_expression(f'\tdef {mag_fn}') ==
		        f"def __{mag_fn}__({mandatory_args}):\n\t")


def test_14():
	expected = f"""def __init__(self, age):
	self.age = age
	"""
	assert (get_expression(f'\tdef init age') == expected)


def test_15():
	expected = f"""def __init__(self, age, name='moshe'):
	{tri_quote}
	:type age: int
	{tri_quote}
	self.age = age
	self.name = name
	"""
	assert (get_expression(f'\tdef init age int name .moshe') == expected)


def test_16():
	expected = f"""def what(p1='lol'):
	{tri_quote}
	:type p1: str
	{tri_quote}
	"""
	assert get_expression(f"def what p1 str .lol") == expected


def test_17():
	expected = f"""def what(p1='lol'):
	{tri_quote}
	:type p1: str
	:rtype: int
	{tri_quote}
	"""
	assert get_expression(f"def what int p1 str .lol") == expected


def test_18():
	expected = f"""def what(p1=1):
	{tri_quote}
	:type p1: str
	:rtype: int
	{tri_quote}
	"""
	assert get_expression(f"def what int p1 str .1") == expected


def test_19():
	expected = f"""def what(*args):
	"""
	assert get_expression(f"def what args") == expected


def test_20():
	expected = f"""def what(**kwargs):
	"""
	assert get_expression(f"def what kwargs") == expected


def test_21():
	expected = f"""def what(*args, **kwargs):
	"""
	assert get_expression(f"def what args kwargs") == expected


def test_22():
	expected = f"""def what(hi, *args, **kwargs):
	"""
	assert get_expression(f"def what hi args kwargs") == expected


@pytest.mark.skip
def test_119():
	expected = f"""def what(p1='1'):
	{tri_quote}
	:type p1: str
	:rtype: int
	{tri_quote}
	"""
	assert get_expression(f"def what int p1 str 1") == expected
