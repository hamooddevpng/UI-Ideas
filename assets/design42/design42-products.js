/* Design 42: Featured Devices & Routers section. */
(()=>{
  if(document.getElementById('featured-products'))return;

  const PRODUCTS=[
    {
      name:'Telikom 4G MiFi Router',
      category:'Mobile Broadband',
      spec:'Connect up to 10 devices simultaneously on high-speed 4G LTE.',
      price:'K120',
      badge:'Best Value',
      image:'https://raw.githubusercontent.com/hamooddevpng/telikom-frontend/main/public/images/jpg/jpg_mobile_hotspot_device.jpg'
    },
    {
      name:'Samsung Galaxy A15',
      category:'Smartphone',
      spec:'6.5-inch Super AMOLED display, 50MP triple camera and 5000mAh battery.',
      price:'K499',
      badge:'Popular',
      image:'https://raw.githubusercontent.com/hamooddevpng/telikom-frontend/main/public/images/jpg/jpg_smartphone_front_back.jpg'
    },
    {
      name:'Telikom 4G LTE Home Gateway Router',
      category:'Mobile Broadband',
      spec:'Dual-band Wi-Fi 6 with fast 4G LTE connectivity for home and office.',
      price:'K399',
      badge:'Home & Office',
      image:'https://raw.githubusercontent.com/hamooddevpng/telikom-frontend/main/public/images/jpg/jpg_mobile_hotspot_device.jpg'
    },
    {
      name:'Samsung Galaxy A25',
      category:'Smartphone',
      spec:'6.5-inch 120Hz FHD+ Super AMOLED, 50MP OIS camera and 128GB storage.',
      price:'K799',
      badge:'Flagship',
      image:'https://raw.githubusercontent.com/hamooddevpng/telikom-frontend/main/public/images/jpg/jpg_smartphone_front_back.jpg'
    },
    {
      name:'ZTE Blade A52 4G',
      category:'Smartphone',
      spec:'6.52-inch HD+ display, 5000mAh battery and octa-core performance.',
      price:'K249',
      badge:'Entry Level',
      image:'https://raw.githubusercontent.com/hamooddevpng/telikom-frontend/main/public/images/jpg/jpg_smartphone_front_back.jpg'
    }
  ];

  const cards=PRODUCTS.map((item)=>`<article class="d42-product-card">
    <div class="d42-product-media">
      <img src="${item.image}" alt="${item.name}" loading="lazy" decoding="async">
      <span class="d42-product-badge">${item.badge}</span>
    </div>
    <div class="d42-product-copy">
      <span class="d42-product-category">${item.category}</span>
      <h3>${item.name}</h3>
      <p>${item.spec}</p>
      <div class="d42-product-meta"><strong>${item.price}</strong><a href="/devices" aria-label="View details for ${item.name}">View Details <span aria-hidden="true">→</span></a></div>
    </div>
  </article>`).join('');

  const section=document.createElement('section');
  section.id='featured-products';
  section.className='d42-products';
  section.setAttribute('aria-labelledby','featuredProductsTitle');
  section.innerHTML=`<div class="d42-products-shell">
    <div class="d42-products-head">
      <div><div class="eyebrow">Devices & routers</div><h2 id="featuredProductsTitle">Featured Devices & Routers</h2><p>Phones and connectivity hardware for life, work and home across Papua New Guinea.</p></div>
      <a class="d42-products-viewall" href="/devices">View All <span aria-hidden="true">→</span></a>
    </div>
    <div class="d42-products-grid">${cards}</div>
  </div>`;

  const main=document.querySelector('main');
  if(!main)return;
  const support=document.getElementById('support');
  if(support&&support.parentNode===main)main.insertBefore(section,support);
  else main.appendChild(section);
})();
