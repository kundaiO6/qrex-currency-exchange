from flet import *
from form import Form
from search import Search
from Notification import Notification
#New to python don`t know if theres a way to avoid puting functions at the top like this
def open_formDialog(e, page):
    #pass page here
    page.dialog = formDialog
    formDialog.open = True
    page.update()


def open_searchDialog(e,page):
    #pass page here
    page.dialog = searchDialog
    searchDialog.open = True
    page.update()

def open_notificationDialog(e, page):
#pass page here
    page.dialog = notificationDialog
    notificationDialog.open = True
    page.update()

def show_drawer(e, page):
    #pass page here
    page.drawer.open = True
    page.drawer.update()

#AppBar 
app_name = Container( margin=margin.only(left=-28), content=Text(  value="Qrex", size=20,color="white", weight="bold", text_align=TextAlign.START))
Appmenu = AppBar(title=app_name, bgcolor="green", color="white")
searchButton = IconButton(icon=icons.SEARCH, icon_color="white")
notificationButton = IconButton(icon=icons.NOTIFICATIONS, icon_color="white")
addNew = ElevatedButton( height=25, width=70,  content=Row([Text("Add", size=12),Container(margin=margin.only(left=-8), content=Icon(name=icons.ADD, size=12))]))
Appmenu.actions.append(addNew)
Appmenu.actions.append(notificationButton)
Appmenu.actions.append(searchButton)

formDialog = AlertDialog(content=Form)
searchDialog = AlertDialog(content=Search)
notificationDialog = AlertDialog(content=Notification)

#TODO impliment a tab layout for BottomAppBar 
Bottomnav =Container( 
    border=Border(top=1),
    content=BottomAppBar(
    content=Row([
        IconButton(icon=icons.HOME),
        IconButton(icon=icons.LIST),
        IconButton(icon=icons.PERSON)

    ], alignment="spaceBetween")
))

