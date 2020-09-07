

function loginUser() {
    showMainWindow()
    document.getElementById("LoginPanel").style.display = "none";
    document.getElementById("LogoutPanel").style.display = "block";
    document.getElementById("RegisterPanel").style.display = "none";
}

function logoutUser() {
    document.getElementById("LoginPanel").style.display = "block";
    document.getElementById("LogoutPanel").style.display = "none";
    document.getElementById("RegisterPanel").style.display = "block";
}

function registerUser() {
    showMainWindow()
    document.getElementById("LoginPanel").style.display = "none";
    document.getElementById("LogoutPanel").style.display = "block";
    document.getElementById("RegisterPanel").style.display = "none";
}

function showMainWindow() {
    document.getElementById("MainWindow").style.display = "block";
    document.getElementById("LoginWindow").style.display = "none";
    document.getElementById("RegisterWindow").style.display = "none";
}

function showLoginWindow() {
    document.getElementById("MainWindow").style.display = "none";
    document.getElementById("LoginWindow").style.display = "block";
    document.getElementById("RegisterWindow").style.display = "none";
}

function showRegisterWindow() {
    document.getElementById("MainWindow").style.display = "none";
    document.getElementById("LoginWindow").style.display = "none";
    document.getElementById("RegisterWindow").style.display = "block";
}

/* DROPDOWN MENU */
// Toggle dropdown content visibility when user clicks button
function openDropdownMenu(dropdownContentID) {
    let element = document.getElementById(dropdownContentID);
    if (element.style.display === "block") {
        element.style.display = "none";
    } else {
        element.style.display = "block";
    }
    let dropdowns = document.getElementsByClassName("dropdown-content");
    for (let dropdown of dropdowns) {
        if (dropdown.id !== dropdownContentID) {
            dropdown.style.display = "none";
        }
    }
}
// Close dropdown if user clicks outside menu
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        for (let dropdown of dropdowns) {
            dropdown.style.display = "none";
        }
    }
}

