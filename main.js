

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