


function show(ID) {
    document.getElementById(ID).style.display = "block";
}
function hide(ID) {
    document.getElementById(ID).style.display = "none";
}


function showMainWindow() {
    show("MainWindow")
    hide("LoginWindow")
    hide("RegisterWindow")
}
function showLoginWindow() {
    hide("MainWindow")
    show("LoginWindow")
    hide("RegisterWindow")
}
function showRegisterWindow() {
    hide("MainWindow")
    hide("LoginWindow")
    show("RegisterWindow")
}


function loginUser() {
    showMainWindow()
    hide("LoginPanel")
    show("LogoutPanel")
    hide("RegisterPanel")
}
function logoutUser() {
    show("LoginPanel")
    hide("LogoutPanel")
    show("RegisterPanel")
}
function registerUser() {
    showMainWindow()
    hide("LoginPanel")
    show("LogoutPanel")
    hide("RegisterPanel")
}


let dropdownBtn = document.querySelector('.menu-btn');
let menuContent = document.querySelector('.menu-content');
dropdownBtn.addEventListener('click',()=>{
    if (menuContent.style.display===""){
        menuContent.style.display="block";
    } else {
        menuContent.style.display="";
    }
});
window.onclick = function(event) {
    if (!event.target.matches('.menu-btn')) {
        let dropdowns = document.getElementsByClassName("menu-content");
        for (let dropdown of dropdowns) {
            dropdown.style.display = "";
        }
    }
}


