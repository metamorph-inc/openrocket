Building Open Rocket 1.1.9 from Source
======================================
### Requirements
* Java JDK/JRE version 1.6 or later
* Eclipse Luna (Found [Here](https://www.eclipse.org/downloads/packages/release/luna/sr2))

### Open the Open Rocket Project
1. Open Eclipse.
2. Select **File > Import**.
3. In the *Select* pop-up window, click **General >  Existing Projects into
   Workspace** and then click **Next**.
4. In the following *Import Projects* menu, click **Browse** next to the *Select
   root directory* box. Navigate to and select the folder that holds all of the
   OpenRocket source code, then click **OK**. The *Projects* box should now list
   the OpenRocket project. Make sure the box next to the OpenRocket project is
   checked and click **Finish**.

### Export OpenRocket as a .jar
1. Select **File > Export**.
2. In the *Select* pop-up window, select **Java >  JAR file** and then click **Next**.
3. In the *JAR File Specification* window, select all the resources you would
   like to export. (Selecting the entire project folder works, but do not include
   old JAR files!) Change the path and name of the exported file in the *JAR file*
   text box if desired. Make sure **Export generated class files and resources**
   and **Compress the contents of the JAR file** options are checked, then click **Next**.
4. Click **Next** again.
5. In the *JAR Manifest Specification* window, select the **Generate the manifest
   file** radial button. Check **Save the manifest in the workspace**. (Leave
   the manifest filename as the default MANIFEST.) Select the **Seal the JAR**
   radial button. Finally, select **Startup** as the *Main class*, then click **Finish**.
