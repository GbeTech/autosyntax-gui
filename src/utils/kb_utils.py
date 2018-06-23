import keyboard as kb
import asyncio

from pyperclip import paste, copy

loop = asyncio.get_event_loop()


@asyncio.coroutine
def clipboard_changed():
	prev_clp = paste()
	count = 0
	while True:
		yield from asyncio.sleep(0.0001)
		count += 1
		new_clp = paste()
		if new_clp != prev_clp or count >= 45:
			break
	print(f'\n\tpolled {count} times until clpbrd change')
	return count


def add_hotkey(*, hotkey, callback, suppress, trigger_on_release):
	print(f'registering: {hotkey}')
	kb.add_hotkey(hotkey=hotkey,
	              callback=callback,
	              suppress=suppress, trigger_on_release=trigger_on_release)


def remove_hotkey(hotkey_or_callback):
	kb.remove_hotkey(hotkey_or_callback)


def wait(hotkey=None, suppress=False, trigger_on_release=False):
	kb.wait(hotkey, suppress, trigger_on_release)


def do_magic(op_keyword=None):
	print('sending end+shift+home+shift+home, ctrl+c')
	kb.send('end+shift+home+shift+home, ctrl+c')
	loop.run_until_complete(clipboard_changed())
	clp = paste()
	print('sending home+shift+end')
	kb.send('home+shift+end')
	is_indented = '\t' in clp or '    ' in clp
	result = get_expression(clp, is_indented, op_keyword)
	copy(result)
	print('sending ctrl+v')
	kb.send('ctrl+v')


def get_expression(clp, is_indented, op_keyword):
	from src.internals import Expression
	line = Expression(clp, is_indented, op_keyword)
	result = line.finalize()
	return result
