/*
 * PrintController.java
 *
 */
package net.sf.openrocket.gui.print;

import com.itextpdf.text.Document;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.ExceptionConverter;
import com.itextpdf.text.Rectangle;
import com.itextpdf.text.pdf.PdfBoolean;
import com.itextpdf.text.pdf.PdfName;
import com.itextpdf.text.pdf.PdfWriter;
import net.sf.openrocket.document.OpenRocketDocument;
import net.sf.openrocket.gui.print.visitor.FinMarkingGuideStrategy;
import net.sf.openrocket.gui.print.visitor.FinSetPrintStrategy;
import net.sf.openrocket.gui.print.visitor.PartsDetailVisitorStrategy;
import net.sf.openrocket.gui.print.visitor.TransitionStrategy;

import java.io.IOException;
import java.io.OutputStream;
import java.util.Iterator;
import java.util.Set;

/**
 * This is the main active object for printing.  It performs all actions necessary to create and populate the print
 * file.
 */
public class PrintController {
	
	/**
	 * Print the selected components to a PDF document.
	 *
	 * @param doc         the OR document
	 * @param toBePrinted the user chosen items to print
	 * @param outputFile  the file being written to
	 * @param settings    the print settings
	 */
	public void printReport(OpenRocketDocument doc, OutputStream outputFile,
						PrintSettings settings) {
		
		Document idoc = new Document(getSize(settings));
		PdfWriter writer = null;
		try {
			writer = PdfWriter.getInstance(idoc, outputFile);
			writer.setStrictImageSequence(true);
			
			writer.addViewerPreference(PdfName.PRINTSCALING, PdfName.NONE);
			writer.addViewerPreference(PdfName.PICKTRAYBYPDFSIZE, PdfBoolean.PDFTRUE);
			try {
				idoc.open();
				Thread.sleep(1000);
			} catch (InterruptedException e) {
			}
			
			DesignReport dp = new DesignReport(doc, idoc);
			dp.writeToDocument(writer);
			idoc.newPage();
					
			
			//Stupid iText throws a really nasty exception if there is no data when close is called.
			if (writer.getCurrentDocumentSize() <= 140) {
				writer.setPageEmpty(false);
			}
			writer.close();
			idoc.close();
		} catch (DocumentException e) {
		} catch (ExceptionConverter ec) {
		} finally {
			if (outputFile != null) {
				try {
					outputFile.close();
				} catch (IOException e) {
				}
			}
		}
	}
	
	/**
	 * Get the correct paper size from the print settings.
	 * 
	 * @param settings	the print settings
	 * @return			the paper size
	 */
	private Rectangle getSize(PrintSettings settings) {
		PaperSize size = settings.getPaperSize();
		PaperOrientation orientation = settings.getPaperOrientation();
		return orientation.orient(size.getSize());
	}
	
}
