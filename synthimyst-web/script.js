const navBtn = document.getElementById("menu")
const navclose = document.getElementById("nav-close")
const menu = document.getElementById("other-navbar");

navBtn.addEventListener("click", function () {
    if (menu.className.match("hidden")) {
        menu.classList.remove("hidden");
        navBtn.classList.toggle("hidden");
        menu.classList.add("visible")
    }
})

navclose.addEventListener("click", function () {
    if (menu.className.match("visible")) {
        menu.style.opacity = 1
        menu.classList.remove("visible");
        menu.classList.add("hidden")

        setTimeout(function(){
            navBtn.classList.toggle("hidden")
        }, 500)
    }
})