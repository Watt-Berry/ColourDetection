# create class to detect a certain colour from image and return coordinates
import asyncio
from pynput.keyboard import Key, Listener


class ColourDetector:
    def __init__(self, camera):
        # public so any outside code should be able to add an image to it
        self.image_to_process = None
        # keyboard should directly alter whether r or q where pressed
        self._quit = False
        # start the listener to continually check for key presses in the background and update values
        key_listener = Listener(on_press=self.process_inputs)
        key_listener.start()

        # create a reference to the pseudo-forever loop
        #self.forever_loop = asyncio.ensure_future(self.keep_looping())
        asyncio.get_event_loop().run_until_complete(self.keep_looping())
        self.intro_message()

    def intro_message(self):
        print("Press enter to run the detector")
        print("Press esc to exit the detector")

    # ProcessImage shouldn't be async as otherwise it might return variables with no value
    # should return maps of the image outlining each specific colour
    def process_image(self) -> None:
        # get colour maps
        self.image_to_process = None
        return None

    def process_inputs(self, key):
        if key == Key.enter:
            # self._quit = False
            # start the pseudo-forever loop
            # try:
            #    self.forever_loop.uncancel()
            # except: pass
            asyncio.get_event_loop().run_until_complete(self.keep_looping())
        elif key == Key.esc:
            # self._quit = True
            # try:
            #    self.forever_loop.cancel()
            # except: pass
            asyncio.get_event_loop().close()
        print(key, "was pressed")

    async def keep_looping(self):
        # keep looping and waiting for any images or an exit command
        # on q pressed exit
        loopI = 1
        while not self._quit:
            # check if any image has been added and if so process it then set the image back to None
            if self.image_to_process:
                colour_maps = self.process_image()
            await asyncio.sleep(1)

            print("loop", loopI, "done")
            loopI += 1


detector = ColourDetector(None)
