// Function to update the clock
function updateClock() {
  var now = new Date();  // Get the current date and time
  var hours = now.getHours();
  var minutes = now.getMinutes();
  var seconds = now.getSeconds();

  // Add a leading zero to minutes and seconds if they are less than 10
  if (minutes < 10) {
      minutes = '0' + minutes;
  }
  if (seconds < 10) {
      seconds = '0' + seconds;
  }

  // Format the time in HH:MM:SS format
  var timeString = hours + ':' + minutes + ':' + seconds;

  // Display the time in the HTML element with id 'clock'
  document.getElementById('clock').textContent = timeString;
}

// Update the clock every second
setInterval(updateClock, 1000);

// Call the function initially to avoid delay
updateClock();

