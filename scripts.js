function fetchOfficerInformation() {
    const organizationName = document.getElementById('organizationName').value;

    if (organizationName.trim() === '') {
        alert('Please enter an organization name.');
        return;
    }

    // Assuming your server endpoint is hosting the Python script
    const endpoint = `/your-python-script-endpoint?organization=${encodeURIComponent(organizationName)}`;

    fetch(endpoint)
        .then(response => response.json())
        .then(data => displayResult(data))
        .catch(error => console.error('Error:', error));
}

function displayResult(data) {
    const resultContainer = document.getElementById('result');
    resultContainer.innerHTML = '';

    if (!data) {
        resultContainer.innerHTML = 'Failed to retrieve officer information. Please try again.';
        return;
    }

    for (const [organization, officers] of Object.entries(data)) {
        resultContainer.innerHTML += `<h2>${organization}</h2>`;
        
        for (const [subtext, officerInfo] of Object.entries(officers)) {
            resultContainer.innerHTML += `<h3>${subtext}</h3>`;
            resultContainer.innerHTML += `<p>Role: ${subtext}</p>`;
            resultContainer.innerHTML += `<p>Name: ${officerInfo.name}</p>`;
            resultContainer.innerHTML += `<p>Email: ${officerInfo.email}</p>`;
        }
    }
}
