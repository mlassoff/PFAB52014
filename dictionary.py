songs = { "Journey" : "Faithfully" , "Reo Speedwagon" : "Keep on Loving You" , "Kansas" :  "Dust in the Wind" , 
"Boston" : "Amanda" , "Survivor" :  "Eye of the Tiger" , "Cure" : "Plainsong"}

salaries = { "Johnson" : 25000 , "Smith" : 35000 , "Hernandez" : 49000 , "Orsoco" : 19500 ,
"Edelman" :  75600 }

print songs["Reo Speedwagon"]
print "The best song on the best album ever made is: " , songs["Cure"]
print "Edelman earns: " , salaries["Edelman"]

songs["Kansas"] = "Carry on Wayward Son"
print songs

salaries["Johnson"] = 30000
print salaries

del salaries["Smith"]
print salaries

if songs.has_key("Journey"):
	print "Journey Rocks!  And Steve Perry is back"
 
print songs.keys()
print songs.values()

