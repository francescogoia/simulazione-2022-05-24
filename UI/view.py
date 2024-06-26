import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None

        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Simulazione 2022-05-24", color="blue", size=24)
        self._page.controls.append(self._title)

        self._DDGenere = ft.Dropdown(label="Genere")
        self._controller.fillDDGenere()

        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph, width=200)
        self._btn_delta = ft.ElevatedButton(text="Delta massimo", on_click=self._controller.handle_delta, disabled=True)

        row1 = ft.Row([self._DDGenere, self.btn_graph, self._btn_delta], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.txt_result1 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result1)

        self._DDCanzone = ft.Dropdown(label="Canzone", width=500)
        self._txtMemoria = ft.TextField(label="Memoria (MBytes)")

        self._btnCreaLista = ft.ElevatedButton(text="Crea lista", on_click=self._controller.handle_lista, disabled=True)

        row3 = ft.Row([ self._DDCanzone, self._txtMemoria,self._btnCreaLista], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result2)
        self._page.update()

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
