fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(async (response) => {
    const data = await response.json();
    const films = data.films;
    for (let i = 0; i < films.length; i++) {
      fetch(data.films[i])
        .then(async (response) => {
          const filmName = await response.json();
          const filmsToAdd = document.querySelector('#list_movies');
          const newElement = document.createElement('li');
          newElement.textContent = filmName.title;
          filmsToAdd.append(newElement);
        });
    }
  });
