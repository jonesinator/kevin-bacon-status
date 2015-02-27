# kevin-bacon-status
A python application that displays whether or not Kevin Bacon is alive or dead.

# Usage
This is being designed to be an application that runs continuously on a
Raspberry Pi connected to a display. The user must obtain his or her own images.
Three images are required for the script to function properly:

1. kevin-bacon-alive.jpg
2. kevin-bacon-dead.jpg
3. kevin-bacon-unknown.jpg

On Raspbian the python-imaging-tk package must be installed via:

    sudo apt-get install python-imaging-tk

Once the prerequisites have been installed and the image files are placed in the
same directory as the script, the script can be invoked by:

    python kevin-bacon-status.py
