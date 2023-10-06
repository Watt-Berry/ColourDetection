from pynput.keyboard import Key, Listener


class InputHandler:
    def __init__(self):
        # define a listener and start it - should always be on as it's used for checking inputs for other cases
        # the listener is a thread itself as well
        self._key_listener = Listener(on_press=self._process_inputs, name="INPUT")
        self._key_listener.start()
        # public dictionary of commands that each key press will have
        self.commands = dict()

    def _process_inputs(self, key):
        try:
            for command in self.commands[key]:
                command()
        except: pass

        print(key, "pressed")
        print(self.commands)

    def attach_func_to_keypress(self, key, func):
        # add space to the values and reassign the last value to the function
        if key in self.commands.keys():
            self.commands[key].append(None)
        else:
            self.commands[key] = [None]
        self.commands[key][-1] = func
