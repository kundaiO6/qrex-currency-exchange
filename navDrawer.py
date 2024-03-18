import flet as ft
navDrawer =  ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.Container(
                margin=ft.margin.only(left=15),
                content=ft.Column([
                ft.Text("Qrex", size=30, weight="bold"),
                ft.Row([ft.Text("Account", size=12, weight="bold"),
                ft.Text("xxx-xxx-xxx", size=12)
                ])
                    ]
                   )),

            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.SETTINGS),
                label="Settings",
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.ARROW_BACK),
                label="logout"
            ),
        ],
    )