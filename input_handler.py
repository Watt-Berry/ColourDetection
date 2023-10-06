import asyncio

from pynput.keyboard import Key, Listener


class InputHandler():
    def __init__(self):
        # define a listener and start it
        self._key_listener = Listener(on_press=self._process_inputs)
        self._key_listener.start()

        self.commands = dict()

    def _process_inputs(self, key):
        print(key, "pressed")
        try:
            for command in self.commands[key]:
                command()
        except:
            # if no commands present then add in an empty key-value pair for future commands
            self.commands[key] = []

        print(self.commands)

    def attach_func_to_keypress(self, key, func):
        # add space to the values and reassign the last value to the function
        if key in self.commands.keys():
            self.commands[key].append(None)
        else:
            self.commands[key] = [None]
        self.commands[key][-1] = func
