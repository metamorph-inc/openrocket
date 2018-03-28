# Simple demonstration of running an OpenRocket simulation from a python script
# Prints the event/time pairs from the simulation
# Tested with jpype 0.5.4.2 and java 6.0

import sys, traceback
import numpy as np
import orhelper
import time
from jpype import *

orhelper.OpenRocketInstance('..\OpenRocket.jar')
orh = orhelper.Helper()

# Load document, run simulation and get events

doc1 = orh.load_doc('..\ork_files\simple.ork')
sim1 = doc1.getSimulation(1)
events1 = orh.get_events(sim1)

print "\nEvents #1"
print events1

doc2 = orh.load_doc('..\ork_files\\rollStabilizedRocket.ork')
sim2 = doc2.getSimulation(0)
events2 = orh.get_events(sim2)

print "\nEvents #2"
print events2
