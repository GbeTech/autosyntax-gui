# import asyncio

# import keyboard as kb
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QKeySequenceEdit, QWidget

# from pyperclip import copy, paste

# from . import Expression
# from . import boilerplate, ignore, do_magic


# from utils.kb_utils import clipboard_changed
# from utils.internals_utils import ignore
# from utils import

# from pyqtkeybind import keybinder
# from utils.kb_utils import do_magic
from src.utils import boilerplate, ignore, do_magic, log, add_hotkey, remove_hotkey


class KeySequenceEdit(QKeySequenceEdit):
	_hotkeys = {}
	_gui_focused = False

	def __init__(self, *args, **kwargs):
		super().__init__(*args)
		boilerplate(self, **kwargs)
		self.op_keyword = kwargs['op_keyword']

		# checkmark
		self._checkmark = self._init_checkmark()

		# noinspection PyUnresolvedReferences
		super().editingFinished.connect(self._editingFinished)

		self._set_hk_ifnot_empty()

	def _set_hk_ifnot_empty(self):
		if not self.keySequence().isEmpty():
			self._set_keyboard_hotkey(self.keySequence().toString())
			self._toggle_checkmark(True)
		else:
			self._toggle_checkmark(False)

	@log()
	def setKeySequence(self, key_seq: str, **kwargs):
		super().setKeySequence(QKeySequence().fromString(key_seq))
		self._set_hk_ifnot_empty()

	@log()
	def _set_keyboard_hotkey(self, hotkey):
		self._remove_current_keyboard_hotkey()
		KeySequenceEdit._hotkeys[self.op_keyword] = hotkey

		add_hotkey(hotkey=hotkey,
		           callback=self._do_magic,
		           suppress=True, trigger_on_release=True)

	@staticmethod
	@log()
	def set_gui_has_focus(value):
		KeySequenceEdit._gui_focused = value

	# Escape to clear
	@log()
	def keyPressEvent(self, QKeyEvent):
		if QKeyEvent.key() == Qt.Key_Escape:
			self.clear()
			self._remove_current_keyboard_hotkey()
			self._toggle_checkmark(False)
		else:
			super().keyPressEvent(QKeyEvent)

	# call setKeySequence with current KeySequence
	# noinspection PyUnusedLocal
	@log()
	def _editingFinished(self, *args):
		self.setKeySequence(self.keySequence().toString())

	# keyboard

	@log()
	def _remove_current_keyboard_hotkey(self):
		with ignore(KeyError):
			print(f'unregistering: {KeySequenceEdit._hotkeys[self.op_keyword]}')
			remove_hotkey(KeySequenceEdit._hotkeys[self.op_keyword])

	@log()
	def _do_magic(self):
		if not KeySequenceEdit._gui_focused:
			print(f'self.op_keyword: ', self.op_keyword)
			do_magic(self.op_keyword)

	def _init_checkmark(self):
		# noinspection PyArgumentList
		_checkmark = QWidget(self.parent())
		geo: QRect = self.geometry()
		_checkmark.setGeometry(QRect(geo.right() + 20, geo.y() - 2, 25, 25))
		return _checkmark

	def _toggle_checkmark(self, green=True):
		bg = lambda file: f'background: url({file}.png)'
		if green:
			self._checkmark.setStyleSheet(bg('greensmall25'))
		# self._checkmark.setStyleSheet(bg('redsmall25'))
		else:
			self._checkmark.setStyleSheet(bg('redsmall25'))

	# print(f'releasing: {KeySequenceEdit._hotkeys[self.op_keyword]}')
	# kb.release(KeySequenceEdit._hotkeys[self.op_keyword])
	# print(kb.is_pressed(KeySequenceEdit._hotkeys[self.op_keyword]))

	# print('sending end+shift+home+shift+home, ctrl+c')
	# kb.send('end+shift+home+shift+home, ctrl+c')
	# self.loop.run_until_complete(clipboard_changed())
	# clp = paste()
	# print('sending home+shift+end')
	# kb.send('home+shift+end')
	# is_indented = '\t' in clp or '    ' in clp
	# result = self._get_expression(clp, is_indented)
	# copy(result)
	# print('sending ctrl+v')
	# kb.send('ctrl+v')

	# NOW IN kb_utils
	# def _get_expression(self, clp, is_indented):
	# 	line = Expression(clp, is_indented, self.op_keyword)
	# 	result = line.finalize()
	# 	return result

	"""def _is_indented_old(self, stop_recursion):
		kb.send('shift+home, ctrl+c')
		self.loop.run_until_complete(clipboard_changed())
		clp = paste()
		if '\t' in clp or '    ' in clp:
			kb.send('right')
			return True
		else:
			kb.send('home')
			return False if stop_recursion else self._is_indented_old(stop_recursion=True)"""

	"""def _has_indentation(self, fn=None):
		kb.send('shift+home, ctrl+c')
		self.loop.run_until_complete(clipboard_changed())
		clp = paste()
		print(f'\nfn is {fn}. clp: {clp}')
		if '\t' in clp:
			print('indentation found')
			kb.send('right')
			return True
		else:
			print('indentation not found')
			if fn is None:
				kb.send('home')
				return self._has_indentation(fn=lambda: False)
			else:
				return fn()

	def _is_indented_old(self):
		kb.send('shift+home, ctrl+c')
		self._has_indentation()
		self.loop.run_until_complete(clipboard_changed())
		clp = paste()
		if '\t' in clp:
			kb.send('right')
			return True
		else:
			print(f'indentation not found, current clp: {paste()}')
			kb.send('home')
			kb.send('shift+home, ctrl+c')
			self.loop.run_until_complete(clipboard_changed())
			clp = paste()
			if '\t' in clp:
				kb.send('right')
				return True
		return False


	def _ready_expression_new(self):
		if not KeySequenceEdit._gui_focused:
			kb.send('home, shift+left, ctrl+c')
			self.loop.run_until_complete(clipboard_changed())
			clp = paste()
			print(clp.__repr__())
"""
