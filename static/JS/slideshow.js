var slideIndex = 0;
function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1 }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
  setTimeout(showSlides, 5000); // Change image every 2 seconds
}


function orderplaced(){
  document.getElementById("placeorder");
  window.location.pathname="placeorder";
}

function Submitorder(){
  document.getElementById('Submitorder');
  window.location.pathname="shippingpage";
}

function add_address(){
  document.getElementById('registerform').style.display = 'block';
}

window.onload = function year(){
  const n = new Date();
  const y = n.getFullYear();
  document.getElementById('copyright').innerHTML = "©." + y + ".All Rights Reserved.";
}



