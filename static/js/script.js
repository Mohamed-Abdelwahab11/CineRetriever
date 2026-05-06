const TMDB_API_KEY = '9e47e360a33f7b48913b77c2b94a7088';

async function fetchPoster(title, year) {
    try {
        const url = `https://api.themoviedb.org/3/search/movie?api_key=${TMDB_API_KEY}&query=${encodeURIComponent(title)}&year=${year}`;
        const res = await fetch(url);
        const data = await res.json();
        if (data.results && data.results.length > 0 && data.results[0].poster_path) {
            return `https://image.tmdb.org/t/p/w500${data.results[0].poster_path}`;
        }
    } catch (e) {
        console.error('TMDB fetch error:', e);
    }
    return null;
}

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
        
        // Render cards
        for (const movie of data.results) {
            const escapedTitle = movie.title.replace(/'/g, "&apos;").replace(/"/g, "&quot;");
            const imdbUrl = `https://www.imdb.com/find?q=${encodeURIComponent(movie.title + ' ' + movie.release_year)}`;
            const wikiUrl = movie.wiki_page || '#';
            
            // Initial render with dynamic CSS poster
            const cardId = 'movie-' + Math.random().toString(36).substr(2, 9);
            grid.innerHTML += `
                <div class="movie-card" id="${cardId}">
                    <div class="score-tag">${movie.score}</div>
                    <div class="card-image-wrapper" id="img-wrapper-${cardId}">
                        <div class="dynamic-poster"><h3>${escapedTitle}</h3></div>
                    </div>
                    <div class="card-info">
                        <h3>${escapedTitle} <span class="year">(${movie.release_year})</span></h3>
                        <p>${movie.overview}</p>
                        <div class="card-actions">
                            <a href="${imdbUrl}" target="_blank" class="btn imdb-btn">IMDb</a>
                            <a href="${wikiUrl}" target="_blank" class="btn wiki-btn">Wikipedia</a>
                        </div>
                    </div>
                </div>
            `;
            
            // Asynchronously fetch and swap poster
            fetchPoster(movie.title, movie.release_year).then(posterUrl => {
                if (posterUrl) {
                    const wrapper = document.getElementById(`img-wrapper-${cardId}`);
                    if (wrapper) {
                        wrapper.innerHTML = `<img src="${posterUrl}" alt="${escapedTitle}" onerror="this.parentElement.innerHTML='<div class=\\'dynamic-poster\\'><h3>${escapedTitle}</h3></div>'">`;
                    }
                }
            });
        }
    } catch (e) {
        grid.innerHTML = '<div class="error">System Error: Connectivity lost.</div>';
    }
}

function handleKeyPress(e) {
    if (e.key === 'Enter') performSearch();
}