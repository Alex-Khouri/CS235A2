


function show(ID) {
    document.getElementById(ID).classList.remove("hidden");
    document.getElementById(ID).classList.add("visible");
}
function hide(ID) {
    document.getElementById(ID).classList.remove("visible");
    document.getElementById(ID).classList.add("hidden");
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


function showTitleSubmenu() {
    show("TitleSubmenu")
    hide("GenreSubmenu")
    hide("ActorSubmenu")
    hide("DirectorSubmenu")
}
function showGenreSubmenu() {
    hide("TitleSubmenu")
    show("GenreSubmenu")
    hide("ActorSubmenu")
    hide("DirectorSubmenu")
}
function showActorSubmenu() {
    hide("TitleSubmenu")
    hide("GenreSubmenu")
    show("ActorSubmenu")
    hide("DirectorSubmenu")
}
function showDirectorSubmenu() {
    hide("TitleSubmenu")
    hide("GenreSubmenu")
    hide("ActorSubmenu")
    show("DirectorSubmenu")
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


// function openDropdownMenu(dropdownContentID) {
//     let element = document.getElementById(dropdownContentID);
//     if (element.style.display === "block") {
//         element.style.display = "none";
//     } else {
//         element.style.display = "block";
//     }
//     let dropdowns = document.getElementsByClassName("dropdown-content");
//     for (let dropdown of dropdowns) {
//         if (dropdown.id !== dropdownContentID) {
//             dropdown.style.display = "none";
//         }
//     }
// }
// window.onclick = function(event) {
//     if (!event.target.matches('.dropbtn')) {
//         let dropdowns = document.getElementsByClassName("dropdown-content");
//         for (let dropdown of dropdowns) {
//             dropdown.style.display = "none";
//         }
//     }
// }


