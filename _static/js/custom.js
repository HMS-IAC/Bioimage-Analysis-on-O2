document.addEventListener("DOMContentLoaded", function() {
    const theme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", theme);

    const themeToggle = document.querySelector("#theme-toggle");
    if (themeToggle) {
        themeToggle.addEventListener("click", function() {
            const currentTheme = document.documentElement.getAttribute("data-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";
            document.documentElement.setAttribute("data-theme", newTheme);
            localStorage.setItem("theme", newTheme);
        });
    }
});
