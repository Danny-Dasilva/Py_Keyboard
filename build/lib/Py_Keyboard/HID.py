# The MIT License (MIT)

#

"""
`adafruit_hid.keyboard_layout_us.KeyboardLayoutUS`
=======================================================

* Author(s): Dan Halbert
"""
import time




class Keycode:
    
    #pylint: disable-msg=invalid-name
    A = 0x04
    """``a`` and ``A``"""
    B = 0x05
    """``b`` and ``B``"""
    C = 0x06
    """``c`` and ``C``"""
    D = 0x07
    """``d`` and ``D``"""
    E = 0x08
    """``e`` and ``E``"""
    F = 0x09
    """``f`` and ``F``"""
    G = 0x0A
    """``g`` and ``G``"""
    H = 0x0B
    """``h`` and ``H``"""
    I = 0x0C
    """``i`` and ``I``"""
    J = 0x0D
    """``j`` and ``J``"""
    K = 0x0E
    """``k`` and ``K``"""
    L = 0x0F
    """``l`` and ``L``"""
    M = 0x10
    """``m`` and ``M``"""
    N = 0x11
    """``n`` and ``N``"""
    O = 0x12
    """``o`` and ``O``"""
    P = 0x13
    """``p`` and ``P``"""
    Q = 0x14
    """``q`` and ``Q``"""
    R = 0x15
    """``r`` and ``R``"""
    S = 0x16
    """``s`` and ``S``"""
    T = 0x17
    """``t`` and ``T``"""
    U = 0x18
    """``u`` and ``U``"""
    V = 0x19
    """``v`` and ``V``"""
    W = 0x1A
    """``w`` and ``W``"""
    X = 0x1B
    """``x`` and ``X``"""
    Y = 0x1C
    """``y`` and ``Y``"""
    Z = 0x1D
    """``z`` and ``Z``"""

    ONE = 0x1E
    """``1`` and ``!``"""
    TWO = 0x1F
    """``2`` and ``@``"""
    THREE = 0x20
    """``3`` and ``#``"""
    FOUR = 0x21
    """``4`` and ``$``"""
    FIVE = 0x22
    """``5`` and ``%``"""
    SIX = 0x23
    """``6`` and ``^``"""
    SEVEN = 0x24
    """``7`` and ``&``"""
    EIGHT = 0x25
    """``8`` and ``*``"""
    NINE = 0x26
    """``9`` and ``(``"""
    ZERO = 0x27
    """``0`` and ``)``"""
    ENTER = 0x28
    """Enter (Return)"""
    RETURN = ENTER
    """Alias for ``ENTER``"""
    ESCAPE = 0x29
    """Escape"""
    BACKSPACE = 0x2A
    """Delete backward (Backspace)"""
    TAB = 0x2B
    """Tab and Backtab"""
    SPACEBAR = 0x2C
    """Spacebar"""
    SPACE = SPACEBAR
    """Alias for SPACEBAR"""
    MINUS = 0x2D
    """``-` and ``_``"""
    EQUALS = 0x2E
    """``=` and ``+``"""
    LEFT_BRACKET = 0x2F
    """``[`` and ``{``"""
    RIGHT_BRACKET = 0x30
    """``]`` and ``}``"""
    BACKSLASH = 0x31
    r"""``\`` and ``|``"""
    POUND = 0x32
    """``#`` and ``~`` (Non-US keyboard)"""
    SEMICOLON = 0x33
    """``;`` and ``:``"""
    QUOTE = 0x34
    """``'`` and ``"``"""
    GRAVE_ACCENT = 0x35
    r""":literal:`\`` and ``~``"""
    COMMA = 0x36
    """``,`` and ``<``"""
    PERIOD = 0x37
    """``.`` and ``>``"""
    FORWARD_SLASH = 0x38
    """``/`` and ``?``"""

    CAPS_LOCK = 0x39
    """Caps Lock"""

    F1 = 0x3A
    """Function key F1"""
    F2 = 0x3B
    """Function key F2"""
    F3 = 0x3C
    """Function key F3"""
    F4 = 0x3D
    """Function key F4"""
    F5 = 0x3E
    """Function key F5"""
    F6 = 0x3F
    """Function key F6"""
    F7 = 0x40
    """Function key F7"""
    F8 = 0x41
    """Function key F8"""
    F9 = 0x42
    """Function key F9"""
    F10 = 0x43
    """Function key F10"""
    F11 = 0x44
    """Function key F11"""
    F12 = 0x45
    """Function key F12"""

    PRINT_SCREEN = 0x46
    """Print Screen (SysRq)"""
    SCROLL_LOCK = 0x47
    """Scroll Lock"""
    PAUSE = 0x48
    """Pause (Break)"""

    INSERT = 0x49
    """Insert"""
    HOME = 0x4A
    """Home (often moves to beginning of line)"""
    PAGE_UP = 0x4B
    """Go back one page"""
    DELETE = 0x4C
    """Delete forward"""
    END = 0x4D
    """End (often moves to end of line)"""
    PAGE_DOWN = 0x4E
    """Go forward one page"""

    RIGHT_ARROW = 0x4F
    """Move the cursor right"""
    LEFT_ARROW = 0x50
    """Move the cursor left"""
    DOWN_ARROW = 0x51
    """Move the cursor down"""
    UP_ARROW = 0x52
    """Move the cursor up"""

    KEYPAD_NUMLOCK = 0x53
    """Num Lock (Clear on Mac)"""
    KEYPAD_FORWARD_SLASH = 0x54
    """Keypad ``/``"""
    KEYPAD_ASTERISK = 0x55
    """Keypad ``*``"""
    KEYPAD_MINUS = 0x56
    """Keyapd ``-``"""
    KEYPAD_PLUS = 0x57
    """Keypad ``+``"""
    KEYPAD_ENTER = 0x58
    """Keypad Enter"""
    KEYPAD_ONE = 0x59
    """Keypad ``1`` and End"""
    KEYPAD_TWO = 0x5A
    """Keypad ``2`` and Down Arrow"""
    KEYPAD_THREE = 0x5B
    """Keypad ``3`` and PgDn"""
    KEYPAD_FOUR = 0x5C
    """Keypad ``4`` and Left Arrow"""
    KEYPAD_FIVE = 0x5D
    """Keypad ``5``"""
    KEYPAD_SIX = 0x5E
    """Keypad ``6`` and Right Arrow"""
    KEYPAD_SEVEN = 0x5F
    """Keypad ``7`` and Home"""
    KEYPAD_EIGHT = 0x60
    """Keypad ``8`` and Up Arrow"""
    KEYPAD_NINE = 0x61
    """Keypad ``9`` and PgUp"""
    KEYPAD_ZERO = 0x62
    """Keypad ``0`` and Ins"""
    KEYPAD_PERIOD = 0x63
    """Keypad ``.`` and Del"""
    KEYPAD_BACKSLASH = 0x64
    """Keypad ``\\`` and ``|`` (Non-US)"""

    APPLICATION = 0x65
    """Application: also known as the Menu key (Windows)"""
    POWER = 0x66
    """Power (Mac)"""
    KEYPAD_EQUALS = 0x67
    """Keypad ``=`` (Mac)"""
    F13 = 0x68
    """Function key F13 (Mac)"""
    F14 = 0x69
    """Function key F14 (Mac)"""
    F15 = 0x6A
    """Function key F15 (Mac)"""
    F16 = 0x6B
    """Function key F16 (Mac)"""
    F17 = 0x6C
    """Function key F17 (Mac)"""
    F18 = 0x6D
    """Function key F18 (Mac)"""
    F19 = 0x6E
    """Function key F19 (Mac)"""

    LEFT_CONTROL = 0xE0
    """Control modifier left of the spacebar"""
    CONTROL = LEFT_CONTROL
    """Alias for LEFT_CONTROL"""
    LEFT_SHIFT = 0xE1
    """Shift modifier left of the spacebar"""
    SHIFT = LEFT_SHIFT
    """Alias for LEFT_SHIFT"""
    LEFT_ALT = 0xE2
    """Alt modifier left of the spacebar"""
    ALT = LEFT_ALT
    """Alias for LEFT_ALT; Alt is also known as Option (Mac)"""
    OPTION = ALT
    """Labeled as Option on some Mac keyboards"""
    LEFT_GUI = 0xE3
    """GUI modifier left of the spacebar"""
    GUI = LEFT_GUI
    """Alias for LEFT_GUI; GUI is also known as the Windows key, Command (Mac), or Meta"""
    WINDOWS = GUI
    """Labeled with a Windows logo on Windows keyboards"""
    COMMAND = GUI
    """Labeled as Command on Mac keyboards, with a clover glyph"""
    RIGHT_CONTROL = 0xE4
    """Control modifier right of the spacebar"""
    RIGHT_SHIFT = 0xE5
    """Shift modifier right of the spacebar"""
    RIGHT_ALT = 0xE6
    """Alt modifier right of the spacebar"""
    RIGHT_GUI = 0xE7
    """GUI modifier right of the spacebar"""


    @classmethod
    def modifier_bit(cls, keycode):
        """Return the modifer bit to be set in an HID keycode report if this is a
        modifier key; otherwise return 0."""
        return 1 << (keycode - 0xE0) if cls.LEFT_CONTROL <= keycode <= cls.RIGHT_GUI else 0



