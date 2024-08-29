document.getElementById('profile-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const profileName = document.getElementById('profile_name').value;
    fetch('/profile-info', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ profile_name: profileName })
    })
    .then(response => response.json())
    .then(data => {
        const profileInfoDiv = document.getElementById('profile-info');
        if (data.status === 'success') {
            profileInfoDiv.innerHTML = `
                <h2>${data.profile_info.fullname} (@${data.profile_info.username})</h2>
                <p><strong>Bio:</strong> ${data.profile_info.bio}</p>
                <p><strong>Followers:</strong> ${data.profile_info.followers}</p>
                <p><strong>Following:</strong> ${data.profile_info.following}</p>
                <p><strong>Posts:</strong> ${data.profile_info.posts}</p>
            `;
        } else {
            profileInfoDiv.innerHTML = `<p style="color: red;">${data.message}</p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('profile-info').innerHTML = `<p style="color: red;">An error occurred. Please try again later.</p>`;
    });
});
