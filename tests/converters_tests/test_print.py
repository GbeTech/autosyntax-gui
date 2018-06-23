from . import get_expression


def test_0():
	assert get_expression('print hi') == "print('hi')"


def test_1():
	assert get_expression('print .hi') == "print(hi)"


def test_1_33():
	assert get_expression('print str hi') == "print(str(hi))"


def test_1_66():
	assert get_expression('print str .hi') == "print(str('hi'))"


def test_2():
	assert get_expression('print hi bye') == "print('hi bye')"


def test_3():
	assert get_expression('print hi .bye') == "print(f'hi {bye}')"


def test_4():
	assert get_expression('print hi str bye') == "print(f'hi {str(bye)}')"


def test_5():
	assert get_expression('print .hi str bye') == "print(f'{hi} {str(bye)}')"


def test_6():
	assert get_expression('print .hi str .bye') == "print(f'{hi} {str(\"bye\")}')"


#
def test_7():
	assert get_expression('print self.hi') == "print(self.hi)"


def test_8():
	assert get_expression('print hi str self.bye') == "print(f'hi {str(self.bye)}')"


def test_9():
	assert get_expression('print hi self.bye') == "print(f'hi {self.bye}')"


"""SPECIFIC HOTKEY TESTS"""
