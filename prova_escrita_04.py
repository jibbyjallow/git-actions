def cercar_el(matriu,element, mostrar_posicio=False):
    trobat =False
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if matriu[i][j] == element:
                trobat = True
                if mostrar_posicio:
                    
                    return (trobat, (i,j))
                else:
                    return (trobat, None)
                
    return (trobat,None)

def sumar_fila(matriu, index=0):
    
    if 0<=index<len(matriu) or -1>=index>=-len(matriu):
        return sum(matriu[index])
    else:
        return None
    
def sumar_matriu(matriu):
    total=0
    for i in range(len(matriu)):
        total += sumar_fila(matriu,i)
        
    return total

def transformar(matriu,k,op):
    
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if op == "+":
                matriu[i][j] += k
            elif op == "-":
                matriu[i][j] -= k
            elif op == "*":
                matriu[i][j] *= k
            elif op == "/":
                matriu[i][j] /= k 


