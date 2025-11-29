const navbar = document.querySelector('.navbar__container')

window.addEventListener('scroll', function() {
    if (this.window.scrollY > 200) {
        navbar.classList.add('active')
    } else {
        navbar.classList.remove('active')
    }
})

const checkbox = document.querySelector('.checbox__hamburger')
const sidebar = document.querySelector('.nav__menu')

checkbox.addEventListener('change', function() {
    if (checkbox.checked) {
        sidebar.classList.add('active')
    } else {
        sidebar.classList.remove('active')
    }
})