class Vare:
    """Repræsenterer en vare i lageret."""
    
    def __init__(self, name: str, quantity: int, location: str, off_site_location="N/A"):
        self.name = name
        self.quantity = quantity
        self.location = location
        self.off_site_location = off_site_location

    def is_in_stock(self):
        """Tjekker om varen er på lager."""
        return self.quantity > 0

    def __str__(self):
        """Returnerer en letlæselig beskrivelse af varen."""
        status = "På lager" if self.is_in_stock() else "Ikke på lager"
        off_site = f" - {self.off_site_location}" if not self.is_in_stock() else ""
        return f"{self.name} ({self.quantity} stk) - {status} - {self.location}{off_site}"
