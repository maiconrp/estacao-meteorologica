from pages import home, login, meteorologia

# DESTINOS
    
class Route:
    def build_routes():
        ROUTES = {
            "/": home.HomePage.build(),
            "/login": login.LoginPage.build(),
            "/Meteorologia": meteorologia.MeteorologiaPage.build()
        }
        return ROUTES


    def get_destiny(route):
        return Route.build_routes().get(route, "/")

    def get_routes():
        return list(Route.build_routes().keys()) 
        # ["/", "/login", "/Meteorologia"]
        # 0, 1, 2
