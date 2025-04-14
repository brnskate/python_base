#!/usr/bin/env python3
"""imprime a tabuada do 1 ao 10

---Tab do 1 
1x1 = 1
...

Tab do 2
2x1 = 2 
....
"""

######################

__version__ = "0.1.1"
__author__ = "Bruno"

template_base = """
---Tab do 2----


{bloco:^18}


##############
"""

#base = [1, 2, 3 ,4 ,5 ,6, 7, 8, 9, 10]
numeros = list(range(1, 11))

print(numeros)

# Iterable
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
#        print(operacoes)
    print("#" * 18)
