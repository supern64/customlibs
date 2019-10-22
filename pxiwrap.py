import pyxinput
from enum import Enum
import time

class Buttons(Enum):
    A = "A"
    B = "B"
    X = "X"
    Y = "Y"
    BACK = "Back"
    MENU = "Back"
    START = "Start"
    THUMB_LEFT = "ThumbL"
    THUMB_RIGHT = "ThumbR"
    SHOULDER_LEFT = "ShoulderL"
    SHOULDER_RIGHT = "ShoulderR"

class DpadDirection(Enum):
    UP = pyxinput.virtual_controller.vController.DPAD_UP
    LEFT = pyxinput.virtual_controller.vController.DPAD_LEFT
    RIGHT = pyxinput.virtual_controller.vController.DPAD_RIGHT
    DOWN = pyxinput.virtual_controller.vController.DPAD_DOWN

class TriggerStickDirection(Enum):
    LEFT = "L"
    RIGHT = "R"

class TriggerValue(Enum):
    FULL = 1.0
    PARTIAL = 0.5
    NONE = 0

class StickValue(Enum):
    LEFT = UP = -1.0
    PARTIAL_LEFT = PARTIAL_UP = -0.5
    CENTER = 0
    RIGHT = DOWN = 1.0
    PARTIAL_RIGHT = PARTIAL_DOWN = 0.5

class vConWrapper:
    def __init__(self):
        self.controller = pyxinput.vController()
    def __del__(self):
        self.controller.UnPlug()
    def button(self, button):
        if not isinstance(button, str):
            button = button.value
        self.controller.set_value("Btn" + button, 1)
        time.sleep(0.2)
        self.controller.set_value("Btn" + button, 0)
    def dpad(self, direction):
        if not isinstance(direction, int):
            direction = direction.value
        self.controller.set_value("Dpad", direction)
        time.sleep(0.2)
        self.controller.set_value("Dpad", 0)
    def trigger(self, trigger, value):
        if not isinstance(trigger, str):
            trigger = trigger.value
        if not isinstance(value, float) and not isinstance(value, int):
            value = value.value
        self.controller.set_value("Trigger" + trigger, value)
        time.sleep(0.2)
        self.controller.set_value("Trigger" + trigger, 0)
    def axis(self, stick, axis, value, hold=False, hold_duration=1.0):
        if not isinstance(stick, str):
            stick = stick.value
        if axis != "x" and axis != "y":
            raise Exception("'axis' must be 'x' or 'y'")
        if not isinstance(value, float) and not isinstance(value, int):
            value = value.value
        self.controller.set_value("Axis" + stick + axis, value)
        if hold is True:
            time.sleep(hold_duration)
        else:
            time.sleep(0.2)
        self.controller.set_value("Axis" + stick + axis, 0)
