from shell_screens import Subscreen
from . import MainScreen


def main():
	s = MainScreen('AUTOSYNTAX HELP')
	s.add_subscreen(Subscreen('commands', {
		'autosyntax start':              'start autosyntax',
		'autosyntax gui':                'start autosyntax with gui',
		'autosyntax --help':             'show this message',
		'autosyntax --config [setting]': 'show configuration wizard [of setting]'}))

	s.display()
