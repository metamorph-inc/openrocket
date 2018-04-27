/*
 * PrintController.java
 *
 */
package net.sf.openrocket.report;

import com.itextpdf.text.Document;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.ExceptionConverter;
import com.itextpdf.text.Rectangle;
import com.itextpdf.text.pdf.PdfBoolean;
import com.itextpdf.text.pdf.PdfName;
import com.itextpdf.text.pdf.PdfWriter;
import net.sf.openrocket.document.OpenRocketDocument;
import java.io.IOException;
import java.io.OutputStream;


/**
 * This is the main active object for printing.  It performs all actions necessary to create and populate the print
 * file.
 */
public class PrintController {
	
	private OpenRocketDocument doc;
	
	public PrintController(OpenRocketDocument doc){
		// just trying this
		this.doc = doc;
	}
	
	/**
	 * Print the selected components to a PDF document.
	 *
	 * @param doc         the OR document
	 * @param toBePrinted the user chosen items to print
	 * @param outputFile  the file being written to
	 * @param settings    the print settings
	 */
	public void export(OutputStream outputFile, PrintSettings settings) {
		
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
