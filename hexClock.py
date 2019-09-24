from Tkinter import *
import time
import threading

class Application(Frame):
    """docstring for Application."""
    def __init__(self, master):
        self.master=master
        Frame.__init__(self, self.master)
        self.exitPoint = False
        self.t = threading.Thread(target=self.clock)
        self.t.start()

    def clock(self):
        while not self.exitPoint:
            startTime = time.time()
            hexColor = time.strftime("%H%M%S")
            print startTime # DEBUG: 
            self.master.configure(background="#%s"%hexColor)
            time.sleep(1-(time.time()-startTime))

root = Tk()
app = Application(master=root)
app.mainloop()
app.exitPoint = True
app.t.join(timeout=None)
