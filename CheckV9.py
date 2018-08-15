#########################################     READ_ME for Scripting    #########################################
###                                                                                                          ###
###             INSTRUCTIONS:                                                                                ###
###             1. Install python3 using brew install.                                                       ###
###             2. pip3 should come with python3 using brew install.                                         ###
###             3. All libraries are imported at the top of the script should be installed using pip3.       ###
###             4. Make sure to read the URLs at the top of each script to learn more.                       ###
###             5. Recommend `pip3 install ipython` for Python interactive shell. Enjoy! :P                  ###
###                                                                                                          ###
################################################################################################################



################################################################################################################
###                                                                                                          ###
###                                                -IMPORTANT-                                               ###
###                                                                                                          ###
###                                               (╯°□°)╯︵ ┻━┻                                              ###
###                                                                                                          ###
###                       ENSURE VALUE(S) ARE SET UNDER 'IMPORT/READ CSV FILE SECTION'                       ###
###                         FIND AND REPLACE <fileName.csv> WITH YOUR CSV FILE NAME                          ###
###                        ENSURE BOTH CSV FILE AND .PY SCRIPT ARE IN THE SAME LIBRARY                       ###
###   IF SCRIPT IS IN A FOLDER CALLED 'CSV_CHECK,' ENSURE THE .CSV FILE IS ALSO IN THE 'CSV_CHECK' FOLDER    ###
###                                                                                                          ###
######################################### END OF READ_ME for Scripting #########################################



############################################    -START OF SCRIPT-    ###########################################

################################
##### IMPORT/READ CSV FILE #####
################################

import re
import sys

#### FILE NAME GOES HERE ####
csvFileName = "sys.argv[-1]

csvfile = open(csvFileName,'r', encoding='utf-8')
csv=[]
#if ascii_decode error thrown, try utf-8 encoding
try:
	csv = [line.split(',') for line in csvfile.readlines()]
except:
	print("ERROR: Invalid character. Converting...")
	csvfile = open(csvFileName,'r', encoding='utf-8',errors='replace')
	for line in csvfile.readlines():
		line.replace(u'\uFFFD','#')
		csv += [line.split(',')]

##############################
##### Validate File Name #####
##############################

#Check for Valid File Name with no special characters (PLACE YOUR FILE NAME IN HERE)
Success = True
for i in csvFileName:
	result = re.search(r"(['!@#$%^&*_ '])",i)
	if result:
		Success = False
if Success:
	print("Success: Valid File Name")
else:
	print("Failure: Invalid File Name (Cannot have special characters or spaces)")

# #############################
# ##### HEADER ROW CHECKS #####
# #############################

#Column check 200 limit
csvfile = open(csvFileName,'r')
for row in csvfile:
    if len(row) <= 200:
        print("Success: CSV has", len(row), "rows.")
    elif len(row) > 200:
        print("Error: CSV has", len(row), "rows.")
    break

#Check if header-userId is formatted correctly
Success = False
for i in csv[0]:
	result = re.fullmatch(r"userId",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of userId in Header Row")
else:
	print("Error found - Failure: Invalid formatting of userId in Header Row")

#Check if header-userAttributes formatted correctly
Success = False
Count = len(csv[0])-1
for i in csv[0]:
	result = re.fullmatch(r"userAttributes.([a-zA-Z0-9_ ])+",i)
	if result:
		Success = True
if Success:
	print("Success: Valid formatting of Header Row userAttribute(s)")
else:
	print(Count,"Error(s) found - Failure: Invalid formatting of userAttribute(s)")

#Check if there is empty header item <-- To Do (Understand wtf is going on here)
Success = True
blank = re.compile(r'\s*')
Count = 0
for i in csv[0]:
	result = blank.match(i).end() == len(i)
	if result:
		Success = False
		Count += 1
if Success:
	print("Success: Valid formatting of Header Row (No empty header column)")
else:
	print(Count,"Error(s) found - Failure: Invalid formatting of Header Row (Empty header column(s) found")

#Check if there are special characters in header row
Success = True
Count = 0 
for i in csv[0]:
	result = re.search(r"(['!@#$%^&*_ '])",i)
	if result:
		Success = False
		Count += 1
if Success:
	print("Success: Valid formatting of Header Row (No special characters)")
else:
	print(Count,"Error(s) found - Failure: Invalid formatting of Header Row (Special Characters Found)")

###########################
##### DATA ROW CHECKS #####
###########################

Success = True
Count = 0
for i in csv[1:]:
	result = len(i) > len(csv[0])
	if result:
		Success = False
		Count += 1
if Success:
	print("Success: Valid Data Row length")
else:
	print(Count,"Error(s) found - Failure: Data Row longer than Header Row")

#GUESS WHERE YOU FUCKING LEFT OFF YOU STUPID SONUVABITCH ---------> Check userId column for email <--------- GUESS WHERE YOU FUCKING LEFT OFF YOU STUPID SONUVABITCH
Success = True
Count = 0
for i in #csv[1]:
	result = re.fullmatch(r"(@[a-zA-Z0-9]+.)",i)
	if result:
		Success = False
		Count += 1
if Success:
	print("Success")
else:
	print("Failure")

#################
##### TO DO #####
#################

##### Priority tasks #####

#### ORIGINAL EMPTY HEADER ITEM CHECK #### <-- To Do - Adjust to simplify system
# blank = re.compile(r'\s*')
# Count = 0
# for i in csv[0]:
# 	if blank.match(i).end() == len(i):
# 		Count += 1
# print(Count,"Error(s) found: Empty header item(s)")

#### Check if there is whitespace #### <-- To Do
# Success = True
# Count = 0
# for i in csv[0]:
# 	result = re.search(r"\s+",i)
# 	if result:
# 		Success = False
# if Success:
# 	print("Success: Valid formatting of Header Row (No Whitespace)")
# else:
# 	print(Count,"Error(s) found - Failure: Invalid formatting of Header Row (Whitespace Found)")

#### Check for valid email under userAttributes.email <-- To Do
# (@[a-zA-Z0-9]+.) <-- utiize this regex under fullmatch?

##### Secondary Tasks #####

#### pull error(s) from special characters (which ones exactly) ####
#### specifcy which data row number is longer than header row (column/row) #####
#### possible - self fix for csv ####
#### set code blocks into functions ####


#################
##### TO DO #####
#################





#############################################    -END OF SCRIPT-    ############################################

################################################################################################################
###                                                                                                          ###
###                                                                                                          ###
###											  HOORAY! It's done!											 ###
###                                                                                                          ###
###												  (づ｡◕‿‿◕｡)づ 												 ###
###                                                                                                          ###
###                                                                                                          ###
################################################################################################################
