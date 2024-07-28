document.getElementById("show-signup").addEventListener("click", function () {
  document.getElementById("flip-card-inner").style.transform =
    "rotateY(180deg)";
});

document.getElementById("show-login").addEventListener("click", function () {
  document.getElementById("flip-card-inner").style.transform = "rotateY(0deg)";
});
