package net.sf.openrocket.document;

import net.sf.openrocket.document.OpenRocketDocument;
import net.sf.openrocket.gui.print.PrintController;
import net.sf.openrocket.gui.print.PrintSettings;
import net.sf.openrocket.gui.print.TemplateProperties;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

import net.sf.openrocket.util.FileHelper;
import net.sf.openrocket.util.Prefs;

/********************************************************
 * Class for creating Design Reports from python Scripts
 ********************************************************/

public class ExportReport {
	
	private OpenRocketDocument doc;
	
	public ExportReport(OpenRocketDocument OR_doc){
		this.doc = OR_doc;
	}
	
	public boolean generateReport() throws IOException {
		File file;
		PrintSettings settings;
		file = new File("DesignReport.pdf");
		file = FileHelper.ensureExtension(file, "pdf");
		settings = Prefs.getPrintSettings();
		TemplateProperties.setColors(settings);
		new PrintController().printReport(this.doc, new FileOutputStream(file), settings);
		return true;
	}
}
