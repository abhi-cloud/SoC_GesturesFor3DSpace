import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
	def __init__(self, title):
		Gtk.Window.__init__(self, title=title)

		grid = Gtk.Grid()
		self.add(grid)

		button1 = Gtk.Button(label="Button {}".format(title))
		button2 = Gtk.Button(label="Button 2")
		button3 = Gtk.Button(label="Button 3")
		button4 = Gtk.Button(label="Button 4")
		button5 = Gtk.Button(label="Button 5")
		button6 = Gtk.Button(label="Button 6")

		button1.connect('clicked', self.button_clicked)

		grid.add(button1)
		grid.attach(button2, 1, 0, 2, 1)
		grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
		grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
		grid.attach(button5, 1, 2, 1, 1)
		grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

	def button_clicked(self, widget):
		print('You clicked {} on {}'.format(self.get_properties('title')[0], widget.get_properties('label')[0]))

win = GridWindow('One')
win2 = GridWindow('Two')
win.connect('delete-event', Gtk.main_quit)
# win2.connect('delete-event', gtk.main_quit)

win2.show_all()
win.show_all()
Gtk.main()