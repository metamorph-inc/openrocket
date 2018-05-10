# Simple demonstration of running an OpenRocket simulation from a Python script
# Prints the event/time pairs from the simulation
# Tested with jpype 0.5.4.2 and Java 8.0
# Note: this script should be run from the same folder as the .ork and openmeta-OpenRocket.jar

import sys, traceback
import numpy as np
import orhelper
import time
from jpype import *

# instantiate OpenRocket
orhelper.OpenRocketInstance('OpenRocket.jar')
# create instance of OpenRocket Helper class
orh = orhelper.Helper()

# Load document, run simulation and get events
doc = orh.load_doc('simple.ork') # replace this with your .ork
sim = doc.getSimulation(1)
events = orh.get_events(sim)

print "\nSimulation Events"
print events
