document.getElementById("productForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const name = document.getElementById("name").value;
    const price = document.getElementById("price").value;
    const image = document.getElementById("image").value;
    const description = document.getElementById("description").value;
  
    const response = await fetch("http://localhost:5000/api/products", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, price, image, description }),
    });
  
    if (response.ok) {
      alert("Product Added!");
      window.location.reload(); // Refresh the page
    } else {
      alert("Error adding product!");
    }
  });
  
  // Fetch and Display Products in Admin Panel
  fetch("http://localhost:5000/api/products")
    .then((res) => res.json())
    .then((data) => {
      let adminProducts = document.getElementById("adminProducts");
      adminProducts.innerHTML = ""; // Clear existing products
  
      data.forEach((product) => {
        adminProducts.innerHTML += `
          <div>
            <img src="${product.image}" width="100">
            <h3>${product.name}</h3>
            <p>₹${product.price}</p>
            <p>${product.description}</p>
            <button onclick="deleteProduct('${product._id}')">Delete</button>
          </div>
        `;
      });
    });
  
  // Delete Product
  async function deleteProduct(id) {
    const response = await fetch(`http://localhost:5000/api/products/${id}`, {
      method: "DELETE",
    });
  
    if (response.ok) {
      alert("Product Deleted!");
      window.location.reload(); // Refresh page
    } else {
      alert("Error deleting product!");
    }
  }
  