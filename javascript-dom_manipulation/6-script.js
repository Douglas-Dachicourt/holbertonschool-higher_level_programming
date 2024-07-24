fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(async (response) => {
    const data = await response.json();
    const heroName = data.name;
    const characterToAdd = document.querySelector('#character');
    characterToAdd.textContent = heroName;
  });
