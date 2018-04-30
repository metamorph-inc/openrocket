import sys, traceback
import numpy as np
import orhelper

orhelper.OpenRocketInstance('C:\Users\Cailey\Documents\MetaMorph\OpenRocket.jar', log_level='ERROR')
orh = orhelper.Helper()

# Load document, run simulation and get events

doc = orh.load_doc('C:\Users\Cailey\Documents\MetaMorph\openrocket\datafiles\examples\simple.ork')

gui = orh.export_rocket_image(doc)

print "Orhelper is: "
print orh.orp
print "Doc Object is: "
print doc
print "GUI object is: "
print gui


#TODO: Create new package & put PrintController in it. Might work? May need to move other classes from gui.print as well

"""
In src.net.openrocket.gui.dialogs.PrintDialog - starts Design Report export
src.net.openrocket.gui.print.PrintController
	/**
	 * Generate a report to a specified file.
	 *
	 * @param f     the file to which rocket data will be written
	 * @param paper the name of the paper size
	 *
	 * @return a file, populated with the "printed" output (the rocket info)
	 *
	 * @throws IOException thrown if the file could not be generated
	 */
	private File generateReport(File f, PrintSettings settings) throws IOException {
		Iterator<PrintableContext> toBePrinted = currentTree.getToBePrinted();
		new PrintController().print(document, toBePrinted, new FileOutputStream(f), settings);
		return f;
	}

Print Controller Parameters:
document is an OR document (.ork)
private RocketPrintTree currentTree; -> instantiated in PrintDialog constructor -- look into this, do I need it?
output file -> being written to --> where is this being named???
settings --> where do I set these? Look in print dialog

"""
