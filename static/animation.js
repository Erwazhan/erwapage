document.addEventListener("DOMContentLoaded", function() {
  AOS.init({
    duration: 1200,  // Duration of the animation in milliseconds
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Select all elements with class 'window' and 'window_big'
  const windows = document.querySelectorAll('.window, .window_big');

  // Add the 'show' class to each window with a delay
  windows.forEach((window, index) => {
      setTimeout(() => {
          window.classList.add('show');
      }, index * 200); // Adjust delay as needed
  });
});

