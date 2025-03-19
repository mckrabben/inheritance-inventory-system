from models.vare import Vare  # Importerer Vare-klassen
from models.specialvare import SpecialVare

class LagerController:
    def __init__(self):
        """Opretter en liste med varer i lageret."""
        self.items = [
            Vare("Hammer", 5, "A1"),
            Vare("Skruetrækker", 0, "B3"),
            Vare("Sav", 3, "C2"),
            SpecialVare("SpecialSav", 5, "C4", "Speciel"),
        ]

    def search_item(self, name):
        """Finder varer der matcher søgningen."""
        return [item for item in self.items if name.lower() in item.name.lower()]

    def get_all_items(self):
        """Returnerer alle varer i lageret."""
        return self.items

    def add_item(self, name, quantity, location, category=None):
        """Tilføjer en ny vare til lageret."""
        try:
            quantity = int(quantity)  # Sikrer at quantity er et tal
            if category:
                self.items.append(SpecialVare(name, quantity, location, category))
                print(f"[ADD] Tilføjet: {name}, {quantity} stk, placering {location}, kategori: {category}")
            else:
                self.items.append(Vare(name, quantity, location))
                print(f"[ADD] Tilføjet: {name}, {quantity} stk, placering {location}")
        except ValueError:
            print("[ERROR] Antal skal være et tal!")

    def update_item(self, name, new_quantity, new_off_site_location, new_category):
        """Opdaterer en vares antal. Hvis en kategori angives, skal varen være en SpecialVare.
        Hvis varen er special men opdateres uden kategori, konverteres den til en normal Vare."""
        try:
            new_quantity = int(new_quantity)
            for idx, item in enumerate(self.items):
                if item.name.lower() == name.lower():
                    if new_category and new_category.strip() != "":
                        # Hvis der er angivet en kategori, skal varen være special
                        if isinstance(item, SpecialVare):
                            item.quantity = new_quantity
                            item.off_site_location = new_off_site_location.strip() or item.off_site_location
                            item.category = new_category
                            print(f"[UPDATE] Updated SpecialVare: {name}")
                        else:
                            # Opgraderer en normal Vare til SpecialVare
                            new_item = SpecialVare(
                                name,
                                new_quantity,
                                item.location,
                                new_category,
                                new_off_site_location.strip() or item.off_site_location
                            )
                            self.items[idx] = new_item
                            print(f"[UPDATE] Upgraded Vare to SpecialVare: {name}")
                    else:
                        # Ingen kategori angivet: Hvis varen er special, skal den nedgraderes til en normal Vare
                        if isinstance(item, SpecialVare):
                            new_item = Vare(
                                name,
                                new_quantity,
                                item.location,
                                new_off_site_location.strip() or item.off_site_location
                            )
                            self.items[idx] = new_item
                            print(f"[UPDATE] Downgraded SpecialVare to Vare: {name}")
                        else:
                            # Normal opdatering af en allerede normal Vare
                            item.quantity = new_quantity
                            item.off_site_location = new_off_site_location.strip() or item.off_site_location
                            print(f"[UPDATE] Updated Vare: {name}")
                    return
            print("[ERROR] Vare ikke fundet!")
        except ValueError:
            print("[ERROR] Antal skal være et tal!")



    def remove_item(self, name):
        """Fjerner en vare fra lageret."""
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"[REMOVE] Fjernet: {name}")
                return
        print("[ERROR] Vare ikke fundet!")
