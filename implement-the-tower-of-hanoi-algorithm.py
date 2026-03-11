** start of main.py **

def hanoi_solver(argument):
    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(argument):
        lista1.append(i+1)
    lista1.reverse()

    nowy = []
    nowy.append(f"{lista1} {lista2} {lista3}")

    def tower(n, start, target, mid):
        if n == 1:
            disk = start.pop()
            target.append(disk)
            nowy.append(f"{lista1} {lista2} {lista3}")
        else:
            tower(n-1, start, mid, target)
            disk = start.pop()
            target.append(disk)
            nowy.append(f"{lista1} {lista2} {lista3}")
            tower(n-1, mid, target, start)

    tower(argument, lista1, lista3, lista2)

    return "\n".join(nowy)



** end of main.py **

