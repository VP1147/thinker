import sys, gi, os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# # Fetch values from the system
# def fetch():
# 	with open(sys.argv[1], "r") as sens:
# 		s1 = int(sens.read())
# 	with open(sys.argv[2], "r") as speed:
# 		s2 = int(speed.read())
# 	return s1, s2

# If set_button clicked

DEVICE = sys.argv[1]

def on_set(set_button):
	os.system("xinput set-prop "+DEVICE+" 'libinput Accel Speed' "+str(accel_scale.get_value()/100))

# Start builder
builder = Gtk.Builder()
builder.add_from_file("layout.glade")

# Import widgets from Glade
win = builder.get_object("win")
box = builder.get_object("box")

# Scales
accel_scale = builder.get_object("accel_scale")
accel_scale.set_value(50)

# Buttons
set_button = builder.get_object("set_button")
set_button.connect("clicked", lambda x: on_set(set_button))

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()