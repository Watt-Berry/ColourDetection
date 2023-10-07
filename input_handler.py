import asyncio

import keyboard


class InputHandler:
    def __init__(self):
        # public dictionary of commands that each key press will have
        self.commands = dict()
        self.recent_key = None

        self._keep_running = False

        self._loop = asyncio.get_event_loop()

    @property
    def keep_running(self):
        return self._keep_running

    @keep_running.setter
    def keep_running(self, value):
        self._keep_running = value
        if value:
            self._loop.create_task(self.check_for_inputs())
            #self._loop.run_until_complete(asyncio.ensure_future(self.check_for_inputs()))
        if not value:
            self._loop.stop()

    async def check_for_inputs(self):
        while self._keep_running:
            for key_check in self.commands.keys():
                if keyboard.is_pressed(key_check): self._process_inputs(key_check)
            await asyncio.sleep(1)

    def _process_inputs(self, key):
        try:
            for command in self.commands[key]:
                command()
        except: pass
        self.recent_key = key

        print(key, "pressed")
        print(self.commands)

    def attach_func_to_keypress(self, key, func):
        # add space to the values and reassign the last value to the function
        if key in self.commands.keys():
            self.commands[key].append(None)
        else:
            self.commands[key] = [None]
        self.commands[key][-1] = func
