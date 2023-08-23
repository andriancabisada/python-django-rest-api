const categoryList = document.getElementById('category-list');
const categoryButton = document.getElementById('category-btn');

categoryButton.addEventListener('click', () => {
    fetch('/categories/')
        .then(response => response.json())
        .then(data => {
            categoryList.innerHTML = '';
            data.forEach(category => {
                const listItem = document.createElement('li');
                listItem.textContent = category.name;
                categoryList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error loading categories:', error);
        });
});
