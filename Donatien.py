# Pour moyenne

donatien={"Python": [19,20,18],"Langage C" : [15,18,17],"SDA":[20,15,16]}

sumNotes=donatien["Python"][0]+donatien["Python"][1]+donatien["Python"][2]+donatien["Langage C"][0]+donatien["Langage C"][1]+donatien["Langage C"][2]+donatien["SDA"][0]+donatien["SDA"][1]+donatien["SDA"][2]

moyenne = sumNotes/(len(donatien)*3.0)
print(moyenne)

#E0
#________________________________

# 1)
L=list(range(1,11))

# 2)
L[0]=L[0]+11
L[1]=L[2]+11
L[2]=L[2]+11
L[3]=L[3]+11
L[4]=L[4]+11
L[5]=L[5]+11


# 3)
L.append(22)

# 4)
L.extend([23,24])

# 5)

# 6)
L.remove(3)

print(L)
print("________________________________\n")



# E1
#______________________________

d={"nom":"Dupuis","prenom":"Jacque","age":30}

#Correct
d['prenom']="Jacques"

print("Liste des clés : ")
print(d.keys())

print("\nListe des valeurs :")
print(d.values())

print("\nListe des clés valeurs")
print(d)

print("La phrase:")
print("\n\n"+d['prenom']+" "+d['nom']+" a "+str(d['age'])+" ans.")

