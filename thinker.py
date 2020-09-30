import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# If button clicked
def on_button_clicked(button):
	print("Speed: ",int(speed_scale.get_value()))
	print("Accel: ",int(accel_scale.get_value()))

# Start builder
builder = Gtk.Builder()
builder.add_from_file("layout.glade")

# Import widgets from Glade
win = builder.get_object("win")
box = builder.get_object("box")
speed_scale = builder.get_object("speed_scale")
accel_scale = builder.get_object("accel_scale")
button = builder.get_object("button")
button.connect("clicked", lambda x: on_button_clicked(button))

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()