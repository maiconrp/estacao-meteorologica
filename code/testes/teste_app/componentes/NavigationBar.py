from flet import NavigationBar, NavigationDestination, icons

navigation_bar = NavigationBar(
    destinations=[
        NavigationDestination(icon=icons.EXPLORE, label="Home"),
        NavigationDestination(icon=icons.COMMUTE, label="Login"),
        NavigationDestination(icon=icons.COMMUTE, label="Meteorologia"),
    ],
)