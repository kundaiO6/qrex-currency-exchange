from flet import *
from listing import Buy, Sell
tabs_menu = Tabs(
    tab_alignment=TabAlignment.CENTER,
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="Buy",
                content=Buy,
                tab_content=Container(width=150,alignment=Alignment(0,0),content=Text("Buy"))
            ),
             Tab(
                text="Sell",
                content=Sell,
                tab_content=Container(width=150,alignment=Alignment(0,0),content=Text("Sell"))
            ),
        ]
    )