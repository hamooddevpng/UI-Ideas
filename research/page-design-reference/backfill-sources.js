const S=(slug,name,url,category='telecom')=>({slug,name,url,category});

// QA backfills are deliberately broader than the minimum. The capture pass may
// reject bot walls, wrong redirects, error pages or incomplete renders, so each
// page study gets enough additional candidates to retain 15 usable visual refs.
const pageBackfills={
  'services-hub':[
    S('bt-consumer','BT','https://www.bt.com/'),
    S('vodafone-uk','Vodafone UK','https://www.vodafone.co.uk/'),
    S('ee-consumer','EE','https://ee.co.uk/'),
    S('three-uk','Three UK','https://www.three.co.uk/'),
    S('virgin-media','Virgin Media','https://www.virginmedia.com/'),
    S('sky-uk','Sky UK','https://www.sky.com/')
  ],
  'personal-mobile':[
    S('vodafone-uk-payg','Vodafone UK PAYG','https://www.vodafone.co.uk/sim-only/pay-as-you-go-sim'),
    S('three-uk-payg','Three UK PAYG Data Packs','https://www.three.co.uk/pay-as-you-go/payg-data-packs'),
    S('ee-payg','EE PAYG Plans','https://ee.co.uk/help/mobile/manage-use/pay-as-you-go/pay-as-you-go-mobile-plans-may2026'),
    S('giffgaff-payg','giffgaff PAYG','https://www.giffgaff.com/sim-only-deals/pay-as-you-go'),
    S('smarty-plans','SMARTY Plans','https://smarty.co.uk/all-plans'),
    S('lebara-mobile','Lebara UK','https://www.lebara.co.uk/en/home.html')
  ],
  'affordable-home-data':[
    S('vodafone-uk-broadband','Vodafone UK Broadband','https://www.vodafone.co.uk/broadband'),
    S('virgin-media-broadband','Virgin Media Broadband','https://www.virginmedia.com/broadband'),
    S('sky-broadband','Sky Broadband','https://www.sky.com/broadband'),
    S('bt-home','BT Broadband / Home','https://www.bt.com/'),
    S('three-data-sim','Three Data Only SIM','https://www.three.co.uk/sim/data-sim-payg'),
    S('giffgaff-broadband','giffgaff','https://www.giffgaff.com/')
  ],
  'special-home-passes':[
    S('three-data-packs','Three PAYG Data Packs','https://www.three.co.uk/pay-as-you-go/payg-data-packs'),
    S('ee-data-addons','EE PAYG Data Add-ons','https://ee.co.uk/help/mobile/manage-use/pay-as-you-go/payg-data-addons'),
    S('vodafone-payg-bundles','Vodafone UK PAYG Bundles','https://www.vodafone.co.uk/sim-only/pay-as-you-go-sim/renew-bundle'),
    S('giffgaff-payg','giffgaff PAYG','https://www.giffgaff.com/sim-only-deals/pay-as-you-go'),
    S('smarty-payg','SMARTY PAYG','https://smarty.co.uk/pay-as-you-go'),
    S('lebara-mobile','Lebara UK','https://www.lebara.co.uk/en/home.html')
  ],
  'u-tokmoa':[
    S('vodafone-broadband-landline','Vodafone Broadband & Landline','https://www.vodafone.co.uk/broadband/broadband-and-landline'),
    S('bt-home','BT Home','https://www.bt.com/'),
    S('virgin-media-broadband','Virgin Media Broadband','https://www.virginmedia.com/broadband'),
    S('sky-broadband','Sky Broadband','https://www.sky.com/broadband'),
    S('three-data-sim','Three Data Only SIM','https://www.three.co.uk/sim/data-sim-payg'),
    S('giffgaff-plans','giffgaff','https://www.giffgaff.com/sim-only')
  ],
  'home-entertainment':[
    S('bt-tv-home','BT Broadband & TV','https://www.bt.com/'),
    S('virgin-media-broadband-tv','Virgin Media Broadband & TV','https://www.virginmedia.com/broadband'),
    S('virgin-tv-subscriptions','Virgin TV Subscriptions','https://www.virginmedia.com/the-edit/tv/virgin-media-tv-subscriptions'),
    S('sky-tv','Sky TV','https://www.sky.com/tv'),
    S('vodafone-uk-broadband','Vodafone UK Broadband','https://www.vodafone.co.uk/broadband'),
    S('sky-broadband','Sky Broadband','https://www.sky.com/broadband')
  ],
  'devices':[
    S('three-phones','Three Phones','https://www.three.co.uk/shop/phones'),
    S('vodafone-uk-phones','Vodafone UK Phones','https://www.vodafone.co.uk/mobile/phones'),
    S('ee-phones','EE Phones','https://ee.co.uk/mobile/phones'),
    S('o2-phones','O2 Phones','https://www.o2.co.uk/shop/phones'),
    S('giffgaff-phones','giffgaff Phones','https://www.giffgaff.com/mobile-phones'),
    S('apple-iphone','Apple iPhone','https://www.apple.com/uk/iphone/','adjacent-retail'),
    S('samsung-smartphones','Samsung Smartphones','https://www.samsung.com/uk/smartphones/','adjacent-retail'),
    S('three-phone-brands','Three Phone Brands','https://www.three.co.uk/mobile-phones/brands')
  ],
  'business-fixed':[
    S('vodafone-enterprise-broadband','Vodafone Enterprise Broadband','https://www.vodafone.co.uk/business/business-broadband/enterprise-broadband'),
    S('bt-business-broadband','BT Business Broadband','https://business.bt.com/business-broadband/'),
    S('comcast-business','Comcast Business','https://business.comcast.com/'),
    S('orange-business','Orange Business','https://www.orange-business.com/en'),
    S('vodafone-business','Vodafone Business','https://www.vodafone.co.uk/business'),
    S('ee-business','EE Business','https://business.ee.co.uk/')
  ],
  'business-mobile':[
    S('ee-business-mobile','EE Business Mobile','https://business.ee.co.uk/business-solutions/plans-devices/'),
    S('ee-small-business-mobile','EE Small Business Mobile','https://business.ee.co.uk/business-solutions/plans-devices/small-business/'),
    S('vodafone-business','Vodafone Business','https://www.vodafone.co.uk/business'),
    S('three-business','Three Business','https://www.three.co.uk/business'),
    S('bt-business','BT Business','https://business.bt.com/'),
    S('orange-business','Orange Business','https://www.orange-business.com/en')
  ],
  'news-media':[
    S('vodafone-group-news','Vodafone Group News','https://www.vodafone.com/news'),
    S('bt-newsroom','BT Group Newsroom','https://newsroom.bt.com/'),
    S('deutsche-telekom-media','Deutsche Telekom Media','https://www.telekom.com/en/newsroom/latest-updates/media-information'),
    S('tmobile-newsroom','T-Mobile Newsroom','https://www.t-mobile.com/news'),
    S('telefonica-news','Telefonica News','https://www.telefonica.com/en/communication-room/'),
    S('gsma-newsroom','GSMA Newsroom','https://www.gsma.com/newsroom/','industry'),
    S('nac-png','National Airports Corporation PNG','https://nac.com.pg/','png-public-enterprise'),
    S('png-ports','PNG Ports','https://www.pngports.com.pg/','png-public-enterprise')
  ],
  'about-us':[
    S('bt-about','BT About','https://www.bt.com/about/bt'),
    S('telstra-about','Telstra About','https://www.telstra.com.au/aboutus/our-company'),
    S('vodafone-group','Vodafone Group','https://www.vodafone.com/about-vodafone'),
    S('ela-motors-profile','Ela Motors Corporate Profile','https://www.toyota-png.com/corporate-profile/','png-business'),
    S('lae-biscuit','Lae Biscuit','https://www.laebiscuit.com/','png-business'),
    S('goodman-fielder-png','Goodman Fielder PNG','https://goodmanfielder.com/countries/papua-new-guinea/','png-business')
  ],
  'store-locator':[
    S('vodafone-uk-stores','Vodafone UK Store Finder','https://stores.vodafone.co.uk/search'),
    S('ee-store-finder','EE Store Finder','https://ee.co.uk/store-finder'),
    S('three-store-locator','Three Store Locator','https://www.three.co.uk/store-locator'),
    S('o2-stores','O2 Store Locator','https://stores.o2.co.uk/'),
    S('ela-motors-locations','Ela Motors Locations','https://www.toyota-png.com/contact-us/','png-business'),
    S('coral-sea-hotels','Coral Sea Hotels Locations','https://coralseahotels.com.pg/','png-business'),
    S('moniplus-branches','Moni Plus Branches','https://www.moniplus.com/branches/','png-business')
  ],
  'careers':[
    S('bt-careers','BT Careers','https://jobs.bt.com/BT/'),
    S('vodafone-careers','Vodafone Careers','https://careers.vodafone.com/'),
    S('vodafone-applying','Vodafone Hiring Process','https://careers.vodafone.com/applying-to-vodafone/'),
    S('ela-motors','Ela Motors PNG','https://www.toyota-png.com/','png-business'),
    S('lae-biscuit','Lae Biscuit','https://www.laebiscuit.com/','png-business'),
    S('nac-png','National Airports Corporation','https://nac.com.pg/','png-public-enterprise')
  ],
  'faqs':[
    S('bt-help','BT Help','https://www.bt.com/help'),
    S('three-support','Three Support','https://www.three.co.uk/support'),
    S('o2-help','O2 Help','https://www.o2.co.uk/help'),
    S('ee-help','EE Help','https://ee.co.uk/help'),
    S('three-contact','Three Contact & Support','https://www.three.co.uk/support/contact-us'),
    S('vodafone-uk','Vodafone UK','https://www.vodafone.co.uk/')
  ],
  'contact':[
    S('three-contact','Three Contact','https://www.three.co.uk/support/contact-us'),
    S('ee-contact','EE Contact','https://ee.co.uk/help/contact-ee'),
    S('coral-sea-contact','Coral Sea Hotels Contact','https://coralseahotels.com.pg/contact-us/','png-business'),
    S('ela-motors-contact','Ela Motors Contact','https://www.toyota-png.com/contact-us/','png-business'),
    S('pacific-industries-contact','Pacific Industries Contact','https://www.pacificindustries.com.pg/contact','png-business'),
    S('moniplus-branches','Moni Plus Branches','https://www.moniplus.com/branches/','png-business')
  ]
};

