import platform

sysstr = platform.system()
print sysstr
if(sysstr =="Windows"):
    print ("Call Windows tasks")
elif(sysstr == "Linux"):
    print ("Call Linux tasks")
elif(sysstr == "Darwin"):
    print ("Call Mac tasks")
else:
    print ("Other System tasks")
