// ================= CONFIG =================
var API_URL = "https://chandigarh-sweets-ordering-system-1.onrender.com";

var allProducts = [];
var cart = [];
var sessionId = "user_" + Math.random().toString(36).substr(2, 9);

// ================= INIT =================
window.onload = function () {

    console.log("SCRIPT LOADED");

    fetchProducts();

    let search = document.getElementById("search-food");

    if (search) {

        search.addEventListener("input", function () {

            let keyword = this.value.toLowerCase();

            let filtered = allProducts.filter(function (product) {
                return product.name.toLowerCase().includes(keyword);
            });

            showProducts(filtered);

            let hero = document.querySelector(".hero");

            if (keyword.length > 0) {

                hero.style.display = "none";

                window.scrollTo({
                    top: document.getElementById("menu").offsetTop - 80,
                    behavior: "smooth"
                });

            } else {

                hero.style.display = "flex";

            }

        });

    }

};

// ================= FETCH PRODUCTS =================
function fetchProducts() {

    fetch(API_URL + "/products")
        .then(function (res) { return res.json(); })
        .then(function (data) {

            allProducts = data;

            console.log("Products loaded:", data.length);

            showCategories();
            showProducts(allProducts);

        })
        .catch(function (err) {
            console.error("Error:", err);
        });

}

// ================= SHOW CATEGORIES =================
function showCategories() {

    var categories = [];

    allProducts.forEach(function (p) {

        if (!categories.includes(p.category)) {
            categories.push(p.category);
        }

    });

    var html = '<button class="tab-btn active" data-category="all">All</button>';

    categories.forEach(function (cat) {

        html += '<button class="tab-btn" data-category="' + cat + '">' + cat + '</button>';

    });

    document.getElementById("category-tabs").innerHTML = html;

    document.querySelectorAll(".tab-btn").forEach(function (btn) {

        btn.onclick = function () {

            document.querySelectorAll(".tab-btn").forEach(function (b) {
                b.classList.remove("active");
            });

            this.classList.add("active");

            var cat = this.getAttribute("data-category");

            if (cat === "all") {

                showProducts(allProducts);

            } else {

                var filtered = allProducts.filter(function (p) {
                    return p.category === cat;
                });

                showProducts(filtered);

            }

        };

    });

}

// ================= SHOW PRODUCTS =================
function showProducts(products) {

    var container = document.getElementById("products-container");

    container.innerHTML = "";

    products.forEach(function (product) {

        var card = document.createElement("div");
        card.className = "product-card";

        var rating = "⭐⭐⭐⭐";

        var badge = "";

        if (product.name.toLowerCase().includes("paneer") ||
            product.name.toLowerCase().includes("biryani")) {

            badge = '<span class="badge">🔥 Bestseller</span>';

        }

        var imageHtml = "";

        if (product.image) {

            imageHtml =
                '<img src="' + product.image + '" style="width:100%;height:180px;object-fit:cover">';

        } else {

            imageHtml = '<i class="fas fa-utensils"></i>';

        }

        card.innerHTML =

            badge +

            '<div class="product-image">' + imageHtml + '</div>' +

            '<div class="product-info">' +

            '<h4>' + product.name + '</h4>' +

            '<div class="rating">' + rating + '</div>' +

            '<p class="price">₹' + product.price + '</p>' +

            '<button class="btn-add">Add to Cart</button>' +

            '</div>';

        card.querySelector(".btn-add").addEventListener("click", function () {

            let img = card.querySelector("img");

            if (img) {
                flyToCart(img);
            }

            addToCart(product);

        });

        container.appendChild(card);

    });

}

// ================= FLY TO CART =================
function flyToCart(img) {

    let cartIcon = document.querySelector(".cart-icon");

    let clone = img.cloneNode(true);

    clone.style.position = "fixed";
    clone.style.zIndex = "1000";
    clone.style.width = "80px";
    clone.style.transition = "all 0.8s ease";

    let rect = img.getBoundingClientRect();

    clone.style.left = rect.left + "px";
    clone.style.top = rect.top + "px";

    document.body.appendChild(clone);

    setTimeout(function () {

        let cartRect = cartIcon.getBoundingClientRect();

        clone.style.left = cartRect.left + "px";
        clone.style.top = cartRect.top + "px";

        clone.style.opacity = "0.5";
        clone.style.transform = "scale(0.3)";

    }, 50);

    setTimeout(function () {

        clone.remove();

    }, 800);

}

