var imagecount = 1;
var image;

function start() {
  var btndown = document.getElementById("down");
  var btnup = document.getElementById("up");
  image = document.querySelect(".picture img");

  btndown.addEventListener("click", moreThanOne);
  btnup.addEventListener("click", lessThanNine);
}

let moreThanOne = function () {
  if (imagecount > 1) {
    imagecount--;
    image.setAttribute("src", imagecount + ".png");
  }
};

let lessThanNine = function () {
  if (imagecount < 6) {
    imagecount++;
    image.setAttribute("src", imagecount + ".png");
  }
};

window.onload = start;
