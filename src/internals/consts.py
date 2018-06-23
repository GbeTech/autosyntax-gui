BUILTIN_FUNCTIONS = ['abs', 'dict', 'min', 'hex', 'next', 'slice', 'any',
                     'id', 'object', 'sorted', 'ascii', 'enumerate', 'input', 'oct',
                     'bin', 'eval', 'int', 'open', 'str', 'bool', 'exec', 'ord',
                     'sum', 'bytearray', 'super', 'bytes', 'float', 'iter',
                     'print', 'tuple', 'callable', 'len', 'property', 'type', 'chr',
                     'frozenset', 'range', 'vars', 'repr', 'zip', 'reversed', 'complex',
                     'round', 'hash', 'memoryview', 'set', 'help', 'max', ]
OPTIONAL_2_ARGS = ['zip']
DONT_KNOW = ['dir', 'staticmethod', 'classmethod',
             '__import__', 'compile',
             'format', 'globals', 'locals', ]

FN_ITER = ['filter', 'all', 'map', ]
TWO_ARGS = ['delattr', 'divmod',
            'getattr', 'hasattr', 'isinstance', 'issubclass', 'pow', ]
THREE_ARGS = ['setattr']
BUILTIN_TYPES = ['dict', 'int', 'str', 'bool', 'tuple', 'set', 'list']
MAGIC_FUNCTIONS = {
	'init': [],
	'str':  [],
	'eq':   ['other']}
