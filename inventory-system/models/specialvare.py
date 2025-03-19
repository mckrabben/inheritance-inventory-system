from models.vare import Vare

class SpecialVare(Vare):
    """Repræsenterer en specialvare i lageret med ekstra funktionalitet."""
    
    def __init__(self, name: str, quantity: int, location: str, category: str, off_site_location="N/A"):
        """Opretter en specialvare med navn, antal, placering og kategori."""
        super().__init__(name, quantity, location, off_site_location)
        self.category = category  # Kategori for specialvaren
    
    def get_category_info(self):
        """Returnerer information om varens kategori."""
        return f"Kategori: {self.category}"
    
    def __str__(self):
        """Returnerer en letlæselig beskrivelse af specialvaren."""
        base_str = super().__str__()
        return f"{base_str} - {self.get_category_info()}"