def trobar_min_max_rendiment(*nombres):
    if len(nombres) == 0:
        return 0, 0
    else:
        millor_rendiment = min(nombres)
        pitjor_rendiment = max(nombres)
        return millor_rendiment, pitjor_rendiment
    

m1 = 10.50
m2 = 12.00
m3 = 15.00
millor_rendiment, pitjor_rendiment = trobar_min_max_rendiment(m1, m2, m3)
#print(f"La millor marca de {m1}, {m2} i {m3} es {millor_rendiment} i la pitjor es {pitjor_rendiment}")

def comptar_estudiants(estudiants):
    return len(estudiants)

notes_estudiants = {
    "Anna": {"Matemàtiques": 8, "Història": 7}, 
    "Marc": {"Matemàtiques": 6}, 
    "Laura": {"Ciències": 9, "Matemàtiques": 10}, 
    "Jordi": {"Història": 5}} 

#print(f"Hi ha {comptar_estudiants(notes_estudiants)} estudiants matriculats a l'institut.")


def comptar_estudiants_matèria(notes, matèria):
    return len([estudiant for estudiant in notes if matèria in notes[estudiant]])

def comptar_estudiants_matèria_v2(notes, matèria):  
    comptador = 0
    for estudiant in notes:
        if matèria in notes[estudiant]:
            comptador += 1
    return comptador    

#print(f"Hi ha {comptar_estudiants_matèria(notes_estudiants, 'Matemàtiques')} estudiant(s) matriculat(s) a la matèria Matemàtiques.")    

#print(f"Hi ha {comptar_estudiants_matèria_v2(notes_estudiants, 'Matemàtiques')} estudiant(s) matriculat(s) a la matèria Matemàtiques.")