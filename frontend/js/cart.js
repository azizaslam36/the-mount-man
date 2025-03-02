let cart = JSON.parse(localStorage.getItem("cart")) || [];

function addToCart(name, price, image) {
    let existingItem = cart.find(item => item.name === name);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({ name, price, image, quantity: 1 });
    }

    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Product added to cart!");
}

// Load cart items into the table on `cart.html`
document.addEventListener("DOMContentLoaded", () => {
    let cartTableBody = document.querySelector("#cart tbody");
    let cartSubtotal = document.getElementById("cartSubtotal");
    let cartTotal = document.getElementById("cartTotal"); // Added total ID
    let subtotal = 0;

    cartTableBody.innerHTML = ""; // Clear existing items

    cart.forEach((item, index) => {
        let itemTotal = item.price * item.quantity;
        subtotal += itemTotal;

        cartTableBody.innerHTML += `
            <tr>
                <td><a href="#" onclick="removeFromCart(${index})"><i class="fa-solid fa-circle-xmark"></i></a></td>
                <td><img src="${item.image}" alt="${item.name}" width="50"></td>
                <td>${item.name}</td>
                <td>₹${item.price}</td>
                <td><input type="number" value="${item.quantity}" min="1" onchange="updateQuantity(${index}, this.value)"></td>
                <td>₹${itemTotal}</td>
            </tr>
        `;
    });

    // Update the Cart Subtotal and Total
    cartSubtotal.innerText = `₹${subtotal}`;
    cartTotal.innerText = `₹${subtotal}`; // Total is same as subtotal since shipping is free
});

// Remove an item from the cart
function removeFromCart(index) {
    cart.splice(index, 1);
    localStorage.setItem("cart", JSON.stringify(cart));
    window.location.reload(); // Refresh the page
}

// Update the quantity of an item
function updateQuantity(index, quantity) {
    if (quantity < 1) return;
    cart[index].quantity = parseInt(quantity);
    localStorage.setItem("cart", JSON.stringify(cart));
    window.location.reload();
}

// Clear the entire cart
function clearCart() {
    localStorage.removeItem("cart");
    window.location.reload();
}