// ================= ADD TO CART =================
function addToCart(product) {

    var existing = cart.find(function (item) {
        return item.id === product.id;
    });

    if (existing) {

        existing.quantity++;

    } else {

        cart.push({
            id: product.id,
            name: product.name,
            price: product.price,
            quantity: 1
        });

    }

    refreshCart();

}

// ================= REFRESH CART =================
function refreshCart() {

    var count = 0;

    cart.forEach(function (item) {
        count += item.quantity;
    });

    document.getElementById("cart-count").innerText = count;

    var cartItems = document.getElementById("cart-items");
    var cartTotal = document.getElementById("cart-total");

    if (cart.length === 0) {

        cartItems.innerHTML = "<p>Cart is empty</p>";
        cartTotal.innerText = "₹0";

        return;

    }

    var total = 0;
    var html = "";

    cart.forEach(function (item) {

        var itemTotal = item.price * item.quantity;

        total += itemTotal;

        html +=

            '<div class="cart-item">' +

            '<div><strong>' + item.name + '</strong><br>₹' +
            item.price + ' x ' + item.quantity + '</div>' +

            '<div>' +

            '<button onclick="changeQty(' + item.id + ',-1)">-</button>' +

            ' ' + item.quantity + ' ' +

            '<button onclick="changeQty(' + item.id + ',1)">+</button>' +

            '</div></div>';

    });

    cartItems.innerHTML = html;

    cartTotal.innerText = "₹" + total;

}

// ================= CHANGE QTY =================
function changeQty(productId, change) {

    cart.forEach(function (item) {

        if (item.id === productId) {

            item.quantity += change;

            if (item.quantity <= 0) {

                cart.splice(cart.indexOf(item), 1);

            }

        }

    });

    refreshCart();

}

// ================= TOGGLE CART =================
function toggleCart() {

    document.getElementById("cart-sidebar").classList.toggle("active");

}

// ================= SYNC CART =================
async function syncCart() {

    for (let item of cart) {

        await fetch(API_URL + "/cart/add/" + item.id +
            "?quantity=" + item.quantity +
            "&session_id=" + sessionId,
            {
                method: "POST"
            });

    }

}

// ================= PLACE ORDER =================
async function placeOrder(event) {

    event.preventDefault();

    await syncCart();

    var orderData = {

        customer_name: document.getElementById("customer-name").value,
        phone: document.getElementById("customer-phone").value,
        address: document.getElementById("address").value || "Pickup",
        order_type: document.getElementById("order-type").value,
        payment_method: document.getElementById("payment-method").value,
        session_id: sessionId

    };

    fetch(API_URL + "/order/place", {

        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(orderData)

    })
        .then(function (res) { return res.json(); })
        .then(function (result) {

            document.getElementById("order-number").innerText =
                "Order #" + result.order_number;

            document.getElementById("success-modal").style.display = "flex";

            cart = [];

            refreshCart();

        });

}

// ================= CLOSE SUCCESS =================
function closeSuccess() {

    document.getElementById("success-modal").style.display = "none";

}
// ================= SHOW CHECKOUT =================
function showCheckout() {

    if (cart.length === 0) {
        alert("Cart is empty!");
        return;
    }

    // cart summary update karo
    var checkoutItems = document.getElementById("checkout-items");
    var checkoutTotal = document.getElementById("checkout-total");

    var html = "";
    var total = 0;

    cart.forEach(function(item){

        var itemTotal = item.price * item.quantity;
        total += itemTotal;

        html += `<p>${item.name} x ${item.quantity} = ₹${itemTotal}</p>`;

    });

    checkoutItems.innerHTML = html;
    checkoutTotal.innerText = "₹" + total;

    toggleCart();
    document.getElementById("checkout-modal").style.display = "flex";

}

// ================= CLOSE CHECKOUT =================
function closeCheckout() {

    document.getElementById("checkout-modal").style.display = "none";

}
document.getElementById("payment-method").addEventListener("change",function(){

let method=this.value

if(method==="upi"){

document.getElementById("upi-box").style.display="block"

}else{

document.getElementById("upi-box").style.display="none"

}


})
