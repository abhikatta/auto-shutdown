import os
import datetime
from tkinter import Tk, messagebox


class Shutdown:
    @staticmethod
    def shutdown(time: int):
        os.system('shutdown /s /t %s' % time)

    @staticmethod
    def main(shutdown_time: int):
        root = Tk()
        root.withdraw()
        while True:
            time = datetime.datetime.now()
            if (time.hour >= 22 and time.minute >= 45):
                t = f"{time.hour} : {time.minute}"
                messagebox.showinfo(
                    'Go to sleep!', 'Shutdown in 15 minute as time is %s, save everything now!' % (t))
                Shutdown.shutdown(shutdown_time)
            time.sleep(60)


if __name__ == '__main__':
    Shutdown.main(15 * 60)
