let box = document.getElementById("too__top");
box.addEventListener("click", function () {
  document.documentElement.scrollTop = 0;
});

window.addEventListener("scroll", function () {
  if (document.documentElement.scrollTop > 0) {
    box.style.display = "flex";
  } else {
    box.style.display = "none";
  }
});
