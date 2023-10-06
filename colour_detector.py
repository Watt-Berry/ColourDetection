# create class to detect a certain colour from image and return coordinates
import asyncio


class ColourDetector:
    def __init__(self):
        # public so any outside code should be able to add an image to it
        self.image_to_process = None
        self._keep_running = False

        self._run_method = None

    #the property is public whereas the variable is private otherwise the setter will vause an infinite loop
    @property
    def keep_running(self):
        return self._keep_running

    #call the _run method when keep_running is set to true and cancel when false
    @keep_running.setter
    def keep_running(self, value: bool):
        self._keep_running = value
        if value:
            print("run loop started")
            self._run_method = asyncio.ensure_future(self._run())
        else:
            print("run loop stopped")
            self._run_method.cancel()


    # ProcessImage shouldn't be async as otherwise it might return variables with no value
    # should return maps of the image outlining each specific colour
    def process_image(self) -> None:
        # get colour maps
        self.image_to_process = None
        return None

    #should not be called from outside the class as its private, the program should only change the keep_running
    #value and whenever that is changed _run will run if true and cancel if false
    async def _run(self):
        self.keep_running = True
        loopI = 1
        while self.keep_running:
            if self.image_to_process:
                colour_maps = self.process_image()
            await asyncio.sleep(1)

            print("loop", loopI, "done")
            loopI += 1