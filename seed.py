"""Seed script to populate the database with initial data."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app
from models import db, Category, Product, BlogPost

categories_data = [
    {
        'name': 'Bongs',
        'slug': 'bongs',
        'description': 'Bongs de vidrio, acrílico y silicona para una experiencia de fumar suave y refrescante.',
        'image': 'images/products/category-bongs.jpg'
    },
    {
        'name': 'Pipas',
        'slug': 'pipas',
        'description': 'Pipas artesanales, de metal, madera y vidrio. Clásicas y modernas.',
        'image': 'images/products/category-pipes.jpg'
    },
    {
        'name': 'Picadores',
        'slug': 'picadores',
        'description': 'Grinders de aluminio, acrílico y madera con imán y múltiples cámaras.',
        'image': 'images/products/category-grinders.jpg'
    },
    {
        'name': 'Papeles y Sedas',
        'slug': 'papeles',
        'description': 'Papeles de arroz, hemp, sin químicos y con sabores.',
        'image': 'images/products/category-papers.jpg'
    },
    {
        'name': 'Vaporizadores',
        'slug': 'vaporizadores',
        'description': 'Vaporizadores portátiles y de escritorio para hierbas secas y concentrados.',
        'image': 'images/products/category-vapes.jpg'
    },
    {
        'name': 'Iluminación',
        'slug': 'iluminacion',
        'description': 'Lámparas LED para cultivo indoor, sodio y sistemas completos.',
        'image': 'images/products/category-lighting.jpg'
    },
    {
        'name': 'Fertilizantes',
        'slug': 'fertilizantes',
        'description': 'Nutrientes orgánicos e inorgánicos para todas las etapas del cultivo.',
        'image': 'images/products/category-nutrients.jpg'
    },
    {
        'name': 'Accesorios',
        'slug': 'accesorios',
        'description': 'Todo lo que necesitas: sedas, filtros, encendedores, limpiadores y más.',
        'image': 'images/products/category-accessories.jpg'
    }
]

products_data = [
    # Bongs
    {
        'name': 'Bong de Vidrio Clásico 30cm',
        'slug': 'bong-vidrio-clasico-30cm',
        'image': 'images/products/bong-vidrio-clasico-30cm.jpg',
        'description': 'Bong de vidrio borosilicato de alta resistencia. Base reforzada, percolador de árbol y boquilla ancha. Incluye bowl de vidrio. Fácil de limpiar y perfecto para uso diario.',
        'short_description': 'Bong de vidrio borosilicato con percolador, 30cm de altura.',
        'price': 8500,
        'compare_price': 10500,
        'stock': 15,
        'featured': True,
        'category': 'bongs'
    },
    {
        'name': 'Bong de Silicona Plegable 20cm',
        'slug': 'bong-silicona-plegable-20cm',
        'image': 'images/products/bong-silicona-plegable-20cm.jpg',
        'description': 'Bong de silicona de grado alimenticio, plegable y resistente a golpes. Viene con bowl de vidrio y downstem. Ideal para llevar a todos lados.',
        'short_description': 'Bong de silicona plegable, irrompible y portátil.',
        'price': 5500,
        'stock': 20,
        'featured': True,
        'category': 'bongs'
    },
    {
        'name': 'Bong Percolador Doble 40cm',
        'slug': 'bong-percolador-doble-40cm',
        'image': 'images/products/bong-percolador-doble-40cm.jpg',
        'description': 'Bong artesanal con doble percolador en espiral y cámara de hielo. Vidrio grueso de 5mm. Filtración triple para hits ultra suaves.',
        'short_description': 'Bong artesanal con doble percolador y cámara de hielo.',
        'price': 14500,
        'stock': 8,
        'featured': True,
        'category': 'bongs'
    },
    {
        'name': 'Mini Bong Viajero 12cm',
        'slug': 'mini-bong-viajero-12cm',
        'image': 'images/products/mini-bong-viajero-12cm.jpg',
        'description': 'Mini bong de vidrio compacto perfecto para llevar. Incluye bowl y downstem. Cabe en cualquier mochila.',
        'short_description': 'Mini bong compacto de 12cm, ideal para viajes.',
        'price': 3500,
        'stock': 25,
        'category': 'bongs'
    },
    # Pipas
    {
        'name': 'Pipa Artesanal de Madera',
        'slug': 'pipa-artesanal-madera',
        'image': 'images/products/pipa-artesanal-madera.jpg',
        'description': 'Pipa tallada a mano en madera de olivo. Cada pieza es única con su propia veta natural. Incluye pantalla de metal removible.',
        'short_description': 'Pipa única tallada a mano en madera de olivo.',
        'price': 6200,
        'stock': 10,
        'featured': True,
        'category': 'pipas'
    },
    {
        'name': 'Pipa Metálica Magnética',
        'slug': 'pipa-metalica-magnetica',
        'image': 'images/products/pipa-metalica-magnetica.jpg',
        'description': 'Pipa de aleación de aluminio aeronáutico con tapa magnética. Incluye herramienta de limpieza y estuche de silicona. Diseño minimalista.',
        'short_description': 'Pipa de aluminio con tapa magnética y estuche.',
        'price': 3800,
        'stock': 30,
        'category': 'pipas'
    },
    {
        'name': 'Pipa de Vidrio Sherlock',
        'slug': 'pipa-vidrio-sherlock',
        'image': 'images/products/pipa-vidrio-sherlock.jpg',
        'description': 'Pipa estilo Sherlock de vidrio borosilicato con carburador. Diseño curvo clásico, fácil de limpiar.',
        'short_description': 'Pipa estilo Sherlock de vidrio borosilicato.',
        'price': 4200,
        'stock': 18,
        'featured': True,
        'category': 'pipas'
    },
    {
        'name': 'Set de Pipas Mini (x3)',
        'slug': 'set-pipas-mini-x3',
        'image': 'images/products/set-pipas-mini-x3.jpg',
        'description': 'Tres pipas de vidrio de colores: rojo, azul y verde. Perfectas para probar distintos diseños o para compartir.',
        'short_description': 'Tres pipas mini de vidrio de colores.',
        'price': 2800,
        'stock': 22,
        'category': 'pipas'
    },
    # Picadores
    {
        'name': 'Grinder Aluminio 4 Piezas 50mm',
        'slug': 'grinder-aluminio-4-piezas-50mm',
        'image': 'images/products/grinder-aluminio-4-piezas-50mm.jpg',
        'description': 'Grinder de aluminio CNC de 50mm con 4 cámaras. Imán potente, dientes afilados en forma de diamante y pantalla de malla fina. Incluye palita.',
        'short_description': 'Grinder de aluminio CNC 4 piezas, 50mm.',
        'price': 4500,
        'compare_price': 5500,
        'stock': 20,
        'featured': True,
        'category': 'picadores'
    },
    {
        'name': 'Grinder Acrílico Transparente',
        'slug': 'grinder-acrilico-transparente',
        'image': 'images/products/grinder-acrilico-transparente.jpg',
        'description': 'Grinder acrílico transparente de 40mm con imán. 2 piezas, fácil de usar. Ideal para principiantes.',
        'short_description': 'Grinder acrílico 2 piezas, 40mm.',
        'price': 1200,
        'stock': 50,
        'category': 'picadores'
    },
    {
        'name': 'Grinder Eléctrico Automático',
        'slug': 'grinder-electrico-automatico',
        'image': 'images/products/grinder-electrico-automatico.jpg',
        'description': 'Grinder eléctrico a pilas con botón pulsador. Tritura sin esfuerzo. Incluye compartimento para guardar. Carga máxima de 3g.',
        'short_description': 'Grinder eléctrico automático a pilas.',
        'price': 6800,
        'stock': 12,
        'featured': True,
        'category': 'picadores'
    },
    {
        'name': 'Grinder Madera Premium con Cenicero',
        'slug': 'grinder-madera-premium-cenicero',
        'image': 'images/products/grinder-madera-premium-cenicero.jpg',
        'description': 'Grinder de madera de haya con 3 cámaras. Incluye cenicero integrado en la base. Diseño ecológico y elegante.',
        'short_description': 'Grinder de madera de haya con cenicero integrado.',
        'price': 5200,
        'stock': 8,
        'category': 'picadores'
    },
    # Papeles
    {
        'name': 'Papeles OCB Hemp King Size x50',
        'slug': 'papeles-ocb-hemp-king-size',
        'image': 'images/products/papeles-ocb-hemp-king-size.jpg',
        'description': 'Papeles de cáñamo OCB King Size, 50 unidades. Sin químicos, quema lenta y pareja.',
        'short_description': 'Papeles OCB de cáñamo king size, 50u.',
        'price': 800,
        'stock': 100,
        'featured': True,
        'category': 'papeles'
    },
    {
        'name': 'Sedas Elements Ultra Thin',
        'slug': 'sedas-elements-ultra-thin',
        'image': 'images/products/sedas-elements-ultra-thin.jpg',
        'description': 'Sedas Elements ultra finas de 32mm. Quema casi invisible. 50 libros por paquete.',
        'short_description': 'Sedas ultra finas Elements 32mm, 50u.',
        'price': 650,
        'stock': 80,
        'category': 'papeles'
    },
    {
        'name': 'Pack Papeles Saborizados (5 sabores)',
        'slug': 'pack-papeles-saborizados',
        'image': 'images/products/pack-papeles-saborizados.jpg',
        'description': 'Pack con 5 paquetes de papeles saborizados: fresa, mango, menta, chocolate y uva. 24 unidades cada uno.',
        'short_description': 'Pack 5 sabores de papeles, 24u c/u.',
        'price': 2500,
        'stock': 35,
        'featured': True,
        'category': 'papeles'
    },
    {
        'name': 'Conos Armados Raw King Size x50',
        'slug': 'conos-armados-raw-king-size',
        'image': 'images/products/conos-armados-raw-king-size.jpg',
        'description': 'Conos pre-armados Raw king size con filtro. 50 unidades. Solo llenar y listo. Hechos de cáñamo orgánico.',
        'short_description': 'Conos Raw pre-armados king size, 50u.',
        'price': 1800,
        'stock': 45,
        'category': 'papeles'
    },
    # Vaporizadores
    {
        'name': 'Vaporizador Portátil XVAPE Starry 4.0',
        'slug': 'vaporizador-portatil-xvape-starry-4',
        'image': 'images/products/vaporizador-portatil-xvape-starry-4.jpg',
        'description': 'Vaporizador portátil con control digital de temperatura. Cámara de convección, batería de 2500mAh. Pantalla OLED. Ideal para hierbas secas.',
        'short_description': 'Vaporizador portátil con control digital de temperatura.',
        'price': 28500,
        'compare_price': 35000,
        'stock': 7,
        'featured': True,
        'category': 'vaporizadores'
    },
    {
        'name': 'Vaporizador de Escritorio Arizer Extreme Q',
        'slug': 'vaporizador-escritorio-arizer-extreme-q',
        'image': 'images/products/vaporizador-escritorio-arizer-extreme-q.jpg',
        'description': 'Vaporizador de mesa con sistema de balón y whip. Control remoto, temperatura digital precisa. Incluye todos los accesorios.',
        'short_description': 'Vaporizador de escritorio con balón y whip.',
        'price': 52000,
        'stock': 3,
        'featured': True,
        'category': 'vaporizadores'
    },
    {
        'name': 'Vape Pen Desechable',
        'slug': 'vape-pen-desechable',
        'image': 'images/products/vape-pen-desechable.jpg',
        'description': 'Vape pen desechable compacto. Sabor natural. Aprox. 300 caladas. Ideal para probar.',
        'short_description': 'Vape pen desechable, 300 caladas.',
        'price': 3200,
        'stock': 50,
        'category': 'vaporizadores'
    },
    # Iluminación
    {
        'name': 'Panel LED Cultivo Full Spectrum 600W',
        'slug': 'panel-led-cultivo-full-spectrum-600w',
        'image': 'images/products/panel-led-cultivo-full-spectrum-600w.jpg',
        'description': 'Panel LED de 600W para cultivo indoor con espectro completo. Incluye switches para vegetación y floración. Ventiladores silenciosos incorporados.',
        'short_description': 'Panel LED 600W full spectrum para indoor.',
        'price': 38500,
        'compare_price': 45000,
        'stock': 10,
        'featured': True,
        'category': 'iluminacion'
    },
    {
        'name': 'Lámpara LED Cultivo 100W',
        'slug': 'lampara-led-cultivo-100w',
        'image': 'images/products/lampara-led-cultivo-100w.jpg',
        'description': 'Lámpara LED de 100W con espectro ajustable. Ideal para espacios pequeños o crecimiento. Plug & play.',
        'short_description': 'Lámpara LED 100W para espacios pequeños.',
        'price': 9500,
        'stock': 15,
        'category': 'iluminacion'
    },
    {
        'name': 'Timer Digital para Cultivo',
        'slug': 'timer-digital-cultivo',
        'image': 'images/products/timer-digital-cultivo.jpg',
        'description': 'Timer digital programable 24h para ciclos de luz. 2 tomas. Fácil configuración.',
        'short_description': 'Timer digital programable para ciclos de luz.',
        'price': 2200,
        'stock': 30,
        'category': 'iluminacion'
    },
    # Fertilizantes
    {
        'name': 'Kit Fertilizantes Top Crop (3x1L)',
        'slug': 'kit-fertilizantes-top-crop-3x1l',
        'image': 'images/products/kit-fertilizantes-top-crop-3x1l.jpg',
        'description': 'Kit completo Top Crop: Top Veg, Top Bloom y Top Candy. Pack 3 botellas de 1 litro cada una. Para todo el ciclo de cultivo.',
        'short_description': 'Kit Top Crop 3x1L para ciclo completo.',
        'price': 8500,
        'compare_price': 10200,
        'stock': 18,
        'featured': True,
        'category': 'fertilizantes'
    },
    {
        'name': 'Enraizante Orgánico 500ml',
        'slug': 'enraizante-organico-500ml',
        'image': 'images/products/enraizante-organico-500ml.jpg',
        'description': 'Enraizante orgánico concentrado. Estimula el desarrollo radicular. Apto para cultivo orgánico. 500ml rinde hasta 100L de solución.',
        'short_description': 'Enraizante orgánico concentrado 500ml.',
        'price': 3200,
        'stock': 25,
        'category': 'fertilizantes'
    },
    {
        'name': 'Medidor pH Digital',
        'slug': 'medidor-ph-digital',
        'image': 'images/products/medidor-ph-digital.jpg',
        'description': 'Medidor de pH digital con calibración automática. Rango 0-14. Exactitud ±0.01. Incluye soluciones de calibración.',
        'short_description': 'Medidor de pH digital profesional.',
        'price': 4800,
        'stock': 20,
        'category': 'fertilizantes'
    },
    # Accesorios
    {
        'name': 'Filtros de Carbón x100',
        'slug': 'filtros-carbon-x100',
        'image': 'images/products/filtros-carbon-x100.jpg',
        'description': 'Filtros de carbón activado de 8mm. 100 unidades por paquete. Reducen impurezas y suavizan el humo.',
        'short_description': '100 filtros de carbón activado 8mm.',
        'price': 900,
        'stock': 60,
        'featured': True,
        'category': 'accesorios'
    },
    {
        'name': 'Encendedor Eléctrico Recargable USB',
        'slug': 'encendedor-electrico-recargable-usb',
        'image': 'images/products/encendedor-electrico-recargable-usb.jpg',
        'description': 'Encendedor eléctrico por arco voltaico. Recargable por USB. Resistente al viento. Sin gas ni llama abierta.',
        'short_description': 'Encendedor arco voltaico recargable USB.',
        'price': 2800,
        'stock': 35,
        'featured': True,
        'category': 'accesorios'
    },
    {
        'name': 'Kit Limpieza para Bongs',
        'slug': 'kit-limpieza-bongs',
        'image': 'images/products/kit-limpieza-bongs.jpg',
        'description': 'Kit completo de limpieza: 250ml solución limpiadora, cepillos de diferentes tamaños y soporte para secado.',
        'short_description': 'Kit completo de limpieza para bongs.',
        'price': 3500,
        'stock': 20,
        'category': 'accesorios'
    },
    {
        'name': 'Bolsa Hermética Multi-uso 5 Pack',
        'slug': 'bolsa-hermetica-multiuso-5-pack',
        'image': 'images/products/bolsa-hermetica-multiuso-5-pack.jpg',
        'description': '5 bolsas herméticas con cierre zip de diferentes tamaños. Mantienen la frescura. Material Mylar.',
        'short_description': '5 bolsas herméticas Mylar de varios tamaños.',
        'price': 1500,
        'stock': 40,
        'category': 'accesorios'
    },
    {
        'name': 'Cenicero de Silicona Plegable',
        'slug': 'cenicero-silicona-plegable',
        'image': 'images/products/cenicero-silicona-plegable.jpg',
        'description': 'Cenicero de silicona plegable con tapa. Atrapa olores. Fácil de limpiar. Ideal para llevar.',
        'short_description': 'Cenicero plegable de silicona con tapa.',
        'price': 1800,
        'stock': 30,
        'category': 'accesorios'
    },
    {
        'name': 'Mochila Grower Edición Limitada',
        'slug': 'mochila-grower-edicion-limitada',
        'image': 'images/products/mochila-grower-edicion-limitada.jpg',
        'description': 'Mochila edición limitada Perrone\'s INC. Compartimento acolchado, bolsillos organizadores y diseño discreto.',
        'short_description': 'Mochila edición limitada Perrone\'s INC.',
        'price': 12000,
        'stock': 5,
        'featured': True,
        'category': 'accesorios'
    }
]

blog_posts_data = [
    {
        'title': 'Guía Completa para Principiantes en el Cultivo Indoor',
        'slug': 'guia-completa-cultivo-indoor-principiantes',
        'image': 'images/products/guia-completa-cultivo-indoor-principiantes.jpg',
        'image': 'images/blog/guia-principiantes.jpg',
        'excerpt': 'Todo lo que necesitas saber para empezar tu primer cultivo indoor: espacio, luces, ventilación y nutrientes.',
        'content': """<h2>Introducción al Cultivo Indoor</h2>
