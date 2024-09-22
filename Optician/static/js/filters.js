const categories = document.querySelectorAll('.category-filter');



categories.forEach((element) => {
    element.addEventListener('click', () => {
        
        let url = `${location.origin}/api/products/`
        
        
        url += `?category=${element.getAttribute('data-id')}`
        console.log(url);
        
        fetch(url).then(response => response.json()).then(data => {
            console.log(data);
            
            
            document.getElementById('shop-single-product').innerHTML = ''

            for( let i in data) {
                console.log(data[i]);
                
                
                
                document.getElementById('shop-single-product').innerHTML += `
                     <div class="col-md-4 col-sm-6">               
                                            <div class="single-product">
                                                <div class="product-img">
                                                    <div class="label-new">
                                                        <span>new</span>
                                                    </div>
                                                    <a href="${data[i]['detail_url']}">
                                                        <!-- <img src="{{product.versions.cover_image.url}}" alt=""> -->
                                                        <img
                                                            src="${data[i]['versions'][0]['cover_image']}"
                                                            alt=""
                                                            class="primary-img"
                                                        />
                                                       
                                                    </a>
                                                </div>
                                                <div class="product-desc">
                                                    <div class="actions">
                                                        <ul>
                                                            <li>
                                                                <a
                                                                    href="#"
                                                                    data-bs-toggle="tooltip"
                                                                    data-placement="top"
                                                                    title="Add To Wish List"
                                                                    ><em
                                                                        >Add to
                                                                        Wish
                                                                        List</em
                                                                    ></a
                                                                >
                                                            </li>
                                                            <li>
                                                                <a
                                                                    href="#"
                                                                    class="link-compare"
                                                                    data-bs-toggle="tooltip"
                                                                    data-placement="top"
                                                                    title="Compare This Product"
                                                                    ><em
                                                                        >Compare
                                                                        this
                                                                        Product</em
                                                                    ></a
                                                                >
                                                            </li>
                                                        </ul>
                                                        <button
                                                            class="button"
                                                            data-bs-toggle="tooltip"
                                                            data-placement="top"
                                                            title="Add To Cart"
                                                        >
                                                            <span
                                                                >Add to
                                                                Cart</span
                                                            >
                                                        </button>
                                                    </div>
                                                    <div
                                                        class="product-content"
                                                    >
                                                        <h2
                                                            class="product-name"
                                                        >
                                                            <a href="#"
                                                                >${data[i]['name']}</a
                                                            >
                                                        </h2>
                                                        <div
                                                            class="product-ratings"
                                                        >
                                                            <a href="#"
                                                                ><i
                                                                    class="fa fa-star"
                                                                ></i
                                                            ></a>
                                                            <a href="#"
                                                                ><i
                                                                    class="fa fa-star"
                                                                ></i
                                                            ></a>
                                                            <a href="#"
                                                                ><i
                                                                    class="fa fa-star"
                                                                ></i
                                                            ></a>
                                                            <a href="#"
                                                                ><i
                                                                    class="fa fa-star"
                                                                ></i
                                                            ></a>
                                                            <a href="#"
                                                                ><i
                                                                    class="fa fa-star"
                                                                ></i
                                                            ></a>
                                                            <span
                                                                class="reviews"
                                                                ><a href="#"
                                                                    >0
                                                                    reviews</a
                                                                ></span
                                                            >
                                                        </div>
                                                        <div class="price-box">
                                                            <p
                                                                class="special-price">
                                                                   ${(data[i]['in_sale'] ? `<span class="special-price">${data[i]['old_price']}${'$'}</span><span class="old-price">${data[i]['price']}${'$'}</span>` : `<span class="special-price">${data[i]['price']}${'$'}</span>`)}
                                                            </p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                        
                `
            }
        })
    });
})

