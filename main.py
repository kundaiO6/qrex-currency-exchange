import flet as ft
from appmenu import *
from form import Form
from welcome import Welcome
from tab import tabs_menu
from navDrawer import navDrawer

def main(page: ft.Page):
    page.drawer = navDrawer   
    page.title="Qrex"
    searchButton.on_click = lambda e : open_searchDialog(e, page)
    notificationButton.on_click = lambda e : open_notificationDialog(e, page)
    addNew.on_click = lambda e : open_formDialog(e, page)
    if True:
        page.add(
            Appmenu,
          tabs_menu
        )
    else:
        page.add(
            Welcome
        )

ft.app(main)

