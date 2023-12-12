import os
import sys
import time
from datetime import datetime

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
import traci

sumoBinary = "sumo-gui"
sumoCmd = [sumoBinary, "-c", "cloud.sumocfg"]

traci.start(sumoCmd)

# ACCEL_THLD = 4.5
# vhcle_map = {}
# num_step = 0
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
traci.close()

