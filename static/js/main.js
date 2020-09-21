

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


function toggleBrowseTitles() {
    if (document.getElementById("BrowseTitles").style.display != "block") {
        show("BrowseTitles");
        document.getElementById("titlesHeading").innerHTML = "&#8595 Titles";
    }
    else {
        hide("BrowseTitles");
        document.getElementById("titlesHeading").innerHTML = "&#8594 Titles";
    }
}
function toggleBrowseGenres() {
    if (document.getElementById("BrowseGenres").style.display != "block") {
        show("BrowseGenres");
        document.getElementById("genresHeading").innerHTML = "&#8595 Genres";
    }
    else {
        hide("BrowseGenres");
        document.getElementById("genresHeading").innerHTML = "&#8594 Genres";
    }
}
function toggleBrowseDirectors() {
    if (document.getElementById("BrowseDirectors").style.display != "block") {
        show("BrowseDirectors");
        document.getElementById("directorsHeading").innerHTML = "&#8595 Directors";
    }
    else {
        hide("BrowseDirectors");
        document.getElementById("directorsHeading").innerHTML = "&#8594 Directors";
    }
}
function toggleBrowseActors() {
    if (document.getElementById("BrowseActors").style.display != "block") {
        show("BrowseActors");
        document.getElementById("actorsHeading").innerHTML = "&#8595 Actors";
    }
    else {
        hide("BrowseActors");
        document.getElementById("actorsHeading").innerHTML = "&#8594 Actors";
    }
}


function loginUser() {
    showMainWindow()
    hide("LoginPanel");
    show("LogoutPanel");
    hide("RegisterPanel");
}
function logoutUser() {
    show("LoginPanel");
    hide("LogoutPanel");
    show("RegisterPanel");
}
function registerUser() {
    showMainWindow();
    hide("LoginPanel");
    show("LogoutPanel");
    hide("RegisterPanel");
}



// DEPRECATED - Dropdown Browse Menu
// let browseButton = document.getElementById("BrowseButton");
// let browseContent = document.getElementById("BrowseContent");
// let titlesButton = document.getElementById("TitlesButton");
// let titlesContent = document.getElementById("TitlesContent");
// let genresButton = document.getElementById("GenresButton");
// let genresContent = document.getElementById("GenresContent");
// let directorsButton = document.getElementById("DirectorsButton");
// let directorsContent = document.getElementById("DirectorsContent");
// let actorsButton = document.getElementById("ActorsButton");
// let actorsContent = document.getElementById("ActorsContent");
// browseButton.addEventListener('click',()=>{
//     titlesContent.style.display="";
//     genresContent.style.display="";
//     directorsContent.style.display="";
//     actorsContent.style.display="";
//     if (browseContent.style.display===""){
//         browseContent.style.display="block";
//     } else {
//         browseContent.style.display="";
//     }
// });
// titlesButton.addEventListener('click',()=>{
//     genresContent.style.display="";
//     directorsContent.style.display="";
//     actorsContent.style.display="";
//     if (titlesContent.style.display===""){
//         titlesContent.style.display="block";
//     } else {
//         titlesContent.style.display="";
//     }
// });
// genresButton.addEventListener('click',()=>{
//     titlesContent.style.display="";
//     directorsContent.style.display="";
//     actorsContent.style.display="";
//     if (genresContent.style.display===""){
//         genresContent.style.display="block";
//     } else {
//         genresContent.style.display="";
//     }
// });
// directorsButton.addEventListener('click',()=>{
//     titlesContent.style.display="";
//     genresContent.style.display="";
//     actorsContent.style.display="";
//     if (directorsContent.style.display===""){
//         directorsContent.style.display="block";
//     } else {
//         directorsContent.style.display="";
//     }
// });
// actorsButton.addEventListener('click',()=>{
//     titlesContent.style.display="";
//     genresContent.style.display="";
//     directorsContent.style.display="";
//     if (actorsContent.style.display===""){
//         actorsContent.style.display="block";
//     } else {
//         actorsContent.style.display="";
//     }
// });

// window.onclick = function(event) {
//     if (!(event.target.matches('.menu-btn') || event.target.matches('.submenu-btn'))) {
//         let dropdowns = document.getElementsByClassName("menu-content");
//         for (let dropdown of dropdowns) {
//             dropdown.style.display = "";
//         }
//     }
// }


