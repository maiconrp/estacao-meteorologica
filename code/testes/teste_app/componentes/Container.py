import flet as ft
from flet import *

"""page_container = Row(
    controls=[
        content=Column(
            controls=[

            ]
        )
    ]
)"""

card_cultura = Container(
    bgcolor = 'white',
    height=95,
    width=300,
    border_radius = 15,
    padding = padding.only(top=25, left=20, right=20, bottom=25),
    margin = margin.only(top=15),
    content = Column(horizontal_alignment = CrossAxisAlignment.CENTER,
        controls=[
            Container(
                content = ft.Text('Irrigação', color='#000000', size=12, weight=FontWeight.W_700),
            ),
        ]
    ),
)

line = Container(
        width=290,
        height=1,
        bgcolor='#00D154',
        margin = margin.only(left=5, bottom=10)
    )

relatorio = Container(
    Row(
        controls=[
            Icon(icons.CIRCLE_ROUNDED, color='#00D154', size=16),
            Text(value='Relatório', color='#000000', size=20, weight=FontWeight.W_600)          
        ]
    )
)

card_irrigacao = Container(
    content=Row(alignment='spaceBetween',
        controls=[
            Container(
                bgcolor = 'white',
                height=140,
                width=140,
                border_radius = 15,
                padding = padding.only(top=14, left=17, right=17, bottom=22),
                margin = margin.only(top=7),
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Container(
                                    bgcolor = '#EBEBF0',
                                    height=24,
                                    width=75,
                                    border_radius = 20,  
                                    margin = margin.only(right=7),                              
                                    content = ft.Text('Irrigação', color='#000000', size=12, weight=FontWeight.W_700), 
                                ),
                                Icon(name='settings', color='#00D154', size=16),
                            ]
                        ),
                        Container(                           
                            Text(value='1h30', color='#000000', size=39, weight=FontWeight.W_700),
                            margin = margin.only(top=-10)
                        ), 
                        Container(
                            Text(value='Tempo ideal de irrigação para hoje', color='#000000', size=11, weight=FontWeight.W_400)
                        ), 
                    ]
                ),
            ),
            Container(
                bgcolor = 'white',
                height=140,
                width=140,
                border_radius = 15,
                padding = padding.only(top=14, left=17, right=17, bottom=22),
                margin = margin.only(top=7),
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Container(                   
                                    bgcolor = '#EBEBF0',
                                    height=24,
                                    width=75,
                                    border_radius = 20,  
                                     margin = margin.only(right=7), 
                                    content = ft.Text('Economia', color='#000000', size=12, weight=FontWeight.W_700) 
                                                                                                      
                                ),

                                Icon(name='settings', color='#00D154', size=16),
                            ]
                        ),
                        Container(
                            Text(value='27%', color='#000000', size=39, weight=FontWeight.W_700),
                            margin = margin.only(top=-10)
                        ), 
                        Container(
                            Text(value='760 litros', color='#000000', size=11, weight=FontWeight.W_400),
                            Text(value='economizados', color='#000000', size=11, weight=FontWeight.W_400)
                        ), 
                    ]
                ),
            ),
        ]
    )
)

card_ET = Container(
    bgcolor = 'white',
    height=95,
    width=300,
    border_radius = 15,
    padding = padding.only(top=25, left=20, right=20, bottom=25),
    margin = margin.only(top=15),
)

page_container = Container(
    content=Column(
        controls=[
            Row(alignment='spaceBetween',
                controls=[
                    Container(
                        Text(value='Olá, Victor', color='#000000', size=25, weight=FontWeight.W_700)
                    ), 

                    Row(
                        controls=[
                            Text(value='Estação', color='#000000', size=13),
                            Icon(name='settings', color='#00D154', size=16)
                        ]
                    )                                            
                ]
            ), 
            Container(
                content=card_cultura,
            ),
            Container(
                content=line,
            ),
            Container(
                content=relatorio,
            ),
            Container(
                content=card_irrigacao,
            ), 
            Container(
                content=card_ET,
            )
        ]
    )
)


container_home = Container(
    width=350,
    height=650,
    bgcolor='#EFEFEF',
    border_radius=35,
    padding = padding.only(top=30, left=23, right=23, bottom=0),
    content=page_container
)















container_cultura = Container(

)