class Keyboard:

    _MAX_KEYPRESSES = 6
    SHIFT_FLAG = 0x80
    ASCII_TO_KEYCODE = (
        b'\x00'    # NUL
        b'\x00'    # SOH
        b'\x00'    # STX
        b'\x00'    # ETX
        b'\x00'    # EOT
        b'\x00'    # ENQ
        b'\x00'    # ACK
        b'\x00'    # BEL \a
        b'\x2a'    # BS BACKSPACE \b (called DELETE in the usb.org document)
        b'\x2b'    # TAB \t
        b'\x28'    # LF \n (called Return or ENTER in the usb.org document)
        b'\x00'    # VT \v
        b'\x00'    # FF \f
        b'\x00'    # CR \r
        b'\x00'    # SO
        b'\x00'    # SI
        b'\x00'    # DLE
        b'\x00'    # DC1
        b'\x00'    # DC2
        b'\x00'    # DC3
        b'\x00'    # DC4
        b'\x00'    # NAK
        b'\x00'    # SYN
        b'\x00'    # ETB
        b'\x00'    # CAN
        b'\x00'    # EM
        b'\x00'    # SUB
        b'\x29'    # ESC
        b'\x00'    # FS
        b'\x00'    # GS
        b'\x00'    # RS
        b'\x00'    # US
        b'\x2c'    # SPACE
        b'\x9e'    # ! x1e|SHIFT_FLAG (shift 1)
        b'\xb4'    # " x34|SHIFT_FLAG (shift ')
        b'\xa0'    # # x20|SHIFT_FLAG (shift 3)
        b'\xa1'    # $ x21|SHIFT_FLAG (shift 4)
        b'\xa2'    # % x22|SHIFT_FLAG (shift 5)
        b'\xa4'    # & x24|SHIFT_FLAG (shift 7)
        b'\x34'    # '
        b'\xa6'    # ( x26|SHIFT_FLAG (shift 9)
        b'\xa7'    # ) x27|SHIFT_FLAG (shift 0)
        b'\xa5'    # * x25|SHIFT_FLAG (shift 8)
        b'\xae'    # + x2e|SHIFT_FLAG (shift =)
        b'\x36'    # ,
        b'\x2d'    # -
        b'\x37'    # .
        b'\x38'    # /
        b'\x27'    # 0
        b'\x1e'    # 1
        b'\x1f'    # 2
        b'\x20'    # 3
        b'\x21'    # 4
        b'\x22'    # 5
        b'\x23'    # 6
        b'\x24'    # 7
        b'\x25'    # 8
        b'\x26'    # 9
        b'\xb3'    # : x33|SHIFT_FLAG (shift ;)
        b'\x33'    # ;
        b'\xb6'    # < x36|SHIFT_FLAG (shift ,)
        b'\x2e'    # =
        b'\xb7'    # > x37|SHIFT_FLAG (shift .)
        b'\xb8'    # ? x38|SHIFT_FLAG (shift /)
        b'\x9f'    # @ x1f|SHIFT_FLAG (shift 2)
        b'\x84'    # A x04|SHIFT_FLAG (shift a)
        b'\x85'    # B x05|SHIFT_FLAG (etc.)
        b'\x86'    # C x06|SHIFT_FLAG
        b'\x87'    # D x07|SHIFT_FLAG
        b'\x88'    # E x08|SHIFT_FLAG
        b'\x89'    # F x09|SHIFT_FLAG
        b'\x8a'    # G x0a|SHIFT_FLAG
        b'\x8b'    # H x0b|SHIFT_FLAG
        b'\x8c'    # I x0c|SHIFT_FLAG
        b'\x8d'    # J x0d|SHIFT_FLAG
        b'\x8e'    # K x0e|SHIFT_FLAG
        b'\x8f'    # L x0f|SHIFT_FLAG
        b'\x90'    # M x10|SHIFT_FLAG
        b'\x91'    # N x11|SHIFT_FLAG
        b'\x92'    # O x12|SHIFT_FLAG
        b'\x93'    # P x13|SHIFT_FLAG
        b'\x94'    # Q x14|SHIFT_FLAG
        b'\x95'    # R x15|SHIFT_FLAG
        b'\x96'    # S x16|SHIFT_FLAG
        b'\x97'    # T x17|SHIFT_FLAG
        b'\x98'    # U x18|SHIFT_FLAG
        b'\x99'    # V x19|SHIFT_FLAG
        b'\x9a'    # W x1a|SHIFT_FLAG
        b'\x9b'    # X x1b|SHIFT_FLAG
        b'\x9c'    # Y x1c|SHIFT_FLAG
        b'\x9d'    # Z x1d|SHIFT_FLAG
        b'\x2f'    # [
        b'\x31'    # \ backslash
        b'\x30'    # ]
        b'\xa3'    # ^ x23|SHIFT_FLAG (shift 6)
        b'\xad'    # _ x2d|SHIFT_FLAG (shift -)
        b'\x35'    # `
        b'\x04'    # a
        b'\x05'    # b
        b'\x06'    # c
        b'\x07'    # d
        b'\x08'    # e
        b'\x09'    # f
        b'\x0a'    # g
        b'\x0b'    # h
        b'\x0c'    # i
        b'\x0d'    # j
        b'\x0e'    # k
        b'\x0f'    # l
        b'\x10'    # m
        b'\x11'    # n
        b'\x12'    # o
        b'\x13'    # p
        b'\x14'    # q
        b'\x15'    # r
        b'\x16'    # s
        b'\x17'    # t
        b'\x18'    # u
        b'\x19'    # v
        b'\x1a'    # w
        b'\x1b'    # x
        b'\x1c'    # y
        b'\x1d'    # z
        b'\xaf'    # { x2f|SHIFT_FLAG (shift [)
        b'\xb1'    # | x31|SHIFT_FLAG (shift \)
        b'\xb0'    # } x30|SHIFT_FLAG (shift ])
        b'\xb5'    # ~ x35|SHIFT_FLAG (shift `)
        b'\x4c'    # DEL DELETE (called Forward Delete in usb.org document)
    )

    def __init__(self):
        """Specify the layout for the given keyboard.

        :param keyboard: a Keyboard object. Write characters to this keyboard when requested.

        Example::

            kbd = Keyboard()
            layout = KeyboardLayoutUS(kbd)
        """
        """Create a Keyboard object that will send USB keyboard HID reports."""
        self.hid_keyboard = None
        # for device in usb_hid.devices:
        #     if device.usage_page == 0x1 and device.usage == 0x06:
        #         self.hid_keyboard = device
        #         break
        # if not self.hid_keyboard:
        #     raise IOError("Could not find an HID keyboard device.")

        # Reuse this bytearray to send keyboard reports.
        self.report = bytearray(8)

        # report[0] modifiers
        # report[1] unused
        # report[2:8] regular key presses

        # View onto byte 0 in report.
        self.report_modifier = memoryview(self.report)[0:1]

        # List of regular keys currently pressed.
        # View onto bytes 2-7 in report.
        self.report_keys = memoryview(self.report)[2:]
        self.keyboard = Keyboard
        # Do a no-op to test if HID device is ready.
        # If not, wait a bit and try once more.
        try:
            self.release_all()
        except OSError:
            print("eror")
            time.sleep(1)
            self.release_all()
        


    def write(self, string):
        """Type the string by pressing and releasing keys on my keyboard.

        :param string: A string of ASCII characters.
        :raises ValueError: if any of the characters are not ASCII or have no keycode
            (such as some control characters).

        Example::

            # Write abc followed by Enter to the keyboard
            layout.write('abc\\n')
        """
        for char in string:
            keycode = self._char_to_keycode(char)
            # If this is a shifted char, clear the SHIFT flag and press the SHIFT key.
            if keycode & self.SHIFT_FLAG:
                keycode &= ~self.SHIFT_FLAG
                self.writer(Keycode.SHIFT)
            self.writer(keycode)
          
            self.release_all()


    def keycodes(self, char):
        """Return a tuple of keycodes needed to type the given character.

        :param char: A single ASCII character in a string.
        :type char: str of length one.
        :returns: tuple of Keycode keycodes.
        :raises ValueError: if ``char`` is not ASCII or there is no keycode for it.

        Examples::

            # Returns (Keycode.TAB,)
            keycodes('\t')
            # Returns (Keycode.A,)
            keycode('a')
            # Returns (Keycode.SHIFT, Keycode.A)
            keycode('A')
            # Raises ValueError because it's a accented e and is not ASCII
            keycode('é')
        """
        keycode = self._char_to_keycode(char)
        if keycode & self.SHIFT_FLAG:
            return (Keycode.SHIFT, keycode & ~self.SHIFT_FLAG)

        return (keycode,)


    def _char_to_keycode(self, char):
        """Return the HID keycode for the given ASCII character, with the SHIFT_FLAG possibly set.

        If the character requires pressing the Shift key, the SHIFT_FLAG bit is set.
        You must clear this bit before passing the keycode in a USB report.
        """
        char_val = ord(char)
        if char_val > 128:
            raise ValueError("Not an ASCII character.")
        keycode = self.ASCII_TO_KEYCODE[char_val]
        if keycode == 0:
            raise ValueError("No keycode available for character.")
        return keycode
    def press(self, keycodes):
        xys = {}
        for string in keycodes.split():
            xys[string] = string
        for a , keycode in Keycode.__dict__.items():
            if a not in xys: continue
            self._add_keycode_to_report(int(keycode))
        send_report(self.report)
        Keyboard.release_all(self)

    def writer(self, *keycodes):

        for keycode in keycodes:
            self._add_keycode_to_report(keycode)
       
        send_report(self.report)

    def release(self, *keycodes):
        
        for keycode in keycodes:
            self._remove_keycode_from_report(keycode)
        self.hid_keyboard.send_report(self.report)
    def release_all(self):
        """Release all pressed keys."""
        for i in range(8):
            self.report[i] = 0
        send_report(self.report)
    def send(self, *keycodes):
        """Press the given keycodes and then release all pressed keys.

        :param keycodes: keycodes to send together
        """
        self.press(*keycodes)
        self.release_all()

    def _add_keycode_to_report(self, keycode):
        """Add a single keycode to the USB HID report."""
        modifier = Keycode.modifier_bit(keycode)
        if modifier:
            # Set bit for this modifier.
            self.report_modifier[0] |= modifier
        else:
            # Don't press twice.
            # (I'd like to use 'not in self.report_keys' here, but that's not implemented.)
            for i in range(self._MAX_KEYPRESSES):
                if self.report_keys[i] == keycode:
                    # Already pressed.
                    return
            # Put keycode in first empty slot.
            for i in range(self._MAX_KEYPRESSES):
                if self.report_keys[i] == 0:
                    self.report_keys[i] = keycode
                    return
            # All slots are filled.
            raise ValueError("Trying to press more than six keys at once.")

    def _remove_keycode_from_report(self, keycode):
        """Remove a single keycode from the report."""
        modifier = Keycode.modifier_bit(keycode)
        if modifier:
            # Turn off the bit for this modifier.
            self.report_modifier[0] &= ~modifier
        else:
            # Check all the slots, just in case there's a duplicate. (There should not be.)
            for i in range(self._MAX_KEYPRESSES):
                if self.report_keys[i] == keycode:
                    self.report_keys[i] = 0
    


# The MIT License (MIT)
#
# Copyright (c) 2017 Dan Halbert
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""
`adafruit_hid.keyboard.Keyboard`
====================================================

* Author(s): Scott Shawcroft, Dan Halbert
"""
def send_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)



    
