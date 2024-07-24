document.addEventListener('DOMContentLoaded', () => {
  const idElement = document.querySelector('#red_header');
  const headerElement = document.querySelector('header');

  idElement.onclick = function () {
    headerElement.classList.add('red');
  };
});
