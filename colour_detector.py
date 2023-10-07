# create class to detect a certain colour from image and return coordinates
#import asyncio
import threading
import time


class ColourDetector:
    def __init__(self):
        # public so any outside code should be able to add an image to it
        self.received_image = None
        # for checking whether to keep running or to stop
        self._keep_running = False

        self._thread = threading.Thread(target=self._run(), name="COLOUR_DETECT")
        self._thread.setName("COLOUR_DETECT")
        self._thread.setDaemon(True)

        self._keep_running = threading.local()

        print(threading.active_count())
        print(threading.current_thread())
        print(threading.enumerate())

    # the property is public whereas the variable is private otherwise the setter will cause an infinite loop
    @property
    def keep_running(self):
        return self._keep_running

    # call the _run method when keep_running is set to true and cancel when false
    @keep_running.setter
    def keep_running(self, value: bool):
        self._keep_running = value
        if value:
            print("run loop started")
            self._thread.start()
        else:
            print("run loop stopped")
            self._thread.join()


    # ProcessImage shouldn't be async as otherwise it might return variables with no value
    # should return maps of the image outlining each specific colour
    def process_image(self) -> None:
        # get colour maps
        self.received_image = None
        return None

    # should not be called from outside the class as its private, the program should only change the keep_running
    # value and whenever that is changed _run will run if true and cancel if false
    def _run(self):
        print("a")
        while self._keep_running:
            print("is looping")
            if self.received_image:
                # get colour maps and return the values
                colour_maps = self.process_image()
            time.sleep(1)