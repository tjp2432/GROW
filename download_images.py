import urllib.request, urllib.parse, os, re, ssl, time

ctx = ssl._create_unverified_context()

products = [
    (1, "bong-vidrio-clasico-30cm", "Bong de Vidrio Clasico 30cm"),
    (2, "bong-silicona-plegable-20cm", "Bong de Silicona Plegable 20cm"),
    (3, "bong-percolador-doble-40cm", "Bong Percolador Doble 40cm"),
    (4, "mini-bong-viajero-12cm", "Mini Bong Viajero 12cm"),
    (5, "pipa-artesanal-madera", "Pipa Artesanal de Madera"),
    (6, "pipa-metalica-magnetica", "Pipa Metalica Magnetica"),
    (7, "pipa-vidrio-sherlock", "Pipa de Vidrio Sherlock"),
    (8, "set-pipas-mini-x3", "Set de Pipas Mini x3"),
    (9, "grinder-aluminio-4-piezas-50mm", "Grinder Aluminio 4 Piezas 50mm"),
    (10, "grinder-acrilico-transparente", "Grinder Acrilico Transparente"),
    (11, "grinder-electrico-automatico", "Grinder Electrico Automatico"),
    (12, "grinder-madera-premium-cenicero", "Grinder Madera Premium con Cenicero"),
    (13, "papeles-ocb-hemp-king-size-x50", "Papeles OCB Hemp King Size x50"),
    (14, "sedas-elements-ultra-thin", "Sedas Elements Ultra Thin"),
    (15, "pack-papeles-saborizados-5", "Pack Papeles Saborizados 5 sabores"),
    (16, "conos-armados-raw-king-size-x50", "Conos Armados Raw King Size x50"),
    (17, "vaporizador-portatil-xvape-starry-4", "Vaporizador Portatil XVAPE Starry 4.0"),
    (18, "vaporizador-escritorio-arizer-extreme-q", "Vaporizador Escritorio Arizer Extreme Q"),
    (19, "vape-pen-desechable", "Vape Pen Desechable"),
    (20, "panel-led-cultivo-full-spectrum-600w", "Panel LED Cultivo Full Spectrum 600W"),
    (21, "lampara-led-cultivo-100w", "Lampara LED Cultivo 100W"),
    (22, "timer-digital-cultivo", "Timer Digital para Cultivo"),
    (23, "kit-fertilizantes-top-crop-3x1l", "Kit Fertilizantes Top Crop 3x1L"),
    (24, "enraizante-organico-500ml", "Enraizante Organico 500ml"),
    (25, "medidor-ph-digital", "Medidor pH Digital"),
    (26, "filtros-carbon-x100", "Filtros de Carbon x100"),
    (27, "encendedor-electrico-recargable-usb", "Encendedor Electrico Recargable USB"),
    (28, "kit-limpieza-bongs", "Kit Limpieza para Bongs"),
    (29, "bolsa-hermetica-multi-uso-5-pack", "Bolsa Hermetica Multi-uso 5 Pack"),
    (30, "cenicero-silicona-plegable", "Cenicero de Silicona Plegable"),
    (31, "mochila-grower-edicion-limitada", "Mochila Grower Edicion Limitada"),
]

os.makedirs("static/images/products", exist_ok=True)

# Try multiple search sources for each product
search_sites = [
    "https://pevgrow.com/",
    "https://www.cannabislandia.com/",
    "https://www.growlobby.com/",
    "https://lacondesagrowshop.com/",
    "https://www.originalgrowers.com/",
]

for pid, slug, name in products:
    dest_path = f"static/images/products/{slug}.jpg"
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        print(f"EXISTS: {name}")
        continue

    found = False
    # Search Google
    for attempt in range(3):
        try:
            query = urllib.parse.quote(f"{name} grow shop")
            url = f"https://www.google.com/search?q={query}&tbm=isch"
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            resp = urllib.request.urlopen(req, timeout=15, context=ctx)
            html = resp.read().decode("utf-8", errors="replace")
            # Find JPEG/PNG URLs in the page
            imgs = re.findall(r'https?://[^"\'<>]+\.(?:jpg|jpeg|png|webp)(?:\?[^"\'<>]*)?', html)
            # Filter out icons and small images
            valid = [i for i in imgs if "logo" not in i.lower() and "icon" not in i.lower()
                     and len(i) > 30 and i.count("/") > 3]
            if valid:
                img_url = valid[0]
                urllib.request.urlretrieve(img_url, dest_path, context=ctx)
                size = os.path.getsize(dest_path)
                if size > 2000:
                    print(f"OK: {name} ({size} bytes)")
                    found = True
                    break
        except Exception as e:
            pass
        time.sleep(1)

    if not found:
        print(f"FAIL: {name}")

print("\nDone!")
