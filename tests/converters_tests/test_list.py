from . import get_expression


def test_0():
	assert get_expression('list hi bye') == "['hi', 'bye']"


def test_1():
	assert get_expression('list hi .bye') == "['hi', bye]"


def test_2():
	assert get_expression('my = list hi bye') == "my = ['hi', 'bye']"


def test_3():
	assert get_expression('my = list hi .bye') == "my = ['hi', bye]"


def test_4():
	assert get_expression('list dict min max collection') == 'list(dict(min(max(collection))))'


def test_5():
	assert get_expression('list dict min max collection1 collection2') == "[dict(min(max(collection1))), 'collection2']"


def test_6():
	assert get_expression(
		'list dict min max collection1 collection2 .collection3') == "[dict(min(max(collection1))), 'collection2', " \
	                                                                 "collection3]"


def test_7():
	assert get_expression(
		'list dict min max collection1 collection2 str collection3') == "[dict(min(max(collection1))), 'collection2', " \
	                                                                    "" \
	                                                                    "" \
	                                                                    "str(collection3)]"


def test_8():
	assert get_expression('list dict .collection') == "list(dict('collection'))"


def test_9():
	assert get_expression(
		'my = list dict min max collection1 collection2 str collection3') == "my = [dict(min(max(collection1))), " \
	                                                                         "'collection2', str(collection3)]"


def test_10():
	assert get_expression('list hi') == 'list(hi)'


def test_11():
	assert get_expression('list .hi') == "list('hi')"


def test_12():
	assert get_expression('my = list hi') == "my = list(hi)"


def test_13():
	assert get_expression('my = list .hi') == "my = list('hi')"


def test_14():
	assert get_expression('list 1 2') == "[1, 2]"


def test_15():
	assert get_expression('list 1 .2') == "[1, '2']"


def test_16():
	assert get_expression('my = list 1 2') == "my = [1, 2]"


def test_17():
	assert get_expression('my = list 1 .2') == "my = [1, '2']"


def test_18():
	assert get_expression('list hi 2') == "['hi', 2]"


def test_19():
	assert get_expression('list hi .2') == "['hi', '2']"


def test_20():
	assert get_expression('list hi str 2') == "['hi', str(2)]"


def test_21():
	assert get_expression('list str .hi zip .2') == "[str('hi'), zip('2')]"


def test_22():
	assert get_expression('list hi self.bye') == "['hi', self.bye]"


def test_23():
	assert get_expression('list hi str zip self.bye') == "['hi', str(zip(self.bye))]"
