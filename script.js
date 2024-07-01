function getRecommendations() {
    var prefs = document.getElementById('userPrefs').value;
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({preferences: prefs})
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('results');
        resultDiv.innerHTML = '';  // Clear previous results
        data.forEach(job => {
            let content = `Title: ${job.title}<br>Description: ${job.description}<br><br>`;
            resultDiv.innerHTML += content;
        });
    })
    .catch(error => console.error('Error:', error));
}
