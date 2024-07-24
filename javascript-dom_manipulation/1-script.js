document.addEventListener('DOMContentLoaded', () => {
  const headerElement = document.querySelector('header');
  const idElement = document.querySelector('#red_header');

  idElement.onclick = function () {
    headerElement.style.color = '#FF0000';
  };
});
