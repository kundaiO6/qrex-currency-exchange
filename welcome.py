from flet import *

Welcome = Container(
    height=500,
    alignment=Alignment(0, 0),
    padding=padding.all(50),
    content=Column([
         Container(margin=margin.only(top=100), content=Text("Welcome to Qrex ", size=25, weight="bold", text_align=TextAlign.CENTER)),
        Container(margin=margin.only(top=-10, bottom=45),content=Text("the best currency exchange \n platform \n", size=15, text_align=TextAlign.CENTER)),
        Container(content=TextButton(width=200, style=ButtonStyle( padding=padding.all(0),bgcolor="green", color="white"),text="Continue", content=Row([Text("Continue"),  Container(margin=margin.only(left=-5), content=Icon(name=icons.ARROW_FORWARD_IOS, size=13))], alignment=MainAxisAlignment.CENTER)))

    ])
)
