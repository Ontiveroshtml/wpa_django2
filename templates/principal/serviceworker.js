console.log("Hola Alumnos");

globalThis.addEventListener("install", event => {
     caches.open("pwa").then(cache => {
         cache.addAll(["manifest.json", "/static/1.jpg", "/static/2.jpg", "/static/3.jpg", "/static/4.jpg", "/static/5.jpg",]);
     })
})
