// static/layout.js
function injectLayout() {
  fetch('static/header.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('header').innerHTML = data;
    });

  fetch('static/footer.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('footer').innerHTML = data;
    });
}

document.addEventListener('DOMContentLoaded', injectLayout);
