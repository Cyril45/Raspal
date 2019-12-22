import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi 
