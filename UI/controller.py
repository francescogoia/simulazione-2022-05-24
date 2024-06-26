import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenere(self):
        generi = self._model._generi
        for g in generi:
            self._view._DDGenere.options.append(ft.dropdown.Option(data=g[0], text=g[1], on_click=self._handleGenere))
        self._view.update_page()

    def _handleGenere(self, e):
        if e.control.data is None:
            self.choiceGenere = None
        else:
            self.choiceGenere = e.control.data

    def handle_graph(self, e):
        self._model._creaGrafo(self.choiceGenere)
        nNodi, nArchi = self._model.getGraphDetails()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato.\n"
                                                       f"Il grafo ha {nNodi} nodi e {nArchi} archi."))
        canzoni = self._model._nodes
        for c in canzoni:
            self._view._DDCanzone.options.append(ft.dropdown.Option(data=c.TrackId, text=c.Name, on_click=self._handleCanzone))

        self._view._btn_delta.disabled = False
        self._view._btnCreaLista.disabled = False
        self._view._btnCreaLista.disabled = False
        self._view.update_page()

    def _handleCanzone(self, e):
        if e.control.data is None:
            self.choiceCanzone = None
        else:
            self.choiceCanzone = e.control.data

    def handle_delta(self, e):
        canzoniDurataMax = self._model.durataMax()
        self._view.txt_result1.controls.append(ft.Text(f"Coppia/e canzoni delta massimo:"))
        for c in canzoniDurataMax:
            self._view.txt_result1.controls.append(ft.Text(f"{c[0]} ** {c[1]} --> {c[2]}"))
        self._view.update_page()

    def handle_lista(self, e):
        dimensioneMB = self._view._txtMemoria.value
        try:
            intDimensioneMB = int(dimensioneMB)
        except ValueError:
            self._view.txt_result2.controls.append(ft.Text("Inserire un valore intero per la memoria"))
            self._view.update_page()
            return
        dimensioneBytes = intDimensioneMB * 1000000
        lista, bytesLista = self._model.handleLista(self.choiceCanzone, dimensioneBytes)
        self._view.txt_result2.controls.append(ft.Text(f"La lista trovata ha dimensione {bytesLista} bytes ed è lunga {len(lista)} canzoni."))
        for l in lista:
            self._view.txt_result2.controls.append(ft.Text(f"{l[0]} : {l[1]} bytes."))

        self._view.update_page()

