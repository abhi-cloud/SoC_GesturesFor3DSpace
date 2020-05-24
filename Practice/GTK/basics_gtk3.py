import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

class MainWindow(gtk.Window):

	def __init__(self, title):
		gtk.Window.__init__(self, title=title)

		# Box
		self.b = gtk.Box(spacing=100)
		self.add(self.b)

		self.label = gtk.Label()
		self.label.set_label('How u doin!')
		self.label.set_angle(45)
		self.set_halign(gtk.Align.END)
		# self.label.connect('clicked', self.button_clicked)
		self.b.pack_start(self.label, True, True, 0)

		# print(self.label.get_properties('angle'))

		self.button = gtk.Button(label='CLick Here!')
		self.button.connect('clicked', self.button_clicked)
		self.b.pack_start(self.button, True, True, 0)


	def button_clicked(self, widget):
		print('You clicked {} on {}'.format(self.get_properties('title')[0], widget.get_properties('label')[0]))

win = MainWindow('One')
win2 = MainWindow('Two')
win.connect('delete-event', gtk.main_quit)
# win2.connect('delete-event', gtk.main_quit)

win2.show_all()
win.show_all()
gtk.main()