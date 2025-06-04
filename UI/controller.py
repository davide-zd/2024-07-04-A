import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    # popolo dropdown anno
    def fillDD_year(self):
        lista_anni = self._model.fillDD_year()
        self._view.ddyear.options.clear()

        for a in lista_anni:
            self._view.ddyear.options.append(ft.dropdown.Option(
                text = a))
        self._view.update_page()

    # popolo dropdown forma
    def handleDD_shape(self, e):
        anno = self._view.ddyear.value

        # controllo che l'anno non sia nullo
        if (anno is None):
            self._view.txt_result1.controls.append(ft.Text("Devi scegliere un anno"))
            self._view.update_page()
            return

        lista_forme = self._model.fillDD_shape(anno)
        self._view.ddshape.options.clear()

        for a in lista_forme:
            self._view.ddshape.options.append(ft.dropdown.Option(
                text=a))
        self._view.update_page()

    def handle_graph(self, e):

        self._view.txt_result1.controls.clear()
        anno = self._view.ddyear.value
        shape = self._view.ddshape.value

        # controllo che l'anno non sia nullo
        if (anno is None):
            self._view.txt_result1.controls.append(ft.Text("Devi scegliere un anno"))
            self._view.update_page()
            return

        # controllo che la forma non sia nulla
        if (shape is None):
            self._view.txt_result1.controls.append(ft.Text("Devi scegliere una forma"))
            self._view.update_page()
            return

        # creo il grafo e i dettagli
        self._model.creoGrafo(anno, shape)
        n, e = self._model.graphDetails()

        # stampo i nodi e gli archi
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha {n} nodi e {e} archi."))
        self._view.update_page()

        n_componenti = self._model.getCompConn()
        self._view.txt_result1.controls.append(ft.Text(f"Il grafo ha: {n_componenti} componenti connesse."))
        self._view.update_page()

        num_max, lista_nodi = self._model.getMaxCompConn()
        self._view.txt_result1.controls.append(ft.Text(f"La componenete connessa più grande è costituita da {num_max} nodi"))
        for i in lista_nodi:
            self._view.txt_result1.controls.append(
                ft.Text(f"{i}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
