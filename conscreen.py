# libconscreen
# Screen controller (Linux only)

from os import get_terminal_size, system, name
from colored import bg, attr
from cursor import hide, show
import termios

columns, lines = get_terminal_size()  # Get terminal size to draw everything correctly


def set_echo(enabled):
    """Tells the terminal if it should echo input.
    Used internally.
    """
    (iflag, oflag, cflag, lflag, ispeed, ospeed, cc) \
        = termios.tcgetattr(0)

    if enabled:
        lflag |= termios.ECHO
    else:
        lflag &= ~termios.ECHO

    new_attr = [iflag, oflag, cflag, lflag, ispeed, ospeed, cc]
    termios.tcsetattr(0, termios.TCSANOW, new_attr)


def clear():
    """Clears the screen.
    Used internally"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def revert_x_to_y(screen):
    """Reverts an column based 2D array to a line based 2D array.
    Used internally."""
    reverted = [[' ']*columns for _ in range(lines - 1)]
    for i in range(len(screen.screen)):
        for n in range(len(screen.screen[i])):
            reverted[n][i] = screen.screen[i][n]
    return reverted


class Screen:
    """Screen object.
    Used for controlling the screen.
    The creation of this object takes no arguments.
    You should only create one for every session, then take over the screen with take_over()
    Update the screen with update() and return the screen with return_over()
    Properties:
        Format: name: type: description

        screen: list: Screen data by individual characters
        is_active: bool: Shows if the screen is active
    Functions:
        Format: name: return_type: description

        drawbg: None: Draws a dark gray background. Used internally.
        take_over: None: Takes over the terminal for the screen object.
        update: None: Updates the screen.
        return_over: None: Returns the screen to the terminal.
        draw: None: Receives a Drawable object and renders it onto the array.
                    Call update() to actually put the object on screen.
    """
    def __init__(self):
        self.screen = [[' ']*(lines - 1) for _ in range(columns)]
        self.objects = []  # TODO
        self.is_active = False

    def drawbg(self):
        print(bg("dark_gray"), end="")

    def take_over(self):
        clear()
        self.is_active = True
        self.drawbg()
        hide()
        set_echo(False)
        reverted = revert_x_to_y(self)
        for i in reverted:
            print("".join(i))

    def update(self):
        if self.is_active is False:
            raise Exception("Screen must be active to update")
        clear()
        self.drawbg()
        reverted = revert_x_to_y(self)
        for i in reverted:
            print("".join(i))

    def return_over(self):
        self.is_active = False
        print(attr('reset'))
        show()
        set_echo(True)
        clear()

    def draw(self, obj):
        if not isinstance(obj, Drawable):
            raise Exception("obj must be of type Drawable or inheritent thereof")
        obj.draw_on(self)


class Drawable:
    """Base class for objects that can be drawn with Screen.draw()
    Each object that will be drawn on the screen must be a member of this class,
    and must have a draw_on() method that receives a Screen and modifies it.
    This class should not be created directly, but rather be inherited from
    another class.

    Properties:
        x: int: X position of the object
        y: int: Y position of the object
        width: int: The width of the object
        height: int: The height of the object
    These properties above should be modified by the inherited class to suit
    your needs by either calling super().__init__ or modifying it directly.

    Functions:
        set_location: None: Sets the location to the X and Y position provided.
    """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def set_location(self, x, y):
        self.x = x
        self.y = y


class Text(Drawable):
    def __init__(self, x, y, text):
        super().__init__(x, y, len(text), len(text.split("\n")))
        self.text = text

    def draw_on(self, screen):
        column = self.x
        line = self.y
        for i in self.text.split("\n"):
            for x in list(i):
                screen.screen[column][line] = x
                column += 1
            line += 1
        return None
