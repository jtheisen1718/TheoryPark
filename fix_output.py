import os
import sys
import zipfile

zip = zipfile.ZipFile('Archive.zip', 'w')
directory = sys.argv[1]
for f in os.listdir(directory):
    zip.write(os.path.join(directory, f), f)
    #print("wrote",f)
zip.close()