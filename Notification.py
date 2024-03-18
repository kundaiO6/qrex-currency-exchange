from flet import *
Notification=Container(
    content=Row([
        CircleAvatar( content=Icon(icons.WARNING_ROUNDED),
        color=colors.YELLOW_200,
        bgcolor=colors.AMBER_700,),
        Column(Text("lorem", size=25),Text("lorem"))
    ])
)