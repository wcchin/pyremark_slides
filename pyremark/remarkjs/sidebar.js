
function openNav() {
  document.getElementById("mySidenav").style.width = "300px";
  document.getElementById("menu-toggle").classList.toggle("change");
  document.getElementById('menu-toggle').setAttribute( "onClick", "closeNav(this)" );
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("menu-toggle").classList.toggle("change");
  document.getElementById('menu-toggle').setAttribute( "onClick", "openNav(this)" );
}
