import configparser

# import json
import os

#
CONFIG_DIRNAME = 'configuration'
CONFIG_FILENAME = 'config.ini'
CONFIG_FILE_FULLPATH = os.path.join(CONFIG_DIRNAME, CONFIG_FILENAME)


def _load_config_ini():
	try:
		ini = configparser.ConfigParser()
		ini.read(CONFIG_FILE_FULLPATH)
		return ini
	except FileNotFoundError as e:
		raise FileNotFoundError('\n'.join([f'configuration file not found.',
		                                   f'CONFIG_DIRNAME: {CONFIG_DIRNAME}',
		                                   f'CONFIG_FILENAME: {CONFIG_FILENAME}',
		                                   f'CONFIG_FILE_FULLPATH: {CONFIG_FILE_FULLPATH}',
		                                   f'getcwd: {os.getcwd()}',
		                                   f'listdir: {os.listdir()}',
		                                   f'original error: {e}']))


class Hotkeys:
	def __init__(self, hotkeys: dict):
		self.global_hotkey = hotkeys['global_hotkey']
		self.quit_hotkey = hotkeys['quit_hotkey']


class ConfigMgr:
	_ini = _load_config_ini()
	hotkeys = Hotkeys(_ini['Hotkeys'])

	@staticmethod
	def set(section, key, value):
		ConfigMgr._ini[section][key] = value
		with open(CONFIG_FILE_FULLPATH, 'w') as configfile:
			ConfigMgr._ini.write(configfile)
