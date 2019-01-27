import pyrebase
from sample import the

'''config = {
    "apiKey": "AIzaSyDYWRcuwOEDLvdRq6nVDrpnoCO2bXybWb4",
    "authDomain": "dhishna-test.firebaseapp.com",
    "databaseURL": "https://dhishna-test.firebaseio.com",
    "projectId": "dhishna-test",
    "storageBucket": "dhishna-test.appspot.com"
} '''
config = {
	"apiKey" : "AIzaSyAZHCLuovX2oNhccuxjetkHNgAcrWcZLGo",
    "authDomain": "dhisna-ac7e0.firebaseapp.com",
    "databaseURL": "https://dhisna-ac7e0.firebaseio.com",
    "projectId": "dhisna-ac7e0",
    "storageBucket": "dhisna-ac7e0.appspot.com"
} 

firebase = pyrebase.initialize_app(config)

finished = [] # list of processed events

print("Fetching the names of the departments.")
db = firebase.database()
depts = []
temp = db.child("events").get()
for dep in temp.each():
	depts.append(dep.key())

print("Fetching the names of the events.")
deptEventsList = []
for dep in depts:
	deptEventsList.append([])	
	temp = db.child("events").child(dep).get()
	for event in temp.each():
		deptEventsList[-1].append(event.key())

print("Event names fetched.")

depts.remove("acc")
depts.remove("pre")

for x in deptEventsList:
    if ('female' in x) or ('Make-a-Ton' in x):
            deptEventsList.remove(x)



print("Starting downloads.")
storage = firebase.storage()

		
for x in range(0, len(depts)):
	curDept = depts[x]
	print("Department: " + curDept + "(" + str(x+1) + " out of " + str(len(depts)) + ")")
	for y in range(0,len(deptEventsList[x])):
		curEvent = deptEventsList[x][y]
		print("Event: " + curEvent + "(" + str(y+1) + " out of " + str(len(deptEventsList[x])) + ")")
		print("Downloading...")
		storage.child("events").child(curDept).child(curEvent).child("event.svg").download("a.svg")
		print("Download finished.")
		print("Processing...")
		the()


        # Enter processing stuff here.

		print("Uploading...")
		#uploads to the database. HANDLE WITH CARE.
		#storage.child("events").child(curDept).child(curEvent).child("event.xml").put("a.xml")
		finished.append(curEvent)
		ent = input("press 1 to continue")
                
                

