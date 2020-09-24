

function show(ID) {
    document.getElementById(ID).style.display = "block";
}
function hide(ID) {
    document.getElementById(ID).style.display = "none";
}


function showMainWindow() {
    show("MainWindow");
    hide("LoginWindow");
    hide("RegisterWindow");
}
function showLoginWindow() {
    hide("MainWindow");
    show("LoginWindow");
    hide("RegisterWindow");
}
function showRegisterWindow() {
    hide("MainWindow");
    hide("LoginWindow");
    show("RegisterWindow");
}
function toggleReviews(ID) {
    if (document.getElementById(ID).style.display != "block") {
        show(ID);
    } else {
        hide(ID);
    }
}
function toggleReviewForm(ID) {
    if (document.getElementById(ID).style.display != "block") {
        show(ID);
    } else {
        hide(ID);
    }
}


function loginUser() {
    showMainWindow()
    hide("LoginButton");
    show("LogoutButton");
    hide("RegisterButton");
}
function logoutUser() {
    show("LoginButton");
    hide("LogoutButton");
    show("RegisterButton");
}


function toggleBrowseTitles() {
    if (document.getElementById("BrowseTitles").style.display != "block") {
        show("BrowseTitles");
        document.getElementById("titlesHeading").innerHTML = "&#8595 Titles";
    } else {
        hide("BrowseTitles");
        document.getElementById("titlesHeading").innerHTML = "&#8594 Titles";
    }
}
function toggleBrowseGenres() {
    if (document.getElementById("BrowseGenres").style.display != "block") {
        show("BrowseGenres");
        document.getElementById("genresHeading").innerHTML = "&#8595 Genres";
    } else {
        hide("BrowseGenres");
        document.getElementById("genresHeading").innerHTML = "&#8594 Genres";
    }
}
function toggleBrowseDirectors() {
    if (document.getElementById("BrowseDirectors").style.display != "block") {
        show("BrowseDirectors");
        document.getElementById("directorsHeading").innerHTML = "&#8595 Directors";
    } else {
        hide("BrowseDirectors");
        document.getElementById("directorsHeading").innerHTML = "&#8594 Directors";
    }
}
function toggleBrowseActors() {
    if (document.getElementById("BrowseActors").style.display != "block") {
        show("BrowseActors");
        document.getElementById("actorsHeading").innerHTML = "&#8595 Actors";
    } else {
        hide("BrowseActors");
        document.getElementById("actorsHeading").innerHTML = "&#8594 Actors";
    }
}


switch(document.getElementById("AuthStatus").innerHTML) {
    case "logged in":
        loginUser();
        break;
    case "logged out":
        logoutUser();
        break;
    case "logging in":
        showLoginWindow();
        break;
    case "registering":
        showRegisterWindow();
        break;
    default:  // This case shouldn't be reached
        showMainWindow();
        console.log("WARNING: Invalid AuthStatus Value");
}