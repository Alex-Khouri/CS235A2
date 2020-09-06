

function login() {
    showMainWindow()
}

function register() {
    showMainWindow()
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