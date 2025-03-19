class Vare:
    """Repræsenterer en vare i lageret."""
    
    def __init__(self, name: str, quantity: int, location: str, off_site_location="N/A"):
        """Opretter en vare med navn, antal og placering."""
        self.name = name  # Navn på varen
        self.quantity = quantity  # Antal på lager
        self.location = location  # Placering i lageret
        self.off_site_location = off_site_location  # Placering udenfor lageret

    def is_in_stock(self):
        """Tjekker om varen er på lager."""
        return self.quantity > 0  # True hvis der er varer, ellers False
    
    def __str__(self):
        """Returnerer en letlæselig beskrivelse af varen."""
        status = "På lager" if self.is_in_stock() else "Ikke på lager"
        off_site = "" if self.is_in_stock() else f" - {self.off_site_location or 'N/A'}"
        return f"{self.name} ({self.quantity} stk) - {status} - {self.location}{off_site}"