<p>El cultivo indoor te permite tener control total sobre el ambiente de tus plantas. Ya no dependes de las estaciones ni del clima exterior. Con el equipo adecuado, puedes obtener cosechas de alta calidad durante todo el año.</p>

<h2>¿Qué necesitas para empezar?</h2>
<h3>1. El Espacio</h3>
<p>Puedes usar un armario, un grow tent o una habitación dedicada. Para empezar, un espacio de 60x60x140cm es suficiente para 1-2 plantas. Asegúrate de que sea un espacio reflectante (pintura blanca o mylar).</p>

<h3>2. La Iluminación</h3>
<p>La luz es el factor más importante. Para principiantes, recomendamos:</p>
<ul>
<li><strong>LED Full Spectrum:</strong> Eficientes, poco calor, buena cobertura</li>
<li><strong>CFL (bajo consumo):</strong> Económicos, ideales para espacios pequeños</li>
</ul>

<h3>3. Ventilación</h3>
<p>Necesitas 3 elementos básicos:</p>
<ul>
<li>Extractor para sacar el aire caliente</li>
<li>Intractor pasivo o activo para entrada de aire fresco</li>
<li>Ventilador interior para movimiento de aire</li>
</ul>

<h3>4. Sustrato y Macetas</h3>
<p>Recomendamos empezar con tierra liviana y macetas de tela (smart pots) que permiten mejor drenaje y aireación de raíces.</p>

