
function openModal() {
  // Get the modal
  var modal = document.getElementById("myModal");
  modal.style.display = "block";

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];
  span.onclick = function() {
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
}

function closeModal() {
  document.getElementById("myModal").style.display = "none";
}



window.addEventListener("keydown", function (event) {
  if (event.key === 's') {
    if (document.getElementById("myModal").style.display === "block") {
      closeModal();
    } else {
      openModal();
    }
  }
}, true);