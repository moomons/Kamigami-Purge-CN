#!/usr/bin/env python

import os
import sys

print('Function: Purge CN subtitle in Kamigami Chi-Jap .ass subtitle files')

Option_Keyword_CN = {  # Lines containing any of those keyword will be removed.
    "CN,NTP,",
    "CN-ue,NTP,"
}
Option_CaseSensitive = 0  # Case insensitive : 0, Case sensitive : 1 (Any non-zero value)
# Option_Overwrite = 0  # Overwrite the original file : 1 (Any non-zero value)
Option_Keyword_EmptyLines = "0000,,"  # Lines ending with this keyword will be removed.
Option_RemoveEmptyLines = 1  # Remove empty lines : 1, else : 0

Option_Rename = 1  # Enable renaming (just simple file name replacement), or it WILL OVERWRITE the file
Option_Rename_Find = " 1920x1080 x264 Hi10P FLAC).Chs&"
Option_Rename_ReplaceAs = ")."

Option_DefaultWorkingDirectory = "."  #
Option_FileExtension = ".ass"  #

# Print Options
# print('Option_Keyword = ' + Option_Keyword_CN)
# print('Option_CaseSensitive = ' + str(Option_CaseSensitive))
# print('Option_Overwrite = ' + str(Option_Overwrite))


def processfile(filepath):
    print('\nOpening file: ' + filepath)
    # filehandle = open("[Kamigami] Hyouka - 01 (BDrip 1920x1080 x264 Hi10P FLAC).Chs&Jap.ass", "r")
    filehandle = open(filepath, "r")
    lines = filehandle.readlines()
    filehandle.close()

    dirpath = os.path.dirname(filepath)
    basename = os.path.basename(filepath)

    if Option_Rename:
        basename = basename.replace(Option_Rename_Find, Option_Rename_ReplaceAs)
        filepath = os.path.join(dirpath, basename)

    # filehandle = open("[Kamigami] Hyouka - 01 (BDrip).Jap.ass", "w")
    print('Saving as: ' + filepath)
    filehandle = open(filepath, "w")

    for line in lines:
        for kw in Option_Keyword_CN:
            if Option_CaseSensitive:
                result = line.find(kw)
                if result != -1:
                    break
            else:
                result = line.lower().find(kw.lower())
                if result != -1:
                    break

        if result == -1:
            result2 = 0
            if Option_RemoveEmptyLines:
                result2 = line.strip().endswith(Option_Keyword_EmptyLines)
            if not result2:
                filehandle.write(line)

    filehandle.close()


# Program Start
# Reference: https://stackoverflow.com/questions/2212643/python-recursive-folder-read
if len(sys.argv) > 1:
    Option_WorkingDirectory = sys.argv[1]
else:
    Option_WorkingDirectory = Option_DefaultWorkingDirectory

print('Working Directory: ' + os.path.abspath(Option_WorkingDirectory))

for root, subdirs, files in os.walk(Option_WorkingDirectory):
    # for subdir in subdirs:
    #     print('\t- subdirectory ' + subdir)
    for filename in files:
        file_path = os.path.join(root, filename)
        processfile(file_path)

print('\nJob done.')
