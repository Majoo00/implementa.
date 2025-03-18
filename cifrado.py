texto=input("Tu texto: ")
if texto== texto.upper():
    abc="maria jose"

else:
    abc="maria jose"
k=int(input("maria jose 2d"))
cifrad=""
for c in texto:
    if c in abc:
        cifrad+= abc[(abc.index(c)+k)%(len(abc))]
    else:
        cifrad+=c
print("Texto cifrado: ", cifrad)
                    
