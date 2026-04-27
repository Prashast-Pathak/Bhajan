// सनातन ज्ञान सागर — Service Worker
// Enables offline access to cached pages and content

const CACHE_NAME = 'sgs-cache-v3';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/bhajans.html',
  '/bhajan.html',
  '/bhagavad-gita.html',
  '/shlokas.html',
  '/prayers.html',
  '/upanishads.html',
  '/wisdom.html',
  '/favorites.html',
  '/about.html',
  '/privacy-policy.html',
  '/contact.html',
  '/data/bhajans.json',
  '/data/gita.json',
  '/data/shlokas.json',
  '/data/prayers.json',
  '/data/upanishads.json',
  '/data/wisdom.json',
  '/manifest.json',
  'https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Lato:wght@300;400;700&display=swap'
];

// Install: cache all static assets
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[SW] Caching static assets');
      return cache.addAll(STATIC_ASSETS);
    }).catch(err => console.error('[SW] Cache install error:', err))
  );
});

// Activate: clean up old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.map(k => {
          if (k !== CACHE_NAME) {
            console.log('[SW] Deleting old cache:', k);
            return caches.delete(k);
          }
        })
      )
    ).then(() => self.clients.claim())
  );
});

// Fetch: serve from cache, fall back to network
self.addEventListener('fetch', event => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  // Skip non-http(s) requests
  if (!event.request.url.startsWith('http')) return;

  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) {
        // Serve from cache, then update cache in background (stale-while-revalidate)
        const fetchPromise = fetch(event.request).then(response => {
          if (response && response.status === 200) {
            caches.open(CACHE_NAME).then(cache => {
              cache.put(event.request, response.clone());
            });
          }
          return response;
        }).catch(() => cached); // On network fail, use cached version
        return cached;
      }

      // Not in cache — fetch from network and cache it
      return fetch(event.request).then(response => {
        if (!response || response.status !== 200 || response.type === 'opaque') {
          return response;
        }
        const responseToCache = response.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, responseToCache);
        });
        return response;
      }).catch(() => {
        // Offline fallback for HTML pages
        if (event.request.headers.get('Accept') && event.request.headers.get('Accept').includes('text/html')) {
          return caches.match('/index.html');
        }
      });
    })
  );
});
