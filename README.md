# lib
This is a library with many things you may need.

How to make a BadUSB with this repository and a Raspberry Pi Pico
-----------------------------------------------------------------
1. Hold the BOOTSEL button on your Raspberry Pi Pico while plugging in into a PC/Laptop.
2. Copy and paste (or drag and drop) the circuitpython-us-10.0.3-uf2 to the Raspberry Pi Pico. It will disconnect. After some seconds, it will connect again as 'CIRCUITPY'.
3. You will see some folders and files on the CIRCUITPY. You should see the folder 'lib' too. Put the 'adafruit_hid' folder into the lib folder of the Pico.
4. Replace the code of code.py with the code of my self-written code.py.
5. Create a boot.py (if it doesn't exist) and put the code of my boot.py in it (WARNING: The seconds you do this crucial step, your Raspberry Pi Pico will execute code.py (for this code.py, it will pretend that it is an filesystem updater, and then, it will rickroll you)).
6. More information what the code will do: It will do nothing for 2 seconds, then, it opens a Terminal and sets your keyboard layout to US, then, it pretends to be a filesystem updater (feels real, honestly). After that (if you press keys, it may fail), it creates cache-cleaner.sh (NOT a cache cleaner, a rickroll script) and runs it. 
7. Have fun and do not do illegal stuff with it (as example, using it on PCs that you do not own without the owners clear permission).
-----------------------------------------------------------------
