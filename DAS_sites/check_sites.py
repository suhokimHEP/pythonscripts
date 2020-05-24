import sys,os

listfile = open("dasmapAOD.list", "r")
    
for line in listfile:
    values = line.split()

    for value in values:
        if "/AOD" in value:
            output = os.popen('dasgoclient -query="site dataset='+value+'" -json').read()
            
            #don't bother with json parsing
            foundsite = False 
            outputlines = output.splitlines()
            for outputline in outputlines:
                #Look for T2 or T3
                if "T2_" in outputline or "T3_" in outputline or "T1_US_FNAL_Disk" in outputline:
                    #Look for 100% presence to filter out original placement
                    if '"block_completion":"100.00%"' in outputline and '"block_fraction":"100.00%"' in outputline and '"dataset_fraction":"100.00%"' in outputline:
                        foundsite = True
			print value
            if not foundsite:
		mvalue = 'No access for'+ value
                print mvalue
   