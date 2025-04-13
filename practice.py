students = {
    "Aさん" : 88,
    "Bさん" : 76,
    "Cさん" : 90
}
students["Dさん"] = 95
students["Cさん"] -=3
for name , score in students.items():
    print( name, "," , score)