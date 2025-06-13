const BASE_URL = 'http://127.0.0.1:8000/api';

document.addEventListener('DOMContentLoaded', () => {
  fetchNews();
  getCurrentUser();

  const form = document.getElementById('newsForm');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const title = document.getElementById('title').value;
      const content = document.getElementById('content').value;
      const token = localStorage.getItem('token');

      if (!token) {
        alert("Login required");
        return;
      }

      try {
        const res = await fetch(`${BASE_URL}/news/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({ title, content })
        });

        if (res.status === 201) {
          alert("News posted!");
          document.getElementById('title').value = '';
          document.getElementById('content').value = '';
          fetchNews();
        } else {
          const err = await res.json();
          alert("Failed to post news: " + JSON.stringify(err));
        }
      } catch (err) {
        alert("Error: " + err.message);
      }
    });
  }

  const logoutBtn = document.getElementById('logoutBtn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
      localStorage.removeItem('token');
      location.reload();
    });
  }
});

async function fetchNews() {
  try {
    const res = await fetch(`${BASE_URL}/news/`);
    if (!res.ok) throw new Error("Failed to fetch news");

    const newsList = await res.json();
    const container = document.getElementById('newsList');
    container.innerHTML = '';

    newsList.forEach(item => {
      container.innerHTML += `
        <div class="card mb-2">
          <div class="card-body">
            <h5>${item.title}</h5>
            <p>${item.content}</p>
          </div>
        </div>`;
    });
  } catch (err) {
    console.error(err);
    alert("Could not load news: " + err.message);
  }
}

async function getCurrentUser() {
  const token = localStorage.getItem('token');
  if (!token) return;

  try {
    const res = await fetch(`${BASE_URL}/user/`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (res.ok) {
      const data = await res.json();
      document.getElementById('greeting').innerText = `Hi, ${data.username}`;
      document.getElementById('authLinks').style.display = 'none';
      document.getElementById('userBox').style.display = 'flex';
    } else {
      console.warn('User not authenticated');
    }
  } catch (err) {
    console.error("Failed to fetch user:", err);
  }
}