const SLIDE_DELAY = 3000; // ms

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides((slideIndex += n));
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";
}

setInterval(() => {
  plusSlides(1);
}, SLIDE_DELAY);

// Scroll
const navcon = document.querySelector(".navcon");
window.addEventListener("scroll", () => {
  if (window.scrollY == 0) {
    navcon.classList.remove("shadow");
  } else {
    navcon.classList.add("shadow");
  }
});
