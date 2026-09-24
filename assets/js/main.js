/**
 * SAMPARK ME DELHI - CORE JAVASCRIPT SYSTEM
 * Handles Cart Management, Hero Slider, Modals, Checkout, and Responsive Interactions
 */

(function () {
  'use strict';

  // --- Cart State Management ---
  const CART_KEY = 'sampark_cart';

  function getCart() {
    try {
      const data = localStorage.getItem(CART_KEY);
      if (data !== null) return JSON.parse(data);
      const initialCart = [{
        id: 'car-tag',
        name: 'Sampark Smart Vehicle Tag (Car / SUV)',
        price: 199,
        originalPrice: 499,
        image: 'assets/images/product-car.jpg',
        vehicleNumber: 'DL 01 AB 1234',
        quantity: 1
      }];
      localStorage.setItem(CART_KEY, JSON.stringify(initialCart));
      return initialCart;
    } catch (e) {
      console.error('Error reading cart', e);
      return [];
    }
  }

  function saveCart(cart) {
    try {
      localStorage.setItem(CART_KEY, JSON.stringify(cart));
      updateCartBadge();
    } catch (e) {
      console.error('Error saving cart', e);
    }
  }

  function updateCartBadge() {
    const cart = getCart();
    const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    const badges = document.querySelectorAll('.cart-counter');
    badges.forEach(badge => {
      badge.textContent = totalCount;
      badge.style.display = totalCount > 0 ? 'flex' : 'flex';
    });
  }

  function addToCart(product, quantity = 1, showToast = true) {
    const cart = getCart();
    const existingIndex = cart.findIndex(item => item.id === product.id);

    if (existingIndex > -1) {
      cart[existingIndex].quantity += quantity;
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        price: product.price,
        originalPrice: product.originalPrice || product.price,
        image: product.image,
        vehicleNumber: product.vehicleNumber || 'Pending Verification',
        quantity: quantity
      });
    }

    saveCart(cart);

    if (showToast) {
      showToastMessage(`✨ Added "${product.name}" to cart!`);
    }
  }

  function removeFromCart(productId) {
    let cart = getCart();
    cart = cart.filter(item => item.id !== productId);
    saveCart(cart);
    renderCartPage();
    showToastMessage('Item removed from cart.');
  }

  function updateQuantity(productId, delta) {
    let cart = getCart();
    const item = cart.find(item => item.id === productId);
    if (item) {
      item.quantity += delta;
      if (item.quantity <= 0) {
        cart = cart.filter(p => p.id !== productId);
      }
      saveCart(cart);
      renderCartPage();
    }
  }

  // --- Toast Notification Helper ---
  function showToastMessage(message) {
    let container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFCC00" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
      <span>${message}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }

  // --- Hero Slider ---
  function initHeroSlider() {
    const slides = document.querySelectorAll('.hero-slider-section .slide');
    const dotsContainer = document.querySelector('.slider-dots');
    const prevBtn = document.querySelector('.slider-prev');
    const nextBtn = document.querySelector('.slider-next');

    if (!slides.length) return;

    let currentIndex = 0;
    let timer = null;

    // Build dots
    if (dotsContainer) {
      dotsContainer.innerHTML = '';
      slides.forEach((_, idx) => {
        const dot = document.createElement('div');
        dot.className = `slider-dot ${idx === 0 ? 'active' : ''}`;
        dot.addEventListener('click', () => goToSlide(idx));
        dotsContainer.appendChild(dot);
      });
    }

    function showSlide(index) {
      slides.forEach((slide, idx) => {
        slide.classList.toggle('active', idx === index);
      });

      const dots = document.querySelectorAll('.slider-dot');
      dots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === index);
      });

      currentIndex = index;
    }

    function nextSlide() {
      const nextIndex = (currentIndex + 1) % slides.length;
      showSlide(nextIndex);
    }

    function prevSlide() {
      const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
      showSlide(prevIndex);
    }

    function goToSlide(index) {
      showSlide(index);
      resetTimer();
    }

    function startTimer() {
      timer = setInterval(nextSlide, 5500);
    }

    function resetTimer() {
      if (timer) clearInterval(timer);
      startTimer();
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        nextSlide();
        resetTimer();
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        prevSlide();
        resetTimer();
      });
    }

    const sliderSection = document.querySelector('.hero-slider-section');
    if (sliderSection) {
      sliderSection.addEventListener('mouseenter', () => clearInterval(timer));
      sliderSection.addEventListener('mouseleave', () => resetTimer());
    }

    startTimer();
  }

  // --- Robust Mobile Drawer Toggle ---
  function initMobileDrawer() {
    const toggles = document.querySelectorAll('.mobile-toggle');
    const drawers = document.querySelectorAll('.mobile-drawer');
    const closeBtns = document.querySelectorAll('.drawer-close');

    if (!toggles.length || !drawers.length) return;

    toggles.forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        drawers.forEach(d => d.classList.add('open'));
        document.body.style.overflow = 'hidden';
      });
    });

    function closeAllDrawers() {
      drawers.forEach(d => d.classList.remove('open'));
      document.body.style.overflow = '';
    }

    closeBtns.forEach(btn => btn.addEventListener('click', closeAllDrawers));
    drawers.forEach(drawer => {
      drawer.addEventListener('click', (e) => {
        if (e.target === drawer) closeAllDrawers();
      });
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeAllDrawers();
    });
  }

  // --- Real Shark Tank YouTube Video Modal Popup ---
  function initVideoModal() {
    const triggers = document.querySelectorAll('[data-video-modal]');
    triggers.forEach(trigger => {
      trigger.addEventListener('click', (e) => {
        e.preventDefault();
        const title = trigger.getAttribute('data-title') || 'Shark Tank India Season 5 Official Pitch';
        createVideoModal(title);
      });
    });
  }

  function createVideoModal(title) {
    const existingModal = document.querySelector('.sampark-modal');
    if (existingModal) existingModal.remove();

    const modal = document.createElement('div');
    modal.className = 'sampark-modal';
    modal.style.cssText = `
      position: fixed; inset: 0; z-index: 99999; background: rgba(10, 13, 20, 0.92);
      backdrop-filter: blur(12px); display: flex; align-items: center; justify-content: center;
      padding: 20px; animation: fadeIn 0.25s ease;
    `;

    modal.innerHTML = `
      <div style="background: #141822; border: 1px solid rgba(255,255,255,0.15); border-radius: 20px; width: 100%; max-width: 820px; overflow: hidden; box-shadow: 0 25px 60px rgba(0,0,0,0.85);">
        <div style="display:flex; align-items:center; justify-content:space-between; padding: 18px 24px; border-bottom: 1px solid rgba(255,255,255,0.1);">
          <h3 style="color:#FFF; font-size: 1.15rem; font-weight:700;">📺 ${title}</h3>
          <button class="modal-close-btn" style="color:#FFF; font-size: 1.8rem; line-height: 1; padding: 2px 8px; cursor:pointer; background:none; border:none;">&times;</button>
        </div>
        <div style="position: relative; padding-bottom: 56.25%; height: 0; background: #000;">
          <iframe style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;"
            src="https://www.youtube-nocookie.com/embed/gLERj3IT__I?autoplay=1"
            title="Shark Tank India Official Pitch - Sampark" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
          </iframe>
        </div>
        <div style="padding: 18px 24px; display:flex; align-items:center; justify-content:space-between; background:#0D111A; flex-wrap:wrap; gap:12px;">
          <span style="color:#94A3B8; font-size:0.88rem;">✨ As Broadcast on National Television • 100% Privacy-Preserving Smart Vehicle Calling</span>
          <a href="products.html" class="btn btn-primary btn-sm">Order Your Tag — ₹199</a>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    const closeBtn = modal.querySelector('.modal-close-btn');
    closeBtn.addEventListener('click', () => modal.remove());
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.remove();
    });
  }

  // --- Interactive FAQ Accordion ---
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
      const question = item.querySelector('.faq-question');
      if (!question) return;
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => i.classList.remove('active'));
        if (!isActive) item.classList.add('active');
      });
    });
  }

  // --- Interactive Virtual Tag Customizer ---
  function initTagCustomizer() {
    const plateInput = document.getElementById('custom-plate-input');
    const plateDisplay = document.getElementById('custom-plate-display');
    const typeSelect = document.getElementById('custom-type-select');
    const typeDisplay = document.getElementById('custom-type-display');
    const orderCustomBtn = document.getElementById('order-custom-tag-btn');

    if (!plateInput || !plateDisplay) return;

    plateInput.addEventListener('input', (e) => {
      let val = e.target.value.toUpperCase();
      plateDisplay.textContent = val || 'DL 01 AB 1234';
    });

    if (typeSelect && typeDisplay) {
      typeSelect.addEventListener('change', (e) => {
        typeDisplay.textContent = e.target.value.toUpperCase();
      });
    }

    if (orderCustomBtn) {
      orderCustomBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const customNumber = plateInput.value.trim().toUpperCase() || 'DL 01 AB 1234';
        const tagType = typeSelect ? typeSelect.value : 'Smart Car Tag';
        addToCart({
          id: 'custom-printed-tag',
          name: `Custom Sampark Tag (${tagType})`,
          price: 199,
          originalPrice: 499,
          image: 'assets/images/real-tag-sticker.png',
          vehicleNumber: customNumber
        }, 1, true);
        setTimeout(() => {
          window.location.href = 'checkout.html';
        }, 500);
      });
    }
  }

  // --- Render Cart Page ---
  function renderCartPage() {
    const itemsContainer = document.getElementById('cart-items-list');
    const subtotalEl = document.getElementById('cart-subtotal');
    const totalEl = document.getElementById('cart-total');
    const discountEl = document.getElementById('cart-discount');
    const emptyState = document.getElementById('cart-empty-state');
    const cartWrapper = document.getElementById('cart-active-wrapper');

    if (!itemsContainer) return;

    const cart = getCart();

    if (cart.length === 0) {
      if (cartWrapper) cartWrapper.style.display = 'none';
      if (emptyState) emptyState.style.display = 'block';
      return;
    }

    if (cartWrapper) cartWrapper.style.display = 'grid';
    if (emptyState) emptyState.style.display = 'none';

    let subtotal = 0;
    itemsContainer.innerHTML = '';

    cart.forEach(item => {
      const itemSubtotal = item.price * item.quantity;
      subtotal += itemSubtotal;

      const row = document.createElement('div');
      row.className = 'cart-item-row';
      row.innerHTML = `
        <div class="cart-item-img">
          <img src="${item.image}" alt="${item.name}">
        </div>
        <div>
          <h4 style="font-size: 1.05rem; font-weight:700; color: #0F172A; margin-bottom: 4px;">${item.name}</h4>
          <p style="font-size: 0.8rem; color: #64748B; margin-bottom: 6px;">Vehicle: <strong style="color:#D97706;">${item.vehicleNumber}</strong></p>
          <span style="font-size: 0.95rem; font-weight:800; color: #0F172A;">₹${item.price}</span>
          ${item.originalPrice > item.price ? `<span style="font-size: 0.8rem; color:#94A3B8; text-decoration:line-through; margin-left:6px;">₹${item.originalPrice}</span>` : ''}
        </div>
        <div class="qty-stepper">
          <button class="qty-btn btn-minus" data-id="${item.id}">-</button>
          <span class="qty-val">${item.quantity}</span>
          <button class="qty-btn btn-plus" data-id="${item.id}">+</button>
        </div>
        <div style="text-align: right;">
          <div style="font-weight: 800; font-size: 1.1rem; color: #0F172A; margin-bottom: 6px;">₹${itemSubtotal}</div>
          <button class="btn-remove-item" data-id="${item.id}" style="color: #EF4444; font-size: 0.82rem; font-weight: 700; display:flex; align-items:center; gap:4px; margin-left:auto;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
            Remove
          </button>
        </div>
      `;
      itemsContainer.appendChild(row);
    });

    const isCouponApplied = sessionStorage.getItem('sampark_coupon_applied') === 'true';
    const discount = isCouponApplied ? 50 : 0;
    const finalTotal = Math.max(0, subtotal - discount);

    if (subtotalEl) subtotalEl.textContent = `₹${subtotal}`;
    if (discountEl) discountEl.textContent = discount > 0 ? `-₹${discount}` : `₹0`;
    if (totalEl) totalEl.textContent = `₹${finalTotal}`;

    // Attach listeners
    itemsContainer.querySelectorAll('.btn-plus').forEach(btn => {
      btn.addEventListener('click', () => updateQuantity(btn.dataset.id, 1));
    });
    itemsContainer.querySelectorAll('.btn-minus').forEach(btn => {
      btn.addEventListener('click', () => updateQuantity(btn.dataset.id, -1));
    });
    itemsContainer.querySelectorAll('.btn-remove-item').forEach(btn => {
      btn.addEventListener('click', () => removeFromCart(btn.dataset.id));
    });
  }

  // --- Coupon Code Handler ---
  function initCoupon() {
    const couponBtn = document.getElementById('apply-coupon-btn');
    const couponInput = document.getElementById('coupon-input');
    const couponMsg = document.getElementById('coupon-msg');

    if (!couponBtn || !couponInput) return;

    couponBtn.addEventListener('click', () => {
      const code = couponInput.value.trim().toUpperCase();
      if (code === 'SAMPARK50' || code === 'DELHI50') {
        sessionStorage.setItem('sampark_coupon_applied', 'true');
        if (couponMsg) {
          couponMsg.style.display = 'block';
          couponMsg.style.color = '#10B981';
          couponMsg.textContent = '🎉 Coupon applied! ₹50 instant discount granted.';
        }
        renderCartPage();
        showToastMessage('Coupon applied: ₹50 OFF!');
      } else {
        if (couponMsg) {
          couponMsg.style.display = 'block';
          couponMsg.style.color = '#EF4444';
          couponMsg.textContent = 'Invalid promo code. Try "SAMPARK50".';
        }
      }
    });
  }

  // --- Pincode Checker Simulation ---
  function initPincodeChecker() {
    const checkBtn = document.getElementById('check-pincode-btn');
    const input = document.getElementById('pincode-input');
    const resultEl = document.getElementById('pincode-result');

    if (!checkBtn || !input || !resultEl) return;

    checkBtn.addEventListener('click', () => {
      const pin = input.value.trim();
      if (!/^\d{6}$/.test(pin)) {
        resultEl.innerHTML = `<span style="color:#EF4444; font-weight:700;">Please enter a valid 6-digit Indian Pincode.</span>`;
        return;
      }

      resultEl.innerHTML = `
        <div style="background:#ECFDF5; border:1px solid #10B981; border-radius:10px; padding:10px 14px; margin-top:10px; color:#065F46; font-size:0.85rem;">
          ⚡ <strong>Delivery Available to ${pin}</strong>: Express Dispatch within 24 Hours. Estimated Delivery: <strong>Tomorrow by 5 PM</strong>.
        </div>
      `;
    });
  }

  // --- Global Buy Now & Add To Cart Button Listeners ---
  function initAddButtons() {
    document.querySelectorAll('[data-add-cart]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const id = btn.getAttribute('data-id');
        const name = btn.getAttribute('data-name');
        const price = parseFloat(btn.getAttribute('data-price'));
        const originalPrice = parseFloat(btn.getAttribute('data-original') || price);
        const image = btn.getAttribute('data-image');
        const vehicleInput = document.getElementById('vehicle-plate-input');
        const vehicleNumber = vehicleInput ? vehicleInput.value.trim().toUpperCase() : 'STANDARD TAG';

        addToCart({ id, name, price, originalPrice, image, vehicleNumber });
      });
    });

    document.querySelectorAll('[data-buy-now]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const id = btn.getAttribute('data-id');
        const name = btn.getAttribute('data-name');
        const price = parseFloat(btn.getAttribute('data-price'));
        const originalPrice = parseFloat(btn.getAttribute('data-original') || price);
        const image = btn.getAttribute('data-image');
        const vehicleInput = document.getElementById('vehicle-plate-input');
        const vehicleNumber = vehicleInput ? vehicleInput.value.trim().toUpperCase() : 'STANDARD TAG';

        addToCart({ id, name, price, originalPrice, image, vehicleNumber }, 1, false);
        window.location.href = 'checkout.html';
      });
    });
  }

  // --- Confetti Wishes Animation Helper ---
  function launchConfetti() {
    const count = 120;
    const container = document.createElement('div');
    container.style.cssText = `position:fixed; inset:0; pointer-events:none; z-index:999999; overflow:hidden;`;
    document.body.appendChild(container);

    const colors = ['#FFCC00', '#FF3E3E', '#10B981', '#3B82F6', '#8B5CF6', '#FFFFFF'];

    for (let i = 0; i < count; i++) {
      const piece = document.createElement('div');
      const size = Math.floor(Math.random() * 8) + 6;
      piece.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size * (Math.random() > 0.5 ? 1 : 1.8)}px;
        background: ${colors[Math.floor(Math.random() * colors.length)]};
        top: -20px;
        left: ${Math.random() * 100}vw;
        opacity: ${Math.random() + 0.4};
        border-radius: ${Math.random() > 0.4 ? '50%' : '2px'};
        transform: rotate(${Math.random() * 360}deg);
        transition: transform 3.5s cubic-bezier(0.25, 0.46, 0.45, 0.94), top 3.5s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 3.5s ease-out;
      `;
      container.appendChild(piece);

      setTimeout(() => {
        piece.style.top = '105vh';
        piece.style.transform = `rotate(${Math.random() * 1080}deg) translateX(${Math.random() * 200 - 100}px)`;
        piece.style.opacity = '0';
      }, 50);
    }

    setTimeout(() => container.remove(), 4000);
  }

  // Expose global methods
  window.SamparkApp = {
    addToCart,
    removeFromCart,
    updateQuantity,
    showToastMessage,
    launchConfetti
  };

  // Run on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
    initHeroSlider();
    initMobileDrawer();
    initVideoModal();
    initAddButtons();
    initCoupon();
    initPincodeChecker();
    initFaqAccordion();
    initTagCustomizer();
    renderCartPage();

    // Default sample cart item if cart is empty on first visit so user can explore seamlessly
    if (getCart().length === 0 && window.location.pathname.endsWith('cart.html')) {
      addToCart({
        id: 'car-tag',
        name: 'Sampark Smart Car Tag',
        price: 199,
        originalPrice: 499,
        image: 'assets/images/product-car.jpg',
        vehicleNumber: 'DL 01 AB 1234'
      }, 1, false);
      renderCartPage();
    }
  });

})();
