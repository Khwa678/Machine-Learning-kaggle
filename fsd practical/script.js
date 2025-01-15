
// Select the button and the box
const startButton = document.getElementById('startButton');
const titleBox = document.getElementById('titleBox');

// Add a click event listener to the button
startButton.addEventListener('click', () => {
    // Toggle the visibility of the title box
    if (titleBox.style.display === 'none' || titleBox.style.display === '') {
        titleBox.style.display = 'block'; // Show the box
    } else {
        titleBox.style.display = 'none'; // Hide the box
    }
});

