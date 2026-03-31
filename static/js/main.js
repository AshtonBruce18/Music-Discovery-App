function parseArtists(jsonString){
    const obj = JSON.parse(jsonString);
    const randIndex = Math.floor(Math.random() * obj.length);

    const currArtist = obj[randIndex];
    const name = currArtist.name;
    const imgURL = currArtist.images[0].url;
    const link = currArtist.external_urls.spotify;
    const followers = currArtist.followers.total;

    return `<h1> ${name} </h1>
            <img src="${imgURL}" alt="${name}"></img>
            <p><span>${followers} followers</span>
            <a class="button" href="${link}">Open Spotify Page</a></p>`;
}