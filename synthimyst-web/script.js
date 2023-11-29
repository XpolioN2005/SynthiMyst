const navBtn = document.getElementById("menu")

navBtn.addEventListener("click", function () {
    if (!navBtn.className.match("hidden")) {
        navBtn.classList.toggle("hidden")
    }
})