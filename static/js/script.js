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
            const escapedTitle = movie.title.replace(/'/g, "&apos;").replace(/"/g, "&quot;");
            grid.innerHTML += `
                <div class="movie-card">
                    <div class="score-tag">${movie.score}</div>
                    <div class="card-image-wrapper">
                        <img src="${movie.poster_url}" alt="${escapedTitle}" onerror="this.parentElement.innerHTML='<div class=\\'dynamic-poster\\'><h3>${escapedTitle}</h3></div>'">
                    </div>
                    <div class="card-info">
                        <h3>${escapedTitle}</h3>
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
}