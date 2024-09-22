function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csfrtoken = getCookie('csrftoken');


const removeWishlists = document.querySelectorAll('.btn-danger');

    const wishlists = document.querySelectorAll('.wishlist');
    wishlists.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/wishlist/`, { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csfrtoken
                },
                body: JSON.stringify({
                    'product': element.dataset.id
                })
            }).then(response => response.json()).then(data => {
                    alert(
                        'Product added to wishlist'
                    )  
            })
        });
    });

removeWishlists.forEach((element) => {
  
    
    element.addEventListener('click', () => {
        return fetch(`${location.origin}/api/wishlist/`, { 
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csfrtoken
            },
            body: JSON.stringify({
                'product': element.dataset.id
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                alert('Product removed to wishlist')
            }
        })
    });
});
