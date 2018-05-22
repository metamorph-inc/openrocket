
OpenRocket - an Open Source model rocket simulator
==================================================
### Source Code for the OpenMETA Adaptation of OpenRocket

This version of OpenRocket has been modified so Python scripts may be used to automate flight simulations.

For **_Python script_** examples, see the [Scripting Examples](https://github.com/metamorph-inc/openrocket/tree/master/scripting_examples) folder.

For an example **_OpenMETA application_** of this OpenRocket version, see the [OpenMETA Rocket project](https://github.com/metamorph-inc/openmeta-rocket).

For instructions on how to **_build OpenRocket.jar from this source_**, see [BUILD.md](https://github.com/metamorph-inc/openrocket/blob/master/BUILD.md).

Source
------
Copyright (C) 2007-2011  Sampo Niskanen
    
For license information see the file LICENSE.TXT.

For more information see http://openrocket.sourceforge.net/

**Contributions have been made by:**

Sampo Niskanen, main developer
Doug Pedrick, support for reading RockSim designs, printing
Richard Graham, geodetic computations
Boris du Reau, internationalization
Tripoli France, Tripoli Spain, Stefan Lobas / ERIG, translations

Changelog
---------
The OpenRocket source code was changed according to [this Mailing List post](https://sourceforge.net/p/openrocket/mailman/openrocket-devel/thread/4F17AA0C.1040002@rdg.cc/) on Sourceforge in order to call OpenRocket from scripts.
1. function net.sf.openrocket.startup.startup.initializeLogging changed from private to public
2. function net.sf.openrocket.startup.startup.initializeL10n changed from private to public
3. function net.sf.openrocket.startup.startup2.loadMotor changed from private to public

