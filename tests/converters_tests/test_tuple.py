from . import get_expression


def test_0():
	assert get_expression('tuple hi bye') == "('hi', 'bye')"


def test_1():
	assert get_expression('tuple hi .bye') == "('hi', bye)"


def test_2():
	assert get_expression('my = tuple hi bye') == "my = ('hi', 'bye')"


def test_3():
	assert get_expression('my = tuple hi .bye') == "my = ('hi', bye)"


def test_4():
	assert get_expression('tuple dict min max collection') == 'tuple(dict(min(max(collection))))'


def test_5():
	assert get_expression('tuple dict min max collection1 collection2') == "(dict(min(max(collection1))), 'collection2')"


def test_6():
	assert get_expression(
		'tuple dict min max collection1 collection2 .collection3') == "(dict(min(max(collection1))), 'collection2', " \
	                                                                  "collection3)"


def test_7():
	assert get_expression(
		'tuple dict min max collection1 collection2 str collection3') == "(dict(min(max(collection1))), 'collection2', " \
	                                                                     "" \
	                                                                     "" \
	                                                                     "str(collection3))"


def test_8():
	assert get_expression('tuple dict .collection') == "tuple(dict('collection'))"


def test_9():
	assert get_expression(
		'my = tuple dict min max collection1 collection2 str collection3') == "my = (dict(min(max(collection1))), " \
	                                                                          "'collection2', str(collection3))"


def test_10():
	assert get_expression('tuple hi') == 'tuple(hi)'


def test_11():
	assert get_expression('tuple .hi') == "tuple('hi')"


def test_12():
	assert get_expression('my = tuple hi') == "my = tuple(hi)"


def test_13():
	assert get_expression('my = tuple .hi') == "my = tuple('hi')"


def test_14():
	assert get_expression('tuple 1 2') == "(1, 2)"


def test_15():
	assert get_expression('tuple 1 .2') == "(1, '2')"


def test_26():
	assert get_expression('tuple hi self.bye') == "('hi', self.bye)"
