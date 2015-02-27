import Tkinter
import urllib2
from PIL import Image, ImageTk

def update():
    html = urllib2.urlopen('http://www.deadoraliveinfo.com/dead.Nsf/bnames/Bacon+Kevin').read()
    if 'alive-record' in html:
        panel.config(image = aliveImage)
        button.config(text='Kevin Bacon is Alive.')
    elif 'dead-record' in html:
        panel.config(image = deadImage)
        button.config(text='Kevin Bacon is Dead.')
    else:
        panel.config(image = unknownImage)
        button.config(text='The status of Kevin Bacon is unknown.')
    root.after(5000, update)

root = Tkinter.Tk()
root.title('Kevin Bacon Status')
aliveImage = ImageTk.PhotoImage(Image.open('kevin-bacon-alive.jpg'))
deadImage = ImageTk.PhotoImage(Image.open('kevin-bacon-dead.jpg'))
unknownImage = ImageTk.PhotoImage(Image.open('kevin-bacon-unknown.jpg'))
widths = [aliveImage.width(), deadImage.width(), unknownImage.width()]
heights = [aliveImage.height(), deadImage.height(), unknownImage.height()]
root.geometry("%dx%d+%d+%d" % (max(widths), max(heights), 0, 0))
panel = Tkinter.Label(root, image=aliveImage)
panel.pack(side='top', fill='both', expand='yes')
button = Tkinter.Button(panel)
button.pack(side='bottom')
update()
root.mainloop()
