// Set default values
const defaultTreble = 0.5;
const defaultMid = 0.5;
const defaultBass = 0.5;
const defaultR1 = 250000;
const defaultR2 = 1000000;
const defaultR3 = 25000;
const defaultR4 = 56000;
const defaultC1 = 0.00000000025;
const defaultC2 = 0.000000022;
const defaultC3 = 0.000000022;

// Initial chart data
let currentData = {
    w: [],  // Frequencies
    mag: [], // Magnitude
};

// Initialize the chart
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: currentData.w,
        datasets: [
            {
                label: 'Magnitude',
                data: currentData.mag,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
                fill: false, // No filling under the line
            },
        ],
    },
    options: {
        responsive: true,
        scales: {
            x: {
                type: 'logarithmic', // Set x-axis to logarithmic scale
                title: {
                    display: true,
                    text: 'Frequency (Hz)', // X-axis label
                },
                min: 10,
                max: 100000,
                ticks: {
                    callback: function(value) {
                        // Show only powers of 10 on the x-axis
                        return [10, 100, 1000, 10000, 100000].includes(value) ? value : '';
                    },
                },
                grid: {
                    drawOnChartArea: false // Optional: avoid drawing grid lines on chart area
                }
            },
            y: {
                min: -25, // Set y-axis minimum
                max: 0,   // Set y-axis maximum
                title: {
                    display: true,
                    text: 'Magnitude (dB)', // Y-axis label
                },
                beginAtZero: false, // Start below zero
            }
        }
    }
});

// Function to update the chart
function updateChart(w, mag) {
    myChart.data.labels = w;
    myChart.data.datasets[0].data = mag; // Magnitude
    myChart.update();
}

// Initialize chart with default values
updateToneResponse(defaultTreble, defaultMid, defaultBass, defaultR1, defaultR2, defaultR3, defaultR4, defaultC1, defaultC2, defaultC3);

// Event listeners for sliders and text inputs
document.querySelectorAll('.slider, input[type="text"]').forEach(function(element) {
    element.addEventListener('input', function() {
        // Retrieve values from sliders
        let treble = document.getElementById('slider1').value;
        let mid = document.getElementById('slider2').value;
        let bass = document.getElementById('slider3').value;

        // Send data to the backend
        updateToneResponse(treble, mid, bass, defaultR1, defaultR2, defaultR3, defaultR4, defaultC1, defaultC2, defaultC3);
    });
});

// Function to send data to the backend
function updateToneResponse(t, m, l, R1, R2, R3, R4, C1, C2, C3) {
    fetch('/update-tone-response/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({
            treble: t,
            mid: m,
            bass: l,
            R1: R1,
            R2: R2,
            R3: R3,
            R4: R4,
            C1: C1,
            C2: C2,
            C3: C3
        })
    }).then(response => response.json())
      .then(data => {
          // Update the chart with the new data
          updateChart(data.w, data.mag);
      });
}

// Function to get the CSRF token
function getCSRFToken() {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.substring('csrftoken='.length, cookie.length);
        }
    }
    return '';
}

// Event listener for the update button
document.getElementById('update_vals').addEventListener('click', function() {
    // Retrieve values from resistor inputs
    let R1 = document.getElementById('R1').value;
    let R2 = document.getElementById('R2').value;
    let R3 = document.getElementById('R3').value;
    let R4 = document.getElementById('R4').value;

    // Retrieve values from capacitor inputs
    let C1 = document.getElementById('C1').value;
    let C2 = document.getElementById('C2').value;
    let C3 = document.getElementById('C3').value;

    // Use the current treble, mid, and bass values from sliders
    let treble = document.getElementById('slider1').value;
    let mid = document.getElementById('slider2').value;
    let bass = document.getElementById('slider3').value;

    // Send data to the backend
    updateToneResponse(treble, mid, bass, R1, R2, R3, R4, C1, C2, C3);
});
