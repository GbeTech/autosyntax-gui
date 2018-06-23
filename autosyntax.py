import ctypes

from PyQt5.QtWidgets import QApplication, QMainWindow

import shell_screens as screens
from src import UI
from sys import argv, exit, executable
from src.utils import kb_utils

"""class WinEventFilter(QAbstractNativeEventFilter):
	def __init__(self, keybinder):
		self.keybinder = keybinder
		super().__init__()
	
	# noinspection PyMethodOverriding
	def nativeEventFilter(self, eventType, message):
		ret = self.keybinder.handler(eventType, message)
		return ret, 0"""


def check_if_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except Exception:
		return False


def start_gui():
	app = QApplication(argv)
	# noinspection PyArgumentList
	MainWindow = QMainWindow()
	ui = UI()
	ui.setupUi(MainWindow)
	MainWindow.show()
	exit(app.exec_())


def start():
	from configuration import ConfigMgr
	kb_utils.add_hotkey(
		hotkey=ConfigMgr.hotkeys.global_hotkey,
		callback=kb_utils.do_magic,
		suppress=True, trigger_on_release=True)

	print(f'press {ConfigMgr.hotkeys.quit_hotkey} to exit')
	kb_utils.wait(ConfigMgr.hotkeys.quit_hotkey)


def main():
	if check_if_admin():
		cmnds_fns = {
			'start':    start,
			'gui':      start_gui,
			'--help':   screens.help.main,
			'--config': lambda: screens.config.main(argv[2:])}
		try:
			cmnds_fns[argv[1]]()
		except (KeyError, IndexError):
			screens.help.main()


	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", executable, "", None, 1)


if __name__ == "__main__":
	# argv.append('--config')
	# argv.append('hotkeys')
	# argv.append('global=ctrl+p')
	main()
