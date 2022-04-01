import tkinter
import gravity

# Sets the size of the simulation environment
sizeX = 1000
sizeY = 1000

# Makes the window
root = tkinter.Tk()
root.title('GravitySim')


def app(canvas):
    canvas.delete("all")
    gravity.simulation(c)
    root.after(25, lambda: app(canvas))


c = tkinter.Canvas(root, width=sizeX, height=sizeY, bd=5, bg="white")
c.grid(row=0, column=0)
gravity.initialize()
app(c)

root.mainloop()
