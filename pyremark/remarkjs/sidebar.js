
function openNav() {
  document.getElementById("mySidenav").style.width = "300px";
  //document.getElementById("menu-toggle").classList.toggle("change");
  //document.getElementById('menu-toggle').setAttribute( "onClick", "closeNav(this)" );
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  //document.getElementById("menu-toggle").classList.toggle("change");
  //document.getElementById('menu-toggle').setAttribute( "onClick", "openNav(this)" );
}

window.addEventListener("keydown", function (event) {
  if (event.key === 'Escape') {
    if (document.getElementById("mySidenav").style.width === "300px") {
      closeNav();
    } else {
      openNav();
    }
  }
}, true);