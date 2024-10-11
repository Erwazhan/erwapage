// Make each window draggable
document.querySelectorAll('.window, .window_big, .window_gallery').forEach(window => {
    let titleBar = window.querySelector('.title-bar');
    let closeButton = window.querySelector('button[aria-label="Close"]'); // Get the Close button by aria-label
    let isDragging = false;
    let offsetX, offsetY;

    // Enable dragging when mousedown on the title bar
    window.addEventListener('mousedown', function(e) {
        // Allow interaction with the window, e.g., clicking buttons, dragging, etc.
        if (e.target === titleBar || titleBar.contains(e.target)) {
            isDragging = true;
            offsetX = e.clientX - window.offsetLeft;
            offsetY = e.clientY - window.offsetTop;

            // Prevent text selection or unwanted interaction during dragging
            e.preventDefault();
        }
    });

    // Stop dragging on mouseup
    document.addEventListener('mouseup', function() {
        isDragging = false;
    });

    // Move the window on mousemove when dragging
    document.addEventListener('mousemove', function(e) {
        if (isDragging) {
            window.style.left = `${e.clientX - offsetX}px`;
            window.style.top = `${e.clientY - offsetY}px`;
        }
    });

    // Close the window when the "Close" button is clicked
    closeButton.addEventListener('click', function() {
        window.style.display = 'none'; // Hide the window
    });
});

// Display the current time
var today = new Date();
document.getElementById('time').innerHTML = today;
