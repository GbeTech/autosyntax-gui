from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt


def boilerplate(control, **kwargs):
	# control.setObjectName(kwargs['name'])
	control.setGeometry(QRect(*kwargs['geometry']))
	if "focus" in kwargs:
		control.setFocus()


# else:
# 	control.setFocusPolicy(Qt.NoFocus)

# NO USAGE
def get_font(family="Segoe UI", size=12, spacing=1.1):
	font = QtGui.QFont()
	font.setFamily(family)
	font.setPointSize(size)
	font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, spacing)
	return font


# NO USAGE
def get_alignment(alignment):
	alignments = {
		'C':  Qt.AlignCenter,
		'HC': Qt.AlignHCenter,
		'VC': Qt.AlignVCenter,
		'B':  Qt.AlignBottom,
		'T':  Qt.AlignTop,
		'R':  Qt.AlignRight,
		'L':  Qt.AlignLeft,
		'J':  Qt.AlignJustify}

	return alignments[alignment]
