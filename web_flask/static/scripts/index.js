/*******************************************************************************************/
// DYNAMIC DISPLAY // 
/*******************************************************************************************/
const header = document.querySelector("#header");
const sections = document.querySelectorAll('section');

// Add an event listener for the scroll event
/*******************************************************************************************/
// ACTIVE NAVIGATION LINK TRACKING ON SCROLL // 
/*******************************************************************************************/
window.addEventListener('scroll', function() {
  var navButtons = document.querySelectorAll('.nav-btn');
  // var sections = document.querySelectorAll('section');
  // Check if the page has been scrolled down by 100 pixels or more
  if (window.scrollY >= 100) {
      header.classList.add("height");
  } else {
      header.classList.remove("height");
  }
  // sections.forEach(function(section, index) {
  //   var rect = section.getBoundingClientRect();
  //   if (rect.top <= (window.innerHeight / 2) && (rect.bottom >= window.innerHeight / 2) || window.scrollY === 0) { 
  //       navButtons.forEach(function(btn) {
  //       btn.classList.remove('active');
  //     });
  //     if (navButtons[index]) {
  //       navButtons[index].classList.add('active');
  //     }
  //   }
  // });
  
  // Remove active class from all navigation buttons when scrolled back to the top
  // if (window.scrollY === 0) {
  //   navButtons.forEach(function(btn) {
  //     btn.classList.remove('active');
  //   });
  // }
  // ADD ANIMATION ON PAGE SCROLL TO VIEWPORT
  sections.forEach((event)=>{
    let top = window.scrollY;
    let offset = event.offsetTop - 150;
    let height = event.offsetHeight;

    if (top >= offset && top < offset + height){
      event.classList.add('show-animate')
    }
    else {
      event.classList.remove('show-animate')
    }
  });
});

/*******************************************************************************************/
// END OF ACTIVE NAVIGATION LINK TRACKING ON SCROLL // 
/*******************************************************************************************/

/*******************************************************************************************/
// PAGE SMOOTH SCROLL // 
/*******************************************************************************************/
var navLinks = document.querySelectorAll('a.nav-btn');
navLinks.forEach((links)=>{
  links.addEventListener('click', (e)=>{
    e.preventDefault();
    var target = document.querySelector(links.getAttribute('href'));
    if(target.getAttribute('id' === 'home')){
      window.scrollTo({top:0, behavior:'smooth'});
    }
    else{
      target.scrollIntoView({behavior:'smooth'})
    }
  });
});


/*******************************************************************************************/
// END OF PAGE SMOOTH SCROLL // 
/*******************************************************************************************/


/*******************************************************************************************/
// OWL CAROUSEL // 
/*******************************************************************************************/
$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
        items:1,
        loop:true,
        nav:true,
        dots:true,
        autoplay:true,
        autoplaySpeed:1000,
        smartSpeed:1500,
        autoplayHoverPause:false
    });
});
/*******************************************************************************************/
// END OF OWL CAROUSEL // 
/*******************************************************************************************/
/*******************************************************************************************/
// Feature Navigation Dropdown // 
/*******************************************************************************************/
const features = document.querySelectorAll('#dropdown');
features.forEach((event)=>{
  event.addEventListener('click', ()=>{
    const featureDropdown = document.querySelector('#featureDropdown');
    const solutionDropdown = document.querySelector('#solutionDropdown');
    

    if (event.classList.contains('features')) {
      featureDropdown.classList.toggle('showDropdown');
    } else {
      solutionDropdown.classList.toggle('showDropdown');
    }
    
    // Toggle the chevron icon
    const bx = event.querySelector('.bx');
    if (bx.classList.contains('bx-chevron-down')) {
      bx.classList.toggle('bx-chevron-up');
    }

    // Close the other dropdown if it's open
    if (event.classList.contains('features') && solutionDropdown.classList.contains('showDropdown')) {
      solutionDropdown.classList.remove('showDropdown');
      const solutionBx = document.querySelector('.solution .bx');
      solutionBx.classList.remove('bx-chevron-up');
    } else if (!event.classList.contains('features') && featureDropdown.classList.contains('showDropdown')) {
      featureDropdown.classList.remove('showDropdown');
      const featureBx = document.querySelector('.features .bx');
      featureBx.classList.remove('bx-chevron-up');
    }
  })
})