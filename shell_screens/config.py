from configuration import ConfigMgr
from . import MainScreen, Subscreen


def hotkeys(hotkeys=None):
	ALIASES = {
		'global':        'global_hotkey',
		'global_hotkey': 'global_hotkey'}
	if hotkeys is None or hotkeys == []:
		ss = Subscreen('hotkeys config', {
			'global': 'set the global hotkey'},
		               "You're here: 'autosyntax.py --config hotkeys'")
		ss.display()
		_choice = input('choose hotkey to set: ')
		_value = input('hotkey value: ')
		# print(f'{_choice} hotkey was changed to: {_value}')
		print(f'Executing --config hotkeys {_choice}={_value}')
		ConfigMgr.set('Hotkeys', ALIASES[_choice], _value)

	else:
		for hotkey in hotkeys:
			_choice, _, _value = hotkey.partition('=')
			ConfigMgr.set('Hotkeys', ALIASES[_choice], _value)


def operators():
	ss = Subscreen('operators config', {
		'list':     'configure list operator',
		'dict':     'configure dict operator',
		'tuple':    'configure tuple operator',
		'for':      'configure for operator',
		'listcomp': 'configure listcomp operator',
		'class':    'configure class operator',
		'def':      'configure def operator',
		'str':      'configure str operator',
		'print':    'configure print operator',
		})
	ss.display()


def main(cmnd=None):
	cmnds_fns = {
		'hotkeys':   hotkeys,
		'operators': operators}

	# If given an empty list or left for default
	if cmnd is None or cmnd == []:
		s = MainScreen('AUTOSYNTAX CONFIGURATION',
		               subtitle="You're here: 'autosyntax.py --config [command]'")
		s.add_subscreen(Subscreen('commands', {
			'hotkeys':   'configure hotkeys',
			'operators': 'configure operators'}))

		s.display()
		_input = input('type command: ')
		try:
			cmnds_fns[_input](cmnd[1:])
		except KeyError:
			s.display()

	else:
		# args = cmnd[1:] if bool(cmnd[1:]) else None
		cmnds_fns[cmnd[0]](cmnd[1:])
