# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/pylint-dev/astroid/blob/main/LICENSE
# Copyright (c) https://github.com/pylint-dev/astroid/blob/main/CONTRIBUTORS.txt

from astroid import nodes
from astroid.brain.helpers import register_module_extender
from astroid.builder import parse
from astroid.manager import AstroidManager


def _curses_transform() -> nodes.Module:
    return parse(
        """
    A_ALTCHARSET = 1
    A_BLINK = 1
    A_BOLD = 1
    A_DIM = 1
    A_INVIS = 1
    A_ITALIC = 1
    A_NORMAL = 1
    A_PROTECT = 1
    A_REVERSE = 1
    A_STANDOUT = 1
    A_UNDERLINE = 1
    A_HORIZONTAL = 1
    A_LEFT = 1
    A_LOW = 1
    A_RIGHT = 1
    A_TOP = 1
    A_VERTICAL = 1
    A_CHARTEXT = 1
    A_ATTRIBUTES = 1
    A_CHARTEXT = 1
    A_COLOR = 1
    KEY_MIN = 1
    KEY_BREAK = 1
    KEY_DOWN = 1
    KEY_UP = 1
    KEY_LEFT = 1
    KEY_RIGHT = 1
    KEY_HOME = 1
    KEY_BACKSPACE = 1
    KEY_F0 = 1
    KEY_Fn = 1
    KEY_DL = 1
    KEY_IL = 1
    KEY_DC = 1
    KEY_IC = 1
    KEY_EIC = 1
    KEY_CLEAR = 1
    KEY_EOS = 1
    KEY_EOL = 1
    KEY_SF = 1
    KEY_SR = 1
    KEY_NPAGE = 1
    KEY_PPAGE = 1
    KEY_STAB = 1
    KEY_CTAB = 1
    KEY_CATAB = 1
    KEY_ENTER = 1
    KEY_SRESET = 1
    KEY_RESET = 1
    KEY_PRINT = 1
    KEY_LL = 1
    KEY_A1 = 1
    KEY_A3 = 1
    KEY_B2 = 1
    KEY_C1 = 1
    KEY_C3 = 1
    KEY_BTAB = 1
    KEY_BEG = 1
    KEY_CANCEL = 1
    KEY_CLOSE = 1
    KEY_COMMAND = 1
    KEY_COPY = 1
    KEY_CREATE = 1
    KEY_END = 1
    KEY_EXIT = 1
    KEY_FIND = 1
    KEY_HELP = 1
    KEY_MARK = 1
    KEY_MESSAGE = 1
    KEY_MOVE = 1
    KEY_NEXT = 1
    KEY_OPEN = 1
    KEY_OPTIONS = 1
    KEY_PREVIOUS = 1
    KEY_REDO = 1
    KEY_REFERENCE = 1
    KEY_REFRESH = 1
    KEY_REPLACE = 1
    KEY_RESTART = 1
    KEY_RESUME = 1
    KEY_SAVE = 1
    KEY_SBEG = 1
    KEY_SCANCEL = 1
    KEY_SCOMMAND = 1
    KEY_SCOPY = 1
    KEY_SCREATE = 1
    KEY_SDC = 1
    KEY_SDL = 1
    KEY_SELECT = 1
    KEY_SEND = 1
    KEY_SEOL = 1
    KEY_SEXIT = 1
    KEY_SFIND = 1
    KEY_SHELP = 1
    KEY_SHOME = 1
    KEY_SIC = 1
    KEY_SLEFT = 1
    KEY_SMESSAGE = 1
    KEY_SMOVE = 1
    KEY_SNEXT = 1
    KEY_SOPTIONS = 1
    KEY_SPREVIOUS = 1
    KEY_SPRINT = 1
    KEY_SREDO = 1
    KEY_SREPLACE = 1
    KEY_SRIGHT = 1
    KEY_SRSUME = 1
    KEY_SSAVE = 1
    KEY_SSUSPEND = 1
    KEY_SUNDO = 1
    KEY_SUSPEND = 1
    KEY_UNDO = 1
    KEY_MOUSE = 1
    KEY_RESIZE = 1
    KEY_MAX = 1
    ACS_BBSS = 1
    ACS_BLOCK = 1
    ACS_BOARD = 1
    ACS_BSBS = 1
    ACS_BSSB = 1
    ACS_BSSS = 1
    ACS_BTEE = 1
    ACS_BULLET = 1
    ACS_CKBOARD = 1
    ACS_DARROW = 1
    ACS_DEGREE = 1
    ACS_DIAMOND = 1
    ACS_GEQUAL = 1
    ACS_HLINE = 1
    ACS_LANTERN = 1
    ACS_LARROW = 1
    ACS_LEQUAL = 1
    ACS_LLCORNER = 1
    ACS_LRCORNER = 1
    ACS_LTEE = 1
    ACS_NEQUAL = 1
    ACS_PI = 1
    ACS_PLMINUS = 1
    ACS_PLUS = 1
    ACS_RARROW = 1
    ACS_RTEE = 1
    ACS_S1 = 1
    ACS_S3 = 1
    ACS_S7 = 1
    ACS_S9 = 1
    ACS_SBBS = 1
    ACS_SBSB = 1
    ACS_SBSS = 1
    ACS_SSBB = 1
    ACS_SSBS = 1
    ACS_SSSB = 1
    ACS_SSSS = 1
    ACS_STERLING = 1
    ACS_TTEE = 1
    ACS_UARROW = 1
    ACS_ULCORNER = 1
    ACS_URCORNER = 1
    ACS_VLINE = 1
    COLOR_BLACK = 1
    COLOR_BLUE = 1
    COLOR_CYAN = 1
    COLOR_GREEN = 1
    COLOR_MAGENTA = 1
    COLOR_RED = 1
    COLOR_WHITE = 1
    COLOR_YELLOW = 1
        """
    )


def register(manager: AstroidManager) -> None:
    register_module_extender(manager, "curses", _curses_transform)
