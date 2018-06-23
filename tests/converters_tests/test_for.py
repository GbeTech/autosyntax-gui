from . import get_expression


def test_0():
	assert get_expression('for collections') == 'for collection in collections:\n\t'


def test_1():
	assert get_expression('for collection') == 'for c in collection:\n\t'


def test_2():
	assert get_expression('for dict min max collection') == 'for c in dict(min(max(collection))):\n\t'


def test_3():
	assert get_expression('for dict min max collections') == 'for collection in dict(min(max(collections))):\n\t'


def test_4():
	assert get_expression('my = for collection') == 'my = for collection'


def test_5():
	assert get_expression('my = for dict min max collection') == 'my = for dict min max collection'


def test_6():
	assert get_expression('for .collection') == "for c in 'collection':\n\t"


def test_7():
	assert get_expression('for .collections') == "for collection in 'collections':\n\t"


def test_8():
	assert get_expression('for dict min max .collection') == "for c in dict(min(max('collection'))):\n\t"


def test_9():
	assert get_expression('for dict min max .collections') == "for collection in dict(min(max('collections'))):\n\t"


def test_10():
	assert get_expression('for self.collection') == "for c in self.collection:\n\t"


def test_11():
	assert get_expression('for self.collections') == "for collection in self.collections:\n\t"


def test_12():
	assert get_expression(
		'for dict min max self.collections') == 'for collection in dict(min(max(self.collections))):\n\t'


def test_13():
	assert get_expression('for args') == 'for arg in args:\n\t'
