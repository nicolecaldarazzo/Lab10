import flet as ft
from pydantic.color import ints_to_rgba


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        anno=self._view._txtAnno.value
        if anno=="":
            self._view._txt_result.controls.append(ft.Text("Inserire un anno!",color="red"))
            return
        try:
            intanno=int(anno)
        except ValueError:
            self._view._txt_result.controls.append(ft.Text("Inserire un valore intero numerico che rappresenti un anno!",color="red"))
            return

        if intanno<1816 or intanno>2016:
            self._view._txt_result.controls.append(ft.Text("Inserire un anno tra il 1816 e il 2016!", color="red"))
            return
        self._model.buildGraph(intanno)
        numComp=self._model.getCompConn()
        elencoStati=self._model.getNodes()
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {numComp} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito il dettaglio sui nodi:"))
        for s in elencoStati:
            self._view._txt_result.controls.append(ft.Text(f"{s[0]} -- {s[1]} vicini."))
        self._view.update_page()

    def handleRaggiungibili(self,e):
        pass
