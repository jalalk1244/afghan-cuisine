// function show_modal() {
//     theModal = document.getElementById('modal');
//     theModal.classList.add("show");
// }

function show_modal() {
    var x = document.getElementById("modal");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }