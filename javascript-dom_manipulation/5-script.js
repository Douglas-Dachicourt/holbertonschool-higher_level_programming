document.addEventListener('DOMContentLoaded', () => {
  const updateElement = document.querySelector('#update_header');
  const headerElement = document.querySelector('header');

  updateElement.onclick = function () {
    headerElement.innerText = 'New Header!!!';
  };
});
