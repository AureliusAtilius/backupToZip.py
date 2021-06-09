#!/usr/bin/env python3
import os, zipfile


def backupToZip(folder):
        # Back up the entire contents of "folder" into a ZIP File.
        folder = os.path.abspath(folder)

        # Figure out the filename this code should use based on 
        # what files already exist.
        number = 1 
        while True:
                zipFilename = os.path.basename(folder) + "_" + str(number) + '.zip'
                if not os.path.exists(zipFilename):
                        break
                number +=1
        
        #TODO: Create the ZIP file.
        print("Creating {}...".format(zipFilename))
        backupZip = zipfile.ZipFile(zipFilename,'w')
        #TODO: Walk the entire folder tree and compress the files in each folder.
        for foldername,subfolders,filenames in os.walk(folder):
                print(f'Adding files in {foldername}...')
                # Add the current folder to the ZIP file.
                backupZip.write(foldername)

                # Add all the files in this folder to the ZIP file.
                for filename in filenames:
                        newBase = os.path.basename(folder)+ "_"
                        if filename.startswith(newBase) and filename.endswith('.zip'):
                                continue # don't back up the backup ZIP files
                        backupZip.qrite(os.path.join(foldername, filename))
        backupZip.close()
        print("Done.")

if __name__=="__main__":
        backupToZip('C:\\Path\\to\\folder')