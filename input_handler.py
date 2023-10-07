import threading
from pynput.keyboard import Listener


class InputHandler:
    def __init__(self):
        # public dictionary of commands that each key press will have
        self.commands = dict()

        self._key_listener = Listener(on_press=self._process_inputs)
        self._key_listener.start()
        print(threading.active_count())
        print(threading.current_thread())

    def _process_inputs(self, key):
        print(key, "pressed")
        try:
            for command in self.commands[key]:
                print(command.__name__)
                command()
        except: pass

    def attach_func_to_keypress(self, key, func):
        # add space to the values and reassign the last value to the function
        if key in self.commands.keys():
            self.commands[key].append(None)
        else:
            self.commands[key] = [None]
        self.commands[key][-1] = func
