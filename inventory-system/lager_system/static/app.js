async function fetchItems() {
    const response = await fetch('/items');
    const data = await response.json();
    document.getElementById('itemsList').innerHTML = data.map(item => `<li class='p-2 border-b'>${item}</li>`).join('');
}

async function searchItem() {
    const query = document.getElementById('searchInput').value;
    const response = await fetch(`/search?query=${query}`);
    const data = await response.json();
    document.getElementById('itemsList').innerHTML = data.map(item => `<li class='p-2 border-b'>${item}</li>`).join('');
}

async function addItem() {
    const name = document.getElementById('itemName').value;
    const quantity = document.getElementById('itemQuantity').value;
    const location = document.getElementById('itemLocation').value;
    await fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ name, quantity, location })
    });
    fetchItems();
}

async function updateItem() {
    const name = document.getElementById('updateName').value;
    const new_quantity = document.getElementById('updateQuantity').value;
    const new_off_site_location = document.getElementById('updateLocation').value;
    await fetch('/update', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ name, new_quantity, new_off_site_location })
    });
    fetchItems();
}

async function removeItem() {
    const name = document.getElementById('removeName').value;
    await fetch('/remove', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ name })
    });
    fetchItems();
}

fetchItems();
