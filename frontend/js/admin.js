document.getElementById("adminLoginForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
  
    const response = await fetch("http://localhost:5000/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });
  
    const data = await response.json();
  
    if (response.ok) {
      localStorage.setItem("adminToken", data.token);
      alert("Login Successful!");
      window.location.href = "admin-dashboard.html"; // Redirect to admin panel
    } else {
      alert(data.message);
    }
  });
  