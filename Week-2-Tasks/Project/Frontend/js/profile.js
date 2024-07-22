document.getElementById('profile-icon').addEventListener('click', function() {
    var menu = document.getElementById('profile-menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
});

document.getElementById('profile-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Simple form validation
    const birthdate = document.getElementById('birthdate').value;
    const joiningDate = document.getElementById('joining-date').value;
    const position = document.getElementById('position').value.trim();

    if (!birthdate || !joiningDate || !position) {
        alert('Please fill in all the fields.');
        return;
    }

    // Update profile (for now, just log the data)
    console.log({
        birthdate,
        joiningDate,
        position
    });

    alert('Profile updated successfully.');
});
