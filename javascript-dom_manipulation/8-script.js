fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(async (response) => {
    const data = await response.json();
    const hello = data.hello;

    const elemToInsert = document.querySelector('#hello');
    elemToInsert.textContent = hello;
  });
