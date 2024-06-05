import flet as ft


def main(page: ft.Page):
    page.title = "Sistema Posgrado"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

     appBar = ft.AppBar(title=ft.Text("Sistema De Adminstración"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar

ft.app(main, view=ft.AppView.WEB_BROWSER)
