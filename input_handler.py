from pynput.keyboard import Key, Listener


class InputHandler():
    def __init__(self):
        self._key_listener = Listener(on_press=self.process_inputs)

        self.commands = dict()

    def process_inputs(self, key):
        try:
            for command in self.commands[key]:
                command()
        except: pass

        print(key, "pressed")

    def attach_func_to_keypress(self, key, func):
        if key in self.commands.keys():
            self.commands[key].append(func)
        else:
            self.commands[key] = [func]