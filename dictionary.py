import pickle


myDict = {}
myDict["001"] = ""
myDict["002"] = ""
myDict["003"] = ""
myDict["004"] = ""
myDict["005"] = ""
myDict["006"] = ""
myDict["007"] = ""
myDict["008"] = ""
myDict["009"] = ""
myDict["010"] = ""
myDict["010"] = ""
myDict["010"] = ""
myDict["011"] = ""
myDict["012"] = ""
myDict["013"] = ""
myDict["014"] = ""
myDict["015"] = ""
myDict["016"] = ""
myDict["017"] = ""
myDict["018"] = ""
myDict["019"] = ""
myDict["020"] = ""
myDict["021"] = ""
myDict["022"] = ""
myDict["023"] = ""
myDict["024"] = ""
myDict["025"] = ""
myDict["026"] = ""
myDict["027"] = ""
myDict["028"] = ""
myDict["029"] = ""
myDict["030"] = ""
myDict["031"] = ""
myDict["033"] = "Nauman"
myDict["034"] = "Umair"
myDict["035"] = "Zaryab"
myDict["036"] = "Saad"
myDict["038"] = "Ahmad"
myDict["039"] = "Atiqa"
myDict["040"] = "Hamza"
myDict["041"] = "Faran"
myDict["042"] = "Hassan"
myDict["043"] = "Haseeb"






output = open('myfile.pkl', 'wb')
pickle.dump(myDict, output)
output.close()


