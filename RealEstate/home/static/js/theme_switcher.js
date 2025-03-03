// Access the mode toggle button and icons
const modeToggle = document.getElementById('mode-toggle');
const sunIcon = document.getElementById('sun-icon');
const moonIcon = document.getElementById('moon-icon');
const body = document.body;

// Check the current mode from localStorage to persist the choice across page reloads
if (localStorage.getItem('mode') === 'dark') {
    body.classList.add('dark-mode');
    sunIcon.style.display = 'none';
    moonIcon.style.display = 'inline-block';
} else {
    body.classList.add('light-mode');
    sunIcon.style.display = 'inline-block';
    moonIcon.style.display = 'none';
}

// Toggle the mode on button click
modeToggle.addEventListener('click', () => {
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        sunIcon.style.display = 'inline-block';
        moonIcon.style.display = 'none';
        localStorage.setItem('mode', 'light');
    } else {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'inline-block';
        localStorage.setItem('mode', 'dark');
    }
});
