import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Fetch values from the system
def fetch():
	with open(sys.argv[1], "r") as sens:
		s1 = int(sens.read())
	with open(sys.argv[2], "r") as speed:
		s2 = int(speed.read())
	return s1, s2

# If set_button clicked
def on_set(set_button):
	with open(sys.argv[1], "w") as sens:
		sens.write(str(int(sens_scale.get_value())))
	with open(sys.argv[2], "w") as speed:
		speed.write(str(int(speed_scale.get_value())))

# If reset_button clicked
def on_reset(reset_button):
	s1, s2 = fetch()
	sens_scale.set_value(s1)
	speed_scale.set_value(s2)

# Start builder
builder = Gtk.Builder()
builder.add_from_file("layout.glade")

# Import widgets from Glade
win = builder.get_object("win")
box = builder.get_object("box")

# Scales
speed_scale = builder.get_object("speed_scale")
sens_scale = builder.get_object("accel_scale")
s1, s2 = fetch()
sens_scale.set_value(s1)
speed_scale.set_value(s2)

# Buttons
set_button = builder.get_object("set_button")
set_button.connect("clicked", lambda x: on_set(set_button))
reset_button = builder.get_object("reset_button")
reset_button.connect("clicked", lambda x: on_reset(reset_button))

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()