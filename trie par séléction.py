# trie par séléction
liste = [6,3,11,9,1,8,5,93,100,54,36,23,0,22,78]

def swap(liste,a,b):
    smv = liste[a]
    liste[a] = liste[b]
    liste[b] = smv
    
for j in range(0,len(liste)):
    indice = j
    for i in range(j+1,len(liste)):
            if liste[indice] > liste[i]:
                indice = i
    swap(liste,indice,j)
print(liste)
