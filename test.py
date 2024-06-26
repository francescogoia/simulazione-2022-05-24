from model.model import Model

myModel = Model()
myModel._creaGrafo("2")
print(myModel.getGraphDetails())
print(myModel.durataMax())
lista, dimLista = myModel.handleLista(63, 20000)
print(dimLista)
print(f"Lista lunga {len(lista)}")
for l in lista:
    print(l)


