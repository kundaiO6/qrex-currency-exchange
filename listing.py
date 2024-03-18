from flet import *
import requests
try:
    r = requests.get('http://127.0.0.1:8000/native/')
    data = r.json()
    Buy = Card(
        width=300,
        content=Container( padding=padding.all(10), content=Column([
            
        ]))
    )
    mark=""
    for x in data:

        if x['action'] == 'Selling':
            mark = 'blue'
        else:
            mark = 'red'

        Buy.content.content.controls.append(Container(bgcolor="white", border_radius=10, width=300, padding=padding.all(10), content=Row([
            ListView(controls=[
            Column([Text(f"1.00 {x['currency']}"),Text(f"{x['at'] } {x['pair']}")]),
            Text(f"{x['phone_number']}, {x['country']}", size=12),

                                                  ],
                                    expand=True,
                                    spacing=10,
                                    auto_scroll=True,
                                                  ),
            TextButton("Buy", style=ButtonStyle( padding=padding.all(0),bgcolor="red", color="white"))
                                                  ])))
except Exception as ex:
    print(ex)
    Buy = Text("Oops Something went wrong check your internet connection")
 
try:
    r = requests.get('http://127.0.0.1:8000/native/')
    data = r.json()
    Sell = Card(
        width=300,
        content=Container( padding=padding.all(10), content=Column([
        
            
        ]))
    )
    mark=""
    for x in data:

        if x['action'] == 'Selling':
            mark = 'blue'
        else:
            mark = 'red'

        Sell.content.content.controls.append(Container(bgcolor="white", border_radius=10, width=300, padding=padding.all(10), content=ListView(controls=[
            Row([Text(f"({x['action']})", color=mark),Text(f"{x['currency']}/{x['pair']} @ {x['at'] }")]),
            Text(f"{x['phone_number']}, {x['country']}", size=12),

                                                  ],
                                    expand=True,
                                    spacing=10,
                                    auto_scroll=True,
                                                  )))
except Exception as ex:
    print(ex)
    Sell = Text("Oops Something went wrong check your internet connection")
 