<h2>Ciclo de Vida de la Planta</h2>
<h3>Germinación (1-2 semanas)</h3>
<p>Coloca la semilla en un vaso con agua 24h, luego pásala a un paño húmedo hasta que salga la raíz. Una vez lista, trasplanta a su maceta definitiva.</p>

<h3>Vegetación (3-8 semanas)</h3>
<p>Durante esta fase, la planta desarrolla su estructura. Mantén 18-20 horas de luz por día. Es crucial no estresar la planta con cambios bruscos.</p>

<h3>Floración (8-12 semanas)</h3>
<p>Cambia el ciclo de luz a 12/12 (12 horas luz, 12 horas oscuridad total). Aquí es donde se forman los cogollos.</p>

<h2>Errores Comunes de Principiantes</h2>
<ol>
<li><strong>Regar en exceso:</strong> La causa #1 de muerte de plantas. Deja que la tierra se seque entre riegos.</li>
<li><strong>Sobrefertilizar:</strong> Menos es más. Sigue las dosis recomendadas.</li>
<li><strong>No medir pH:</strong> Mantén el pH entre 6.0 y 6.8 en tierra.</li>
<li><strong>Fugas de luz:</strong> Durante la floración, cualquier fuga de luz puede causar estrés.</li>
</ol>

<h2>Equipo Recomendado para Empezar</h2>
<p>En Perrone's INC tenemos todo lo que necesitas para tu primer cultivo. Desde paneles LED hasta kits de fertilizantes. Visita nuestra sección de <a href="/productos">productos</a> para ver nuestro catálogo completo.</p>""",
        'category': 'Cultivo',
        'tags': 'cultivo, indoor, principiantes, guia, marihuana',
        'published': True,
        'featured': True
    },
    {
        'title': 'Cómo Elegir el Mejor Vaporizador para tus Necesidades',
        'slug': 'como-elegir-mejor-vaporizador',
        'image': 'images/products/como-elegir-mejor-vaporizador.jpg',
        'image': 'images/blog/vapo1.jpg',
        'excerpt': 'Guía para elegir entre vaporizadores portátiles, de escritorio, y qué características tener en cuenta.',
        'content': """<h2>¿Por qué Vaporizar?</h2>
<p>La vaporización se ha convertido en una de las formas más populares de consumo. Al no producir combustión, evitas los subproductos tóxicos del humo y obtienes un sabor más puro y limpio.</p>

<h2>Tipos de Vaporizadores</h2>

<h3>1. Vaporizadores Portátiles</h3>
<p>Ideales para quien busca discreción y movilidad. Características a considerar:</p>
<ul>
<li><strong>Autonomía de batería:</strong> Busca mínimo 2000mAh</li>
<li><strong>Tipo de calentamiento:</strong> Convección (mejor sabor) vs Conducción (más denso)</li>
<li><strong>Control de temperatura:</strong> Preciso y ajustable</li>
<li><strong>Facilidad de limpieza:</strong> Fundamental para el mantenimiento</li>
</ul>

<h3>2. Vaporizadores de Escritorio</h3>
<p>Para uso en casa, ofrecen la mejor experiencia:</p>
<ul>
<li><strong>Sistema de balón:</strong> Llenas una bolsa y compartes</li>
<li><strong>Sistema whip:</strong> Manguera directa para uso individual</li>
<li><strong>Potencia:</strong> Mayor capacidad de carga y control preciso</li>
</ul>

<h3>3. Vape Pens</h3>
<p>Compactos y discretos, perfectos para llevar. Ideales para quienes recién empiezan.</p>

<h2>Características Clave</h2>
<table>
<tr><td><strong>Control de Temperatura</strong></td><td>Busca rangos de 160°C a 220°C</td></tr>
<tr><td><strong>Materiales</strong></td><td>Acero inoxidable y vidrio son los mejores</td></tr>
<tr><td><strong>Garantía</strong></td><td>Mínimo 1 año, ideal 2+ años</td></tr>
<tr><td><strong>Flujo de aire</strong></td><td>Regulable para personalizar la experiencia</td></tr>
</table>

<h2>Recomendación Perrone's INC</h2>
<p>Para quienes empiezan, recomendamos el XVAPE Starry 4.0: calidad-precio inmejorable. Para los más exigentes, el Arizer Extreme Q es el rey de los vaporizadores de escritorio.</p>""",
        'category': 'Vaporización',
        'tags': 'vaporizador, vape, hierbas, salud',
        'published': True,
        'featured': True
    },
    {
        'title': 'Historia y Cultura Cannábica: De lo Sagrado a lo Moderno',
        'slug': 'historia-cultura-cannabica-sagrado-moderno',
        'image': 'images/products/historia-cultura-cannabica-sagrado-moderno.jpg',
        'image': 'images/blog/belgrano.jpg',
        'excerpt': 'Un recorrido por la historia del cannabis desde sus usos ancestrales hasta la cultura moderna.',
        'content': """<h2>Raíces Antiguas</h2>
<p>El cannabis acompaña a la humanidad desde hace milenios. Las primeras evidencias de su uso datan del año 4000 a.C. en China, donde se utilizaba tanto como fibra textil como con fines medicinales.</p>

<h2>El Cannabis en la Medicina Tradicional</h2>
<p>En la India, el cannabis era considerado una planta sagrada. Los textos védicos lo mencionan como una fuente de alegría y liberación. En el antiguo Egipto, se usaba para tratar el glaucoma y la inflamación.</p>

<h2>La Llegada a América</h2>
<p>El cannabis llegó a América con los colonizadores españoles, que lo cultivaban por su fibra. Fue en el siglo XX cuando comenzó la estigmatización y posterior prohibición.</p>

<h2>La Revolución Contracultural</h2>
<p>En los años 60 y 70, el cannabis se convirtió en símbolo de la contracultura. Movimientos hippies, músicos de jazz y rock, y artistas de todo tipo adoptaron la planta como emblema de libertad y creatividad.</p>

<h2>La Era Moderna: Legalización y Regulación</h2>
<p>En las últimas décadas, el paradigma ha cambiado drásticamente. Países como Uruguay, Canadá y varios estados de EE.UU. han legalizado el cannabis. Hoy hablamos de:</p>
<ul>
<li><strong>Uso medicinal:</strong> Reconocido por sus propiedades terapéuticas</li>
<li><strong>Uso recreativo:</strong> Regulado y controlado</li>
<li><strong>Industria:</strong> Un mercado global multimillonario</li>
</ul>

<h2>La Cultura Hoy</h2>
<p>La cultura cannábica moderna es diversa e inclusiva. Desde growers que comparten conocimientos en redes sociales, hasta chefs que crean experiencias gastronómicas, pasando por la moda y el arte.</p>

<p>En Perrone's INC celebramos esta cultura con respeto y pasión. Nuestro objetivo es ofrecer productos de calidad mientras educamos y construimos una comunidad responsable.</p>""",
        'category': 'Cultura',
        'tags': 'historia, cultura, cannabis, legalizacion',
        'published': True,
        'featured': True
    },
    {
        'title': 'Tips para Mantener tus Accesorios como Nuevos',
        'slug': 'tips-mantener-accesorios-como-nuevos',
        'image': 'images/products/tips-mantener-accesorios-como-nuevos.jpg',
        'image': 'images/blog/2116.jpg',
        'excerpt': 'Cómo limpiar y mantener tus bongs, pipas y grinders para que duren más y funcionen mejor.',
        'content': """<h2>Por qué es Importante la Limpieza</h2>
<p>Mantener tus accesorios limpios no solo es cuestión de estética. Un bong o pipa sucio puede afectar el sabor, reducir la eficiencia y hasta ser perjudicial para la salud.</p>

<h2>Limpieza de Bongs</h2>
<h3>Método Rápido (Limpieza Diaria)</h3>
<p>Enjuaga con agua caliente después de cada uso. Esto evita que la resina se acumule.</p>

<h3>Limpieza Profunda (Semanal)</h3>
<ol>
<li>Vacía el agua y desarma todas las piezas</li>
<li>Coloca las partes en una bolsa con alcohol isopropílico al 90% y sal gruesa</li>
<li>Agita vigorosamente por 2-3 minutos</li>
<li>Enjuaga con agua caliente hasta eliminar todo residuo</li>
<li>Deja secar completamente antes de armar</li>
</ol>

<h2>Limpieza de Pipas</h2>
<p>Las pipas requieren atención especial por sus formas intrincadas:</p>
<ul>
<li>Usa alcohol isopropílico y sal</li>
<li>Para pipas de vidrio: sumerge en alcohol toda la noche</li>
<li>Para pipas de metal: puedes hervirlas en agua por 10 minutos</li>
<li>Usa limpiapipas para alcanzar zonas difíciles</li>
</ul>

<h2>Mantenimiento de Grinders</h2>
<ul>
<li>Limpia los dientes con un cepillo pequeño después de cada uso</li>
<li>Congela el grinder por 30 minutos para desprender resina pegada</li>
<li>Lava con alcohol isopropílico una vez al mes</li>
<li>Lubrica la rosca con aceite vegetal comestible si está dura</li>
</ul>

<h2>Consejos Generales</h2>
<ul>
<li>No uses agua hirviendo en vidrio frío (puede romperlo)</li>
<li>Evita limpiadores con químicos agresivos</li>
<li>Ten un kit de limpieza dedicado</li>
<li>Cambia el agua del bong después de cada sesión</li>
</ul>

<p>En nuestro catálogo encontrarás kits de limpieza profesionales para mantener tus accesorios en perfecto estado. <a href="/productos/accesorios">Ver accesorios de limpieza</a></p>""",
        'category': 'Accesorios',
        'tags': 'limpieza, mantenimiento, bongs, pipas, grinders',
        'published': True,
        'featured': False
    },
    {
        'title': 'Guía de Nutrientes: Qué Darle a tus Plantas en Cada Etapa',
        'slug': 'guia-nutrientes-cada-etapa',
        'image': 'images/products/guia-nutrientes-cada-etapa.jpg',
        'excerpt': 'Conocé qué nutrientes necesita tu planta en vegetación, floración y precosecha.',
        'content': """<h2>La Alimentación de tus Plantas</h2>
<p>Una nutrición adecuada es la diferencia entre una cosecha mediocre y una espectacular. Cada etapa del ciclo de vida requiere un perfil nutricional específico.</p>

<h2>Etapa de Vegetación</h2>
<h3>Macronutrientes Clave:</h3>
<ul>
<li><strong>Nitrógeno (N):</strong> Alto - Fundamental para hojas y tallos</li>
<li><strong>Fósforo (P):</strong> Medio - Desarrollo radicular</li>
<li><strong>Potasio (K):</strong> Medio - Transporte de nutrientes</li>
</ul>
<p>Usa fertilizante de vegetación con alta relación N. Recomendamos Top Veg de Top Crop.</p>

<h2>Etapa de Floración</h2>
<h3>Cambio de Perfil:</h3>
<ul>
<li><strong>Nitrógeno (N):</strong> Bajo - Reducir progresivamente</li>
<li><strong>Fósforo (P):</strong> Alto - Formación de cogollos</li>
<li><strong>Potasio (K):</strong> Alto - Producción de resina</li>
</ul>
<p>Cambia a fertilizante de floración. El Top Bloom es excelente para esta etapa.</p>

<h2>Etapa de Engorde y Maduración</h2>
<ul>
<li>Agrega un potenciador de cogollos como Top Candy</li>
<li>Mantén buen nivel de Potasio</li>
<li>Reduce el Nitrógeno al mínimo</li>
</ul>

<h2>Precosecha (Flushing)</h2>
<p>2 semanas antes de cosechar, usa solo agua pH balanceada. Esto elimina residuos de fertilizantes y mejora el sabor final.</p>

<h2>Problemas Comunes</h2>
<table>
<tr><td><strong>Hojas amarillas abajo</strong></td><td>Falta de Nitrógeno</td></tr>
<tr><td><strong>Puntas quemadas</strong></td><td>Exceso de fertilizante</td></tr>
<tr><td><strong>Hojas enrolladas</strong></td><td>Estrés por calor o sobrefertilización</td></tr>
<tr><td><strong>Manchas marrones</strong></td><td>Posible deficiencia de Calcio/Magnesio</td></tr>
</table>

<h2>Recomendación Perrone's INC</h2>
<p>Nuestro kit Top Crop 3x1L tiene todo lo necesario para el ciclo completo. Ideal para principiantes y expertos.</p>""",
        'category': 'Cultivo',
        'tags': 'nutrientes, fertilizantes, cultivo, floracion, vegetacion',
        'published': True,
        'featured': False
    }
]


def seed():
    with app.app_context():
        db.create_all()

        if Category.query.first():
            print("La base de datos ya tiene datos. Ejecutá 'drop all' si querés reseedear.")
            return

        for cat_data in categories_data:
            cat = Category(**cat_data)
            db.session.add(cat)
        db.session.commit()
        print(f"Categorías creadas: {len(categories_data)}")

        cat_map = {c.slug: c.id for c in Category.query.all()}

        for prod_data in products_data:
            category_slug = prod_data.pop('category')
            product = Product(**prod_data, category_id=cat_map[category_slug])
            db.session.add(product)
        db.session.commit()
        print(f"Productos creados: {len(products_data)}")

        for post_data in blog_posts_data:
            post = BlogPost(**post_data)
            db.session.add(post)
        db.session.commit()
        print(f"Artículos de blog creados: {len(blog_posts_data)}")

        print("Base de datos poblada exitosamente!")


if __name__ == '__main__':
    seed()
