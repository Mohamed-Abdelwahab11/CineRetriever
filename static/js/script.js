async function performSearch() {
    const query = document.getElementById('queryInput').value;
    const grid = document.getElementById('resultsGrid');
    const stats = document.getElementById('stats');

    if (!query.trim()) return;

    grid.innerHTML = '<div class="loader">Accessing Cinematic Archive...</div>';

    try {
        const startTime = performance.now();
        const response = await fetch(`/search?query=${encodeURIComponent(query)}`);
        const data = await response.json();
        const endTime = performance.now();

        stats.innerText = `Found ${data.results.length} results in ${((endTime - startTime)/1000).toFixed(3)}s`;
        
        grid.innerHTML = '';
        data.results.forEach(movie => {
            grid.innerHTML += `
                <div class="movie-card">
                    <div class="score-tag">${movie.score}</div>
                    <img src="${movie.poster_url}" alt="${movie.title}" onerror="this.src='https://via.placeholder.com/500x750?text=No+Poster'">
                    <div class="card-info">
                        <h3>${movie.title}</h3>
                        <p>${movie.overview}</p>
                    </div>
                </div>
            `;
        });
    } catch (e) {
        grid.innerHTML = '<div class="error">System Error: Connectivity lost.</div>';
    }
}

function handleKeyPress(e) {
    if (e.key === 'Enter') performSearch();
}بي