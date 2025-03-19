from vare import Vare

class LagerController:
    def __init__(self):
        """Opretter en liste med varer i lageret."""
        self.items = [
            Vare("Hammer", 5, "A1"),
            Vare("Skruetrækker", 0, "B3"),
            Vare("Sav", 3, "C2"),
            Vare("Møtrik", 10, "A2"),
            Vare("Bolt", 15, "A3"),
            Vare("Søm", 100, "A4"),
            Vare("Boremaskine", 2, "D1"),
            Vare("Vaterpas", 4, "E5"),
            Vare("Målebånd", 6, "F2"),
            Vare("Skruenøgle", 8, "G3"),
            Vare("Fastnøgle", 7, "H1"),
            Vare("Multimeter", 3, "I4"),
            Vare("Loddekolbe", 5, "J2"),
            Vare("Limpistol", 2, "K3"),
            Vare("Murerhammer", 3, "L1"),
            Vare("Vinkelsliber", 1, "M5"),
            Vare("Skæreklinge", 4, "N2"),
            Vare("Arbejdshandsker", 12, "O3"),
            Vare("Sikkerhedsbriller", 8, "P1"),
            Vare("Ørepropper", 20, "Q4"),
            Vare("Arbejdslampe", 3, "R5"),
            Vare("Kabeltromle", 2, "S1"),
            Vare("Forlængerledning", 5, "T2"),
            Vare("El-tester", 6, "U3"),
            Vare("Lommelygte", 9, "V4"),
            Vare("Svejsehjelm", 2, "W1"),
            Vare("Svejsehandsker", 5, "X2"),
            Vare("Svejseapparat", 1, "Y3"),
            Vare("Tætningsmasse", 7, "Z4"),
            Vare("Dykkerpistol", 3, "A5"),
            Vare("Hæfteklammer", 40, "B6"),
            Vare("Hæftepistol", 2, "C7"),
            Vare("Trælim", 5, "D8"),
            Vare("Gaffatape", 8, "E9"),
            Vare("Malertape", 6, "F10"),
            Vare("Sandpapir", 30, "G11"),
            Vare("Støvmasker", 10, "H12"),
            Vare("Læderhandsker", 7, "I13"),
            Vare("Høreværn", 3, "J14"),
            Vare("Arbejdssko", 4, "K15"),
            Vare("Kedeldragt", 2, "L16"),
            Vare("Fugepistol", 5, "M17"),
            Vare("Siliconefuge", 12, "N18"),
            Vare("Tommestok", 9, "O19"),
        ]

    def search_item(self, name):
        """Finder varer der matcher søgningen."""
        return [item for item in self.items if name.lower() in item.name.lower()]

    def get_all_items(self):
        """Returnerer alle varer i lageret."""
        return self.items

    def add_item(self, name, quantity, location):
        """Tilføjer en ny vare til lageret."""
        try:
            quantity = int(quantity)
            self.items.append(Vare(name, quantity, location))
        except ValueError:
            pass

    def update_item(self, name, new_quantity, new_off_site_location="N/A"):
        """Opdaterer en vares antal og valgfri lokation."""
        try:
            new_quantity = int(new_quantity)
            for item in self.items:
                if item.name.lower() == name.lower():
                    item.quantity = new_quantity
                    item.off_site_location = new_off_site_location
                    return
        except ValueError:
            pass

    def remove_item(self, name):
        """Fjerner en vare fra lageret."""
        self.items = [item for item in self.items if item.name.lower() != name.lower()]
