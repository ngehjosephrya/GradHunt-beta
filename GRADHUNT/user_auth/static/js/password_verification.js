window.addEventListener('DOMContentLoaded', function() {
    var signupForm = document.querySelector('form');
    signupForm.addEventListener('submit', function(event) {
      var password1 = document.getElementById('password1').value;
      var password2 = document.getElementById('password2').value;

      if (password1 !== password2) {
        event.preventDefault();
        alert('Passwords do not match!');
      }
    });
  });