import urllib.request, os, re, ssl

ctx = ssl._create_unverified_context()

# Map products to likely product page URLs on pevgrow.com
product_urls = {
    1: "https://pevgrow.com/bong-cristal-percolador-ice-fuma-marihuana-30-cm.html",
    2: "https://pevgrow.com/bong-de-silicona-plegable.html",
    9: "https://pevgrow.com/grinder-aluminio-4-partes-50mm.html",
    # add more as we find them
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

for pid, page_url in product_urls.items():
    try:
        req = urllib.request.Request(page_url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=15, context=ctx)
        html = resp.read().decode("utf-8", errors="replace")
        
        # Find og:image or first large product image
        og = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html)
        if og:
            img_url = og.group(1)
        else:
            imgs = re.findall(r'<img[^>]+src="([^"]+\.(?:jpg|jpeg|png))"[^>]*>', html)
            imgs = [i for i in imgs if "logo" not in i.lower() and "icon" not in i.lower() and "banner" not in i.lower()]
            img_url = imgs[0] if imgs else None
        
        if img_url:
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            elif img_url.startswith("/"):
                img_url = "https://pevgrow.com" + img_url
            
            # Map pid to slug
            slug_map = {1: "bong-vidrio-clasico-30cm", 2: "bong-silicona-plegable-20cm", 9: "grinder-aluminio-4-piezas-50mm"}
            slug = slug_map[pid]
            dest = f"static/images/products/{slug}.jpg"
            urllib.request.urlretrieve(img_url, dest, context=ctx)
            print(f"OK {pid}: {slug} ({os.path.getsize(dest)} bytes) - {img_url[:80]}")
        else:
            print(f"FAIL {pid}: no image found")
    except Exception as e:
        print(f"FAIL {pid}: {str(e)[:80]}")
