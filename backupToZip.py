#!/usr/bin/env python3
import os, zipfile


def backupToZip(folder):
        # Back up the entire contents of "folder" into a ZIP File.
        folder = os.path.abspath(folder)

        # Figure out the filename this code should use based on 
        # what files already exist.
        number = 1 
        while True:
                zipFilename = os.psth.basename(folder) + "_" + str(number) + '.zip'
                if not os.path.exists(zipFilename):
                        break
                number +=1
        
        #TODO: Create the ZIP file.

        #TODO: Walk the entire folder tree and compress the files in each folder.
        print("Done.")

if __name__=="__main__":
        backupToZip('C:\\Path\\to\\folder')