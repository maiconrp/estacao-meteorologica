from flet import *

dlg = AlertDialog(
    content =  Container(
        width = 250,
        height = 200,
        bgcolor = 'white',
        border_radius = 15,
        content = Container(
            Text(value='Milho', color='#000000', size=25, weight=FontWeight.W_700)
        )
    )      
)