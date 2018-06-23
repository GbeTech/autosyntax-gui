from typing import List


class Line:
	def __init__(self, firstword: str):
		self.words: List[str] = [firstword]
	
	# NO USAGE
	def add_word_at_index(self, word: str, index: int = None):
		self.words.insert(index, word)
	
	def __str__(self):
		return 'words: ' + ', '.join(self.words)


class Indentation:
	def __init__(self, firstword: str):
		self.lines: List[Line] = [Line(firstword)]
		self._indentation: Indentation = None
	
	@staticmethod
	def _convert_line(line):
		ret = ''
		for word in line.words:
			ret += word
		return ret
	
	def add_indented_line(self, firstword: str):
		if self._indentation is None:
			self._indentation = Indentation(firstword)
		else:
			self._indentation.add_line(firstword)
	
	def add_line(self, firstword: str):
		self.lines.append(Line(firstword))
	
	def add_word_to_last_line(self, word):
		if not isinstance(word, str):
			[self.lines[-1].words.append(w) for w in word]
		else:
			self.lines[-1].words.append(word)
	
	def convert(self, depth: int = 0) -> str:
		ret = ''
		for line in self.lines:
			ret += '\t' * depth
			ret += self._convert_line(line)
			ret += '\n'
		# ret += '\t'
		if self._indentation is not None:
			ret += self.next().convert(depth=depth + 1)
		
		if not ret.endswith('\n\t'):
			ret += '\t'
		return ret
	
	def erase_nested_indentation(self):
		self._indentation = None
	
	def is_word_in_any_line(self, search: str):
		for line in self.lines:
			for word in line.words:
				if search in word:
					return True
		return False
	
	def last_line(self):
		return self.lines[-1]
	
	def next(self, *, depth=1):
		if depth == 1:
			return self._indentation
		else:
			return self._indentation.next(depth=depth - 1)
	
	def set_nested_indentation(self, indentation):
		self._indentation = indentation
	
	def close_line_w_parenthesis(self, *, line_idx=0, colon=True):
		closing_char = '):' if colon else ')'
		if self.lines[line_idx].words[-1] == ', ':
			self.lines[line_idx].words[-1] = closing_char
		else:
			self.add_word_to_last_line(closing_char)
	
	"""# NO USAGE
		def add_word_to_line_at(self, word: str, line_idx: int):
			try:
				self.lines[line_idx].words.append(word)
			except IndexError:
				self.add_line(word)
				print(f'!!\tSPECIFIED INDEX OUT OF RANGE ({line_idx}), '
					  f'added new line at {len(self.lines)-1} '
					  f'with firstword = {word}')
			"""
# NO USAGE
