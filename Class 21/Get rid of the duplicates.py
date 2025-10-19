# Get rid of the duplicates
students ={
    "id1":
     {
         "name" : "Ulaa",
         "Grade" : "7",
         "subject":['computer','English','Science']
     } ,
     "id2":
     {
         "name" : "Usha",
         "Grade" : "7",
         "subject":['CA','Math','H&PE']

     } , 
         "id3":
     {
         "name" : "Ulaa",
         "Grade" : "7",
         "subject":['computer','English','Science']
     } ,
         "id4":
     {
         "name" : "Hafsa",
         "Grade" : "7",
         "subject":['computer','English','Science']
     } 

}
result = {}
for keys,value in students.items():
    if value not in result.values():
        result[keys] = value

print(result)