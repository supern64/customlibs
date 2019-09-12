# GTimer
# Global timer intervals

from pyee import BaseEventEmitter
import threading
import ctypes
import time

class GlobalTimer():
    """A global timer object.
    Properties:
        interval: The interval which increases the timer and counts as a tick.
        ticks: The amount of ticks that passed in the timer.
        triggers: A list of triggers registered.
        events: A pyee.BaseEventEmitter used for top layer events.
    Events:
        You can register to an event with @self.events.on(event_name) or self.events.on(event_name, function)
        tick: Triggers on each tick of the clock.
        trigger: Triggers when any triggers are triggered.
        Arguments:
            trigger: The trigger triggered
    """
    def __init__(self, interval=0.1):
        """Initializes global timer.
        interval: The time between each timer tick."""
        self.interval = interval
        self.ticks = 0
        self.timer = 0
        self.triggers = []
        self.events = BaseEventEmitter()
        self._delete_triggers = []
        self._internal_events = BaseEventEmitter()
        self._internal_events.on('tick', self._ontick)
        self._thread = threading.Thread(name='tick', target=self._thread_tick)
    def _thread_tick(self):
        """Thread only! Counts each tick."""
        while True:
            self.ticks = self.ticks + 1
            self.timer = self.timer + self.interval
            self._internal_events.emit('tick')
            time.sleep(self.interval)
    def _get_id(self): 
        # returns id of the respective thread 
        if hasattr(self._thread, '_thread_id'): 
            return self._thread._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self._thread: 
                return id
    def _raise_exception(self): 
        thread_id = self._get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 
    def _ontick(self):
        """Function to calculate intervals on each tick."""
        self.events.emit("tick")
        if self.triggers != []:
            for i in self.triggers:
                if i.interval_type == "interval":
                    if i.type == "every":
                        if round(self.timer, 5) % i.interval == 0:
                            self.events.emit("trigger", i)
                    elif i.type == "only":
                        if round(self.timer, 5) == i.interval:
                            self.events.emit("trigger", i)
                            self._delete_triggers.append(i)
                    else:
                        raise Exception("Should never be here")
                elif i.interval_type == "tick":
                    if i.type == "every":
                        if self.ticks % i.interval == 0:
                            self.events.emit("trigger", i)
                    elif i.type == "only":
                        if self.ticks == i.interval:
                            self.events.emit("trigger", i)
                            self._delete_triggers.append(i)
                    else:
                        raise Exception("Should never be here")                            
            for i in self._delete_triggers:
                if i in self.triggers:
                    self.triggers.remove(i)
    def start(self):
        """Starts the global timer."""
        self._thread.start()
    def stop(self):
        """Stops the global timer."""
        self._raise_exception()
    def add_interval_trigger(self, interval, name, type="every"):
        """Adds an interval type trigger. Counts by the seconds on the timer. Less accurate and works worse.
        interval: The amount of time this trigger requires to trigger. Works depend on type attribute.
        name: A name for the interval trigger
        type: The type of the trigger. MUST be set to either 'every' or 'only'
              every: Trigger every X seconds
              only: Trigger only when timer is X seconds"""
        if type != "every" and type != "only":
            raise IntervalTypeNotValid("Interval type MUST be either 'every' or 'only'")
        trigger = _IntervalTrigger(interval, type, "interval", name)
        self.triggers.append(trigger)
    def add_tick_trigger(self, tick, name, type="every"):
        """Adds an tick type trigger. Counts by when the timer ticks. More accurate and works better.
        interval: The amount of ticks this trigger requires to trigger. Works depend on type attribute.
        name: A name for the interval trigger
        type: The type of the trigger. MUST be set to either 'every' or 'only'
              every: Trigger every X ticks
              only: Trigger only when X ticks have passed"""
        if type != "every" and type != "only":
            raise IntervalTypeNotValid("Interval type MUST be either 'every' or 'only'")
        trigger = _IntervalTrigger(tick, type, "tick", name)
        self.triggers.append(trigger)
    def remove_trigger(self, name):
        """Removes a trigger.
        name: The name of the trigger you wish to remove."""
        to_remove = next((x for x in self.triggers if x.name == name), None)
        if to_remove == None:
            raise TriggerNotFound("Trigger name not found. Maybe a typo?")
        self.triggers.remove(to_remove)
        
class _IntervalTrigger():
    """An object type for triggers. Not intended for out of module use."""
    def __init__(self, interval, type, interval_type, name):
        self.interval = interval
        self.type = type
        self.interval_type = interval_type
        self.name = name


class IntervalTypeNotValid(Exception):
    pass

class TriggerNotFound(Exception):
    pass
