document.addEventListener("DOMContentLoaded", function () {
    console.log("✅script.js!");

    const toggleBtn = document.getElementById("dark-mode-toggle");
    const body = document.body;

    if (!toggleBtn) {
        console.error("❌");
        return;
    }

    const currentMode = getCookie("darkMode");
    console.log("🔍:", currentMode);

    if (currentMode === "enabled") {
        body.classList.add("dark-mode");
        console.log("🌙");
    } else {
        console.log("☀️ ");
    }

   
    toggleBtn.addEventListener("click", function () {
        console.log("🌙 Done!");

        body.classList.toggle("dark-mode");

        if (body.classList.contains("dark-mode")) {
            setCookie("darkMode", "enabled", 30);
            console.log("✅!");
        } else {
            setCookie("darkMode", "disabled", 30);
            console.log("☀️");
        }
    });


    function setCookie(name, value, days) {
        let expires = "";
        if (days) {
            let date = new Date();
            date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + value + "; path=/" + expires;
    }

    function getCookie(name) {
        let nameEQ = name + "=";
        let ca = document.cookie.split(";");
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i].trim();
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const hiddenElements = document.querySelectorAll(".hidden");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }
        });
    }, { threshold: 0.2 });

    hiddenElements.forEach(el => observer.observe(el));
});
