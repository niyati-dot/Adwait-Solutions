document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.navmenu a');
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentPath === linkPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});
document.addEventListener("DOMContentLoaded", function() {
  const newsletterForm = document.getElementById('newsletter-form');
  const messageContainer = document.querySelector('.alert');

  newsletterForm.addEventListener('submit', function(event) {
      event.preventDefault();  // Prevent the default form submission
      const formData = new FormData(this);

      messageContainer.innerHTML = ''; // Clear previous messages
      messageContainer.className = ''; // Reset message class

      fetch(this.action, {
          method: 'POST',
          body: formData,
      })
      .then(response => response.json())
      .then(data => {
          // Reset the form regardless of the outcome
          this.reset();

          if (data.success) {
              messageContainer.innerHTML = `<i class="bi bi-check-circle"></i> ${data.message}`; // Success message
              messageContainer.className = 'alert alert-success'; // Set success class
          } else {
              messageContainer.innerHTML = `<i class="bi bi-exclamation-triangle"></i> ${data.message || data.errors.email[0]}`; // Error message
              messageContainer.className = 'alert alert-danger'; // Set error class
          }

          // Remove the message after 5 seconds
          setTimeout(() => {
              messageContainer.innerHTML = '';
              messageContainer.className = ''; // Reset the class
          }, 5000);
      })
      .catch(error => {
          messageContainer.innerHTML = 'An error occurred. Please try again.';
          messageContainer.className = 'alert alert-danger'; // Set error class

          // Reset the form in case of an error
          this.reset();
      });
  });
});

document.addEventListener("DOMContentLoaded", function() {
    const contactForm = document.getElementById('contact-form');
    const msgContainer = document.querySelector('.inquiry-alert');
  
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the default form submission
        const formData = new FormData(this);
  
        msgContainer.innerHTML = ''; // Clear previous messages
        msgContainer.className = ''; // Reset message class
  
        fetch(this.action, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Reset the form regardless of the outcome
            this.reset();
  
            if (data.success) {
                // Success message
                msgContainer.innerHTML = `<i class="bi bi-check-circle"></i> ${data.message}`;
                msgContainer.className = 'inquiry-alert alert-success'; // Set success class
            } else {
                // Error message
                msgContainer.innerHTML = `<i class="bi bi-exclamation-triangle"></i> ${data.message || data.errors.email[0]}`;
                msgContainer.className = 'inquiry-alert alert-danger'; // Set error class
            }
  
            // Remove the message after 5 seconds
            setTimeout(() => {
                msgContainer.innerHTML = '';
                msgContainer.className = ''; // Reset the class
            }, 5000);
        })
        .catch(error => {
            msgContainer.innerHTML = 'An error occurred. Please try again.';
            msgContainer.className = 'inquiry-alert alert-danger'; // Set error class
  
            // Reset the form in case of an error
            this.reset();
        });
    });
  });
  