document.addEventListener ('DOMContentLoaded', ()=>{
    function inputAutoFill(id, inputValue) {
        const element = document.getElementById(id);
        if (inputValue === 'country') {
            element.value = geoplugin_countryName();
        } else if (inputValue === 'state') {
            element.value = geoplugin_region();
        } else if (inputValue === 'city') {
            element.value = geoplugin_city();
        }
    }
    inputAutoFill('country', 'country');
    inputAutoFill('state', 'state');
})

 // JavaScript to show/hide family fields based on user's choice
 const createFamilyRadio = document.getElementById('create_family');
 const joinFamilyRadio = document.getElementById('join_family');
 const newFamilyFields = document.getElementById('new_family_fields');
 const existingFamilyFields = document.getElementById('existing_family_fields');

 createFamilyRadio.addEventListener('change', function() {
     if (createFamilyRadio.checked) {
         newFamilyFields.style.display = 'block';
         existingFamilyFields.style.display = 'none';
     }
 });

 joinFamilyRadio.addEventListener('change', function() {
     if (joinFamilyRadio.checked) {
         existingFamilyFields.style.display = 'block';
         newFamilyFields.style.display = 'none';
     }
 });