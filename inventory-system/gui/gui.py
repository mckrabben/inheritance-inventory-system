import tkinter as tk  # Importerer tkinter til GUI
from controllers.lager_controller import LagerController  # Importerer lagerkontrolleren

class LagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lagersystem")
        self.controller = LagerController()

        # **Søg efter vare**
        tk.Label(root, text="Søg efter vare:").pack()
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()
        tk.Button(root, text="Søg", command=self.search_item).pack()

        # **Vis alle varer**
        tk.Button(root, text="Vis alle varer", command=self.show_all_items).pack()

        # **Resultatvisning**
        tk.Label(root, text="Resultater:").pack()
        self.result_listbox = tk.Listbox(root, width=50, height=10)
        self.result_listbox.pack()

        # **Tilføj vare**
        tk.Label(root, text="Tilføj ny vare").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        tk.Label(root, text="Antal").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()
        tk.Label(root, text="Placering").pack()
        self.location_entry = tk.Entry(root)
        self.location_entry.pack()

        tk.Label(root, text="Kategori (Optional)").pack()
        self.category_entry = tk.Entry(root)
        self.category_entry.pack()
        
        tk.Button(root, text="Tilføj", command=self.add_item).pack()

        # **Opdater lager**
        tk.Label(root, text="Opdater lager").pack()
        self.update_name_entry = tk.Entry(root)
        self.update_name_entry.pack()
        tk.Label(root, text="Nyt antal").pack()
        self.update_amount_entry = tk.Entry(root)
        self.update_amount_entry.pack()

        tk.Label(root, text="Off-site Lokation (Optional)").pack()
        self.update_off_site_location_entry = tk.Entry(root)
        self.update_off_site_location_entry.pack()


        tk.Label(root, text="Specialvare Kategori (Optional)").pack()
        self.update_category_entry = tk.Entry(root)
        self.update_category_entry.pack()

        tk.Button(root, text="Opdater", command=self.update_item).pack()

        # **Fjern vare**
        tk.Label(root, text="Fjern vare").pack()
        self.remove_name_entry = tk.Entry(root)
        self.remove_name_entry.pack()
        tk.Button(root, text="Fjern", command=self.remove_item).pack()

    # **Metoder til at håndtere handlinger**
    def search_item(self):
        """ Finder varer baseret på input fra søgefeltet """
        name = self.search_entry.get()
        results = self.controller.search_item(name)
        self.display_results(results)

    def show_all_items(self):
        """ Viser alle varer i lageret """
        self.display_results(self.controller.get_all_items())

    def add_item(self):
        """Tilføjer en ny vare til lageret."""
        name = self.name_entry.get()
        quantity = self.amount_entry.get()
        location = self.location_entry.get()
        category = self.category_entry.get()
        self.controller.add_item(name, quantity, location, category if category.strip() != "" else None)
        self.show_all_items()

    def update_item(self):
        """ Opdaterer en vares antal  """
        name = self.update_name_entry.get()
        new_quantity = self.update_amount_entry.get()
        new_off_site_location = self.update_off_site_location_entry.get()
        new_category = self.update_category_entry.get()
        print(new_category)
        self.controller.update_item(name, new_quantity, new_off_site_location, new_category)
        self.show_all_items()

    def remove_item(self):
        """ Fjerner en vare fra lageret """
        name = self.remove_name_entry.get()
        self.controller.remove_item(name)
        self.show_all_items()

    def display_results(self, results):
        """ Viser søgeresultater eller alle varer i listeboksen """
        self.result_listbox.delete(0, tk.END)  # Ryd listeboks
        for item in results:
            self.result_listbox.insert(tk.END, str(item))  # Indsæt hver vare i GUI-listen
