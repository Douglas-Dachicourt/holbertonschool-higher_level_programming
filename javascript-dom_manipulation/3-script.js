document.addEventListener('DOMContentLoaded', () => {
  const idElement = document.querySelector('#toggle_header');
  const headerElement = document.querySelector('header');

  idElement.onclick = function () {
    if (headerElement.classList.contains('green') === true) {
      headerElement.classList.remove('green');
      headerElement.classList.add('red');
    } else if (headerElement.classList.contains('red') === true) {
      headerElement.classList.remove('red');
      headerElement.classList.add('green');
    }
  };
});
