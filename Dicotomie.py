#Dicotomie
liste = [6,0,3,11,9,1,8,5,93,100,54,36,23,22,78]

def GoogleDico (liste,a):
    Quit = 0
    if liste[int(len(liste)/2)] == a:
    else:
        while Quit == 0:
            moitie = int(len(liste)/2)
            if liste[moitie] < a :
                del(liste[])

    
def swap(liste,a,b):
    smv = liste[a]
    liste[a] = liste[b]
    liste[b] = smv
    
for j in range(0,len(liste)):
    for a in range(0,len(liste)-1):
        b = a + 1
        if liste[a] > liste[b]:
            swap(liste,a,b)
print(liste)