const contextBackfills={
  'context-png-businesses':[
    S('coral-sea-hotels','Coral Sea Hotels','https://coralseahotels.com.pg/','png-business'),
    S('pacific-industries','Pacific Industries','https://www.pacificindustries.com.pg/','png-business'),
    S('moniplus','Moni Plus','https://www.moniplus.com/','png-business'),
    S('lae-biscuit','Lae Biscuit','https://www.laebiscuit.com/','png-business'),
    S('ela-motors','Ela Motors PNG','https://www.toyota-png.com/','png-business'),
    S('goodman-fielder-png','Goodman Fielder PNG','https://goodmanfielder.com/countries/papua-new-guinea/','png-business')
  ],
  'context-png-public-sector':[
    S('png-customs','PNG Customs','https://customs.gov.pg/','png-government'),
    S('national-airports','National Airports Corporation','https://nac.com.pg/','png-public-enterprise'),
    S('png-ports','PNG Ports','https://www.pngports.com.pg/','png-public-enterprise'),
    S('works-png','Department of Works & Highways','https://www.works.gov.pg/','png-government'),
    S('casa-png','Civil Aviation Safety Authority','https://www.casapng.gov.pg/','png-government'),
    S('aic-png','PNG Accident Investigation Commission','https://aic.gov.pg/','png-government')
  ]
};

module.exports={pageBackfills,contextBackfills};
