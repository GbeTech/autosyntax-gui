from . import get_expression


def test_0():
	assert get_expression('lcomp collection') == "[c for c in collection]"


def test_1():
	assert get_expression('my = lcomp collection') == "my = [c for c in collection]"


def test_2():
	assert get_expression('lcomp collections') == "[collection for collection in collections]"


def test_3():
	assert get_expression('my = lcomp collections') == "my = [collection for collection in collections]"


def test_4():
	assert get_expression('lcomp .collection') == "[c for c in 'collection']"


def test_5():
	assert get_expression('my = lcomp .collection') == "my = [c for c in 'collection']"


def test_6():
	assert get_expression('lcomp .collections') == "[collection for collection in 'collections']"


def test_7():
	assert get_expression('my = lcomp .collections') == "my = [collection for collection in 'collections']"


def test_8():
	assert get_expression('lcomp str zip dict collection') == "[str(zip(dict(c))) for c in collection]"


def test_9():
	assert get_expression('lcomp str zip dict .collection') == "[str(zip(dict(c))) for c in 'collection']"


def test_10():
	assert get_expression('lcomp str zip dict .collection') == "[str(zip(dict(c))) for c in 'collection']"


def test_11():
	assert get_expression('lcomp str zip dict self.collection') == "[str(zip(dict(c))) for c in self.collection]"


def test_12():
	assert get_expression(
		'lcomp str zip dict self.collections') == "[str(zip(dict(collection))) for collection in self.collections]"


def test_13():
	assert get_expression('lcomp self.collections') == "[collection for collection in self.collections]"
