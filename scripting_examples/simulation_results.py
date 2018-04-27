import numpy as np
import orhelper
from random import gauss
import math
from matplotlib import pyplot as plt
import sys

with orhelper.OpenRocketInstance("C:\Users\metamorph\Documents\OpenRocket_test.jar"):
    # opens Open Rocket, runs simulation, and outputs common flight metrics
    orh = orhelper.Helper()

    # Load document
    doc = orh.load_doc("..\ork_files\simple.ork")

    # Run second OpenRocket simulation (first sim has a faulty motor)
    sim = doc.getSimulation(0)
    print sim.getStatus()
    # Randomize various parameters
    opts = sim.getOptions()
    rocket = opts.getRocket()

    arguments = sys.argv;
    if(len(sys.argv) == 3):
        num = int(sys.argv[1])
        plotResults = sys.argv[2]
    elif(len(sys.argv) == 2):
        num = int(sys.argv[1])
        plotResults = ''
    else:
        num = 10
        plotResults = ''

    baseWindSpeed = 5.0 # m/s
    windSpeedInc = 2.0 # m/s

    print "Random Seed is %d" %opts.getRandomSeed()
    opts.setRandomSeed(0)
    print "Random Seed is %d" %opts.getRandomSeed()

    # Run num simulations and add to self
    for p in range(int(num)):
        print "\n------------------------------------------"
        print 'Running simulation ', p
        print "Random Seed is %d" %opts.getRandomSeed()

        # opts.setLaunchRodAngle(math.radians( gauss(45, 5) ))    # 45 +- 5 deg in direction
        # opts.setLaunchRodDirection(math.radians( gauss(0, 5) )) # 0 +- 5 deg in direction

        windSpeed = baseWindSpeed + p*windSpeedInc
        print "Wind Speed: %.3f" % windSpeed
        opts.setWindSpeedAverage( windSpeed )                # 15 +- 5 m/s in wind

        # for component_name in ('Nose cone', 'Body tube'):       # 5% in the mass of various components
        #     component = orh.get_component_named( rocket, component_name )
        #     mass = component.getMass()
        #     component.setMassOverridden(True)
        #     component.setOverrideMass( mass * gauss(1.0, 0.05) )

        orh.run_simulation(sim)

        # get flight data
        flightData = sim.getSimulatedData()
        print "Max Velocity: %.3f" % flightData.getMaxVelocity()
        print "Max Altitude: %.3f" % flightData.getMaxAltitude()
        print "Max Acceleration: %.3f" % flightData.getMaxAcceleration()
        print "Max Mach: %.3f" % flightData.getMaxMachNumber()
        print "Ground Hit Velocity: %.3f" % flightData.getGroundHitVelocity()
        print "Launch Rod Velocity: %.3f" % flightData.getLaunchRodVelocity()
        print "Flight Time: %.3f" % flightData.getFlightTime()

        print "------------------------------------------"

        data = orh.get_timeseries(sim, ['Time', 'Altitude', 'Vertical velocity'] )
        events = orh.get_events(sim)

        # Make a custom plot the simulation
        if(plotResults == "-p"):
            events_to_annotate = ['Motor burnout', 'Apogee', 'Launch rod clearance']
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax2 = ax1.twinx()

            plt.title('Simulation %d' % p)
            ax1.plot(data['Time'], data['Altitude'], 'b-')
            ax2.plot(data['Time'], data['Vertical velocity'], 'r-')
            ax1.set_xlabel('Time (s)')
            ax1.set_ylabel('Altitude (m)', color='b')
            ax2.set_ylabel('Vertical Velocity (m/s)', color='r')
            change_color = lambda ax, col : [x.set_color(col) for x in ax.get_yticklabels()]
            change_color(ax1, 'b')
            change_color(ax2, 'r')

            index_at = lambda t : (np.abs(data['Time']-t)).argmin()
            for name, time in events.items():
                if not name in events_to_annotate: continue
                ax1.annotate(name, xy=(time, data['Altitude'][index_at(time)] ), xycoords='data',
                            xytext=(20, 0), textcoords='offset points',
                            arrowprops=dict(arrowstyle="->", connectionstyle="arc3")
                            )

            ax1.grid(True)
            plt.show()
