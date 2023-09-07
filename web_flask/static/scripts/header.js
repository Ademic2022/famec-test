$('.ui.checkbox')
  .checkbox();

$('select.dropdown')
  .dropdown();

$('.message .close').on('click', function() {
  $(this)
    .closest('.message')
    .transition('fade');
});
/*******************************************************************************************/
// PASSWORD VISIBILITY // 
/*******************************************************************************************/
function toggleVisibility(event) {
    event.preventDefault(); // Prevent default behavior of the click event
    const visibilityIcon = document.querySelector('i#toggleVisibility');
    const passwordInput = document.querySelector("#passwordInput");
    let checkVisibility = visibilityIcon.classList.contains('bx-hide');
    
    if (checkVisibility && passwordInput.type === 'password'){
        visibilityIcon.classList.remove('bx-hide');
        visibilityIcon.classList.add('bx-show');
        passwordInput.type = 'text';
    } else {
        visibilityIcon.classList.remove('bx-show');
        visibilityIcon.classList.add('bx-hide');
        passwordInput.type = 'password';
    }
}

document.getElementById('toggleVisibility').addEventListener('click', toggleVisibility);
