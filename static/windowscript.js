// static/your_app/js/script.js
document.addEventListener("DOMContentLoaded", function() {
  // Get all close buttons
  const closeButtons = document.querySelectorAll('.title-bar-controls button[aria-label="Close"]');

  // Add click event listener to each close button
  closeButtons.forEach(function(button) {
      button.addEventListener("click", function() {
          // Find the closest window element by checking all relevant classes
          let windowElement = button.closest('.window');

          if (!windowElement) {
              // If not found, check for other window classes
              windowElement = button.closest('.window_big') ||
                              button.closest('.window_gallery') ||
                              button.closest('.window');
          }

          if (windowElement) {
              windowElement.style.display = "none";
          }
      });
  });
});

const panes = document.querySelectorAll('.window, .window_big, .window_gallery');

let z = 1

panes.forEach((window) => {
  const title = window.querySelector('.title-bar')
  const corner = window.querySelector('.corner')

  window.addEventListener('mousedown', () => {
    z = z + 1
    window.style.zIndex = z
  })

  title.addEventListener('mousedown', (event) => {
    window.classList.add('is-dragging')

    let l = window.offsetLeft
    let t = window.offsetTop

    let startX = event.pageX
    let startY = event.pageY

    const drag = (event) => {
      event.preventDefault()

      window.style.left = l + (event.pageX - startX) + 'px'
      window.style.top = t + (event.pageY - startY) + 'px'
    }

    const mouseup = () => {
      window.classList.remove('is-dragging')

      document.removeEventListener('mousemove', drag)
      document.removeEventListener('mouseup', mouseup)
    }

    document.addEventListener('mousemove', drag)
    document.addEventListener('mouseup', mouseup)
  })

  corner.addEventListener('mousedown', (event) => {
    let w = window.clientWidth
    let h = window.clientHeight

    let startX = event.pageX
    let startY = event.pageY

    const drag = (event) => {
      event.preventDefault()

      window.style.width = w + (event.pageX - startX) + 'px'
      window.style.height = h + (event.pageY - startY) + 'px'
    }

    const mouseup = () => {
      document.removeEventListener('mousemove', drag)
      document.removeEventListener('mouseup', mouseup)
    }

    document.addEventListener('mousemove', drag)
    document.addEventListener('mouseup', mouseup)
  })
})

var today = new Date();
document.getElementById('time').innerHTML=today;