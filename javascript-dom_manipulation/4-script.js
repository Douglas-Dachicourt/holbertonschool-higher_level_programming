document.addEventListener('DOMContentLoaded', () => {
  const addItemElement = document.querySelector('#add_item');
  const listElement = document.querySelector('.my_list');

  addItemElement.onclick = function () {
    const newElement = document.createElement('li');
    newElement.textContent = 'Item';

    listElement.append(newElement);
  };
});
