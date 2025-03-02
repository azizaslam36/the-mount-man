const bar = document.getElementById("bar");
const close = document.getElementById("close");
const nav = document.getElementById("navbar");

if(bar){
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}
if(close){
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}

fetch("http://127.0.0.1:5000/api/products")
  .then(response => response.json())
  .then(data => console.log("Products:", data))
  .catch(error => console.error("Error fetching products:", error));


fetch("http://127.0.0.1:5000/api/products")
  .then((res) => res.json())
  .then((data) => {
    let productContainer = document.getElementById("products");
    productContainer.innerHTML = ""; // Clear existing products
    data.forEach((product) => {
      productContainer.innerHTML += `
        <div class="product">
          <img src="${product.image}" alt="${product.name}">
          <h3>${product.name}</h3>
          <p>₹${product.price}</p>
          <p>${product.description}</p>
          <button onclick="addToCart('${product.name}', ${product.price})">Add to Cart</button>
        </div>
      `;
    });
  });

  function addToCart(productId, name, price, image) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push({ id: productId, name, price, image });
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Added to cart!");
}

function displayCart() {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  let cartContainer = document.getElementById("cart-items");
  cartContainer.innerHTML = ""; // Clear previous items

  cart.forEach(item => {
      cartContainer.innerHTML += `
          <div class="cart-item">
              <img src="${item.image}" alt="${item.name}">
              <p>${item.name} - ₹${item.price}</p>
              <button onclick="removeItem(${item.id})">Remove</button>
          </div>
      `;
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const cartElement = document.getElementById("cart");

  if (!cartElement) {
    console.error("Cart element not found!");
    return;  // Stop execution if the cart element does not exist
  }

  function displayCart() {
    cartElement.innerHTML = "<p>Cart is working!</p>";
  }

  displayCart(); // Call function after checking element existence
});



displayCart();

