const productList = document.getElementById('product-list');
const productButton = document.getElementById('product-btn');

productButton.addEventListener('click', () => {
    fetch('/products/')
        .then(response => response.json())
        .then(data => {
            productList.innerHTML = '';
            data.forEach(product => {
                const listItem = document.createElement('li');
                listItem.textContent = `${product.name} - ${product.description}`;
                productList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error loading products:', error);
        });
});
