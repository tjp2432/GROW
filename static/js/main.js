async function addToCart(productId) {
    try {
        const res = await fetch('/api/cart/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: productId, quantity: 1 })
        });
        const data = await res.json();
        if (data.success) {
            updateCartBadge(data.count);
            showToast('Producto agregado al carrito', 'success');
        }
    } catch (e) {
        showToast('Error al agregar al carrito', 'error');
    }
}

async function updateCart(productId, quantity) {
    try {
        const res = await fetch('/api/cart/update', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: productId, quantity: quantity })
        });
        const data = await res.json();
        if (data.success) {
            location.reload();
        }
    } catch (e) {
        showToast('Error al actualizar carrito', 'error');
    }
}

async function removeFromCart(productId) {
    try {
        const res = await fetch('/api/cart/remove', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: productId })
        });
        const data = await res.json();
        if (data.success) {
            location.reload();
        }
    } catch (e) {
        showToast('Error al eliminar del carrito', 'error');
    }
}

async function updateCartBadge() {
    try {
        const res = await fetch('/api/cart');
        const data = await res.json();
        const badge = document.getElementById('cartBadge');
        if (badge) {
            badge.textContent = data.count;
            badge.style.display = data.count > 0 ? 'flex' : 'none';
        }
    } catch (e) {
        console.error('Error updating cart badge');
    }
}

function showToast(message, type) {
    const container = document.querySelector('.flash-container') || document.createElement('div');
    if (!container.classList.contains('flash-container')) {
        container.className = 'flash-container';
        document.body.prepend(container);
    }

    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    container.appendChild(alert);

    setTimeout(() => {
        alert.classList.remove('show');
        setTimeout(() => alert.remove(), 300);
    }, 3000);
}

document.addEventListener('DOMContentLoaded', function() {
    updateCartBadge();

    if (window.location.hash === '#checkout') {
        document.querySelector('.checkout-form')?.scrollIntoView({ behavior: 'smooth' });
    }

    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (el) {
        return new bootstrap.Tooltip(el);
    });
});
