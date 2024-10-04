let zIndexCounter = 1; // Initialize a global z-index counter

// Make each window draggable and bring the clicked one to the front
document.querySelectorAll('.window, .window_big, .window_gallery').forEach(window => {
    let titleBar = window.querySelector('.title-bar');
    let closeButton = window.querySelector('button[aria-label="Close"]'); // Get the Close button by aria-label
    let isDragging = false;
    let offsetX, offsetY;

    // Bring the window to the front on mousedown, before any other interaction
    window.addEventListener('mousedown', function(e) {
        // Bring the clicked window to the front by updating its z-index
        this.style.zIndex = ++zIndexCounter;

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

var today = new Date();
document.getElementById('time').innerHTML=today;