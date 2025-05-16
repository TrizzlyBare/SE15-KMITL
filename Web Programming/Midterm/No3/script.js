var imagecount = 1;
var image;

function start() {
  var btndown = document.getElementById("down");
  var btnup = document.getElementById("up");
  image = document.getElementById("picture").getElementsByTagName("img")[0];

  btndown.addEventListener("click", moreThanOne);
  btnup.addEventListener("click", lessThanNine);
}

let moreThanOne = function () {
  if (imagecount > 1) {
    imagecount--;
    image.setAttribute("src", "img/" + imagecount + ".png");
  }
};

let lessThanNine = function () {
  if (imagecount < 6) {
    imagecount++;
    image.setAttribute("src", "img/" + imagecount + ".png");
  }
};

window.addEventListener("load", start, false);
