// Base URL of your API
const BASE_URL = 'http://127.0.0.1:8000/api';  

// REGISTER
if (document.getElementById('registerForm')) {
  document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const res = await fetch(`${BASE_URL}/register/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value
      })
    });
    const data = await res.json();
    alert("Registered successfully");
    window.location.href = "login.html";
  });
}

// LOGIN
if (document.getElementById('loginForm')) {
  document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const res = await fetch(`${BASE_URL}/token/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    });
    const data = await res.json();
    if (data.access) {
      localStorage.setItem('token', data.access);
      alert("Login successful");
      window.location.href = "index.html";
    } else {
      alert("Login failed");
    }
  });
}