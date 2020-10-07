import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Fetch values from the system
def fetch(s1, s2):
	with open(sys.argv[1]+"/sensitivity", "r") as sens:
		s1 = sens.read()
	with open(sys.argv[1]+"/speed", "r") as speed:
		s2 = speed.read()

# If button clicked
def on_button_clicked(button):
	with open(sys.argv[1]+"/sensitivity", "w") as sens:
		sens.write(str(int(sens_scale.get_value())))
	with open(sys.argv[1]+"/speed", "w") as speed:
		speed.write(str(int(speed_scale.get_value())))

# Start builder
builder = Gtk.Builder()
builder.add_from_file("layout.glade")

# Import widgets from Glade
win = builder.get_object("win")
box = builder.get_object("box")
speed_scale = builder.get_object("speed_scale")
sens_scale = builder.get_object("accel_scale")
button = builder.get_object("button")
button.connect("clicked", lambda x: on_button_clicked(button))

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()