import os
import uuid
from datetime import datetime
from functools import wraps

from flask import (Flask, render_template, request, redirect, url_for,
                   flash, jsonify, session, abort)
from flask_login import (LoginManager, login_user, logout_user,
                         login_required, current_user)
from werkzeug.utils import secure_filename

from config import Config
from models import db, User, Category, Product, Order, OrderItem, BlogPost, Contact
from forms import (LoginForm, ProductForm, BlogForm, ContactForm, CheckoutForm)

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'
login_manager.login_message = 'Inicia sesión para acceder al panel.'

with app.app_context():
    db.create_all()
    if not User.query.filter_by(is_admin=True).first():
        admin = User(
            username='admin',
            email='admin@perronesinc.com',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

def save_image(file, subfolder='products'):
    if file and allowed_file(file.filename):
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4().hex}.{ext}"
        path = os.path.join(app.config['UPLOAD_FOLDER'], subfolder, filename)
        file.save(path)
        return f"images/{subfolder}/{filename}"
    return None

def slugify(text):
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text

@app.context_processor
def inject_globals():
    categories = Category.query.filter_by(active=True).all() if hasattr(Category, 'active') else Category.query.all()
    cart_count = 0
    cart = session.get('cart', {})
    if cart:
        cart_count = sum(item['quantity'] for item in cart.values())
    return dict(categories=categories, cart_count=cart_count, now=datetime.now())

@app.route('/')
def index():
    featured_products = Product.query.filter_by(featured=True, active=True).limit(8).all()
    latest_products = Product.query.filter_by(active=True).order_by(Product.created_at.desc()).limit(4).all()
    blog_posts = BlogPost.query.filter_by(published=True).order_by(BlogPost.created_at.desc()).limit(3).all()
    categories = Category.query.all()
    return render_template('index.html',
                         featured_products=featured_products,
                         latest_products=latest_products,
                         blog_posts=blog_posts,
                         categories=categories)

@app.route('/productos')
def products():
    page = request.args.get('page', 1, type=int)
    category_slug = request.args.get('categoria')
    search = request.args.get('buscar')

    query = Product.query.filter_by(active=True)

    if category_slug:
        category = Category.query.filter_by(slug=category_slug).first_or_404()
        query = query.filter_by(category_id=category.id)

    if search:
        query = query.filter(
            Product.name.ilike(f'%{search}%') |
            Product.description.ilike(f'%{search}%')
        )

    query = query.order_by(Product.created_at.desc())
    products_page = query.paginate(page=page, per_page=app.config['PER_PAGE'], error_out=False)
    categories = Category.query.all()

    return render_template('products.html',
                         products=products_page,
                         categories=categories,
                         current_category=category_slug,
                         search=search)

@app.route('/producto/<slug>')
def product_detail(slug):
    product = Product.query.filter_by(slug=slug, active=True).first_or_404()
    related = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id,
        Product.active == True
    ).limit(4).all()
    return render_template('product.html', product=product, related=related)

@app.route('/api/cart', methods=['GET'])
def api_cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, item in cart.items():
        product = db.session.get(Product, int(pid))
        if product:
            subtotal = product.price * item['quantity']
            total += subtotal
            items.append({
                'id': product.id,
                'name': product.name,
                'slug': product.slug,
                'price': product.price,
                'quantity': item['quantity'],
                'image': product.image,
                'subtotal': round(subtotal, 2)
            })
    return jsonify({'items': items, 'total': round(total, 2), 'count': len(items)})

@app.route('/api/cart/add', methods=['POST'])
def api_cart_add():
    data = request.get_json()
    product_id = str(data.get('product_id'))
    quantity = int(data.get('quantity', 1))
    product = db.session.get(Product, int(product_id))
    if not product or not product.active:
        return jsonify({'error': 'Producto no encontrado'}), 404

    cart = session.get('cart', {})
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {'quantity': quantity}

    session['cart'] = cart
    session.modified = True
    total_items = sum(item['quantity'] for item in cart.values())
    return jsonify({'success': True, 'count': total_items})

@app.route('/api/cart/update', methods=['POST'])
def api_cart_update():
    data = request.get_json()
    product_id = str(data.get('product_id'))
    quantity = int(data.get('quantity', 0))
    cart = session.get('cart', {})
    if quantity <= 0:
        cart.pop(product_id, None)
    else:
        cart[product_id] = {'quantity': quantity}
    session['cart'] = cart
    session.modified = True
    return jsonify({'success': True})

@app.route('/api/cart/remove', methods=['POST'])
def api_cart_remove():
    data = request.get_json()
    product_id = str(data.get('product_id'))
    cart = session.get('cart', {})
    cart.pop(product_id, None)
    session['cart'] = cart
    session.modified = True
    return jsonify({'success': True})

@app.route('/carrito')
def cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, item in cart.items():
        product = db.session.get(Product, int(pid))
        if product:
            subtotal = product.price * item['quantity']
            total += subtotal
            items.append({
                'id': product.id,
                'name': product.name,
                'slug': product.slug,
                'price': product.price,
                'quantity': item['quantity'],
                'image': product.image,
                'subtotal': round(subtotal, 2)
            })
    return render_template('cart.html', items=items, total=round(total, 2))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', {})
    if not cart:
        flash('Tu carrito está vacío.', 'warning')
        return redirect(url_for('cart'))

    form = CheckoutForm()
    if current_user.is_authenticated:
        form.email.data = current_user.email

    if form.validate_on_submit():
        items = []
        subtotal = 0
        for pid, item in cart.items():
            product = db.session.get(Product, int(pid))
            if product:
                items.append({
                    'product': product,
                    'quantity': item['quantity'],
                    'price': product.price
                })
                subtotal += product.price * item['quantity']

        shipping = subtotal * 0.1 if subtotal < 10000 else 0
        total = subtotal + shipping

        order_number = f"PIC-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        order = Order(
            order_number=order_number,
            user_id=current_user.id if current_user.is_authenticated else None,
            full_name=form.full_name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
            notes=form.notes.data,
            subtotal=round(subtotal, 2),
            shipping=round(shipping, 2),
            total=round(total, 2),
            payment_method='transferencia'
        )
        db.session.add(order)
        db.session.flush()

        for item in items:
            oi = OrderItem(
                order_id=order.id,
                product_id=item['product'].id,
                product_name=item['product'].name,
                quantity=item['quantity'],
                price=item['price']
            )
            db.session.add(oi)

        db.session.commit()
        session.pop('cart', None)
        return redirect(url_for('order_confirmation', order_number=order.order_number))

    return render_template('checkout.html', form=form)

@app.route('/pedido/<order_number>')
def order_confirmation(order_number):
    order = Order.query.filter_by(order_number=order_number).first_or_404()
    return render_template('order_confirmation.html', order=order)

@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('categoria')
    query = BlogPost.query.filter_by(published=True)
    if category:
        query = query.filter_by(category=category)
    posts = query.order_by(BlogPost.created_at.desc()).paginate(
        page=page, per_page=app.config['PER_PAGE'], error_out=False)
    categories = db.session.query(BlogPost.category).filter_by(published=True).distinct().all()
    return render_template('blog.html', posts=posts, categories=[c[0] for c in categories if c[0]])

@app.route('/blog/<slug>')
def blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug, published=True).first_or_404()
    recent = BlogPost.query.filter(
        BlogPost.published == True,
        BlogPost.id != post.id
    ).order_by(BlogPost.created_at.desc()).limit(3).all()
    return render_template('blog_post.html', post=post, recent=recent)

@app.route('/nosotros')
def about():
    return render_template('about.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(contact)
        db.session.commit()
        flash('Mensaje enviado correctamente. Te responderemos pronto.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data) and user.is_admin:
            login_user(user)
            flash('Bienvenido al panel de administración.', 'success')
            return redirect(url_for('admin_dashboard'))
        flash('Credenciales inválidas.', 'error')
    return render_template('admin/login.html', form=form)

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    stats = {
        'products': Product.query.count(),
        'orders': Order.query.count(),
        'contacts': Contact.query.filter_by(read=False).count(),
        'posts': BlogPost.query.count(),
        'revenue': db.session.query(db.func.sum(Order.total)).filter(
            Order.status != 'cancelled').scalar() or 0,
        'pending_orders': Order.query.filter_by(status='pending').count()
    }
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html', stats=stats, recent_orders=recent_orders)

@app.route('/admin/productos')
@login_required
@admin_required
def admin_products():
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.created_at.desc()).paginate(
        page=page, per_page=app.config['PER_PAGE'], error_out=False)
    return render_template('admin/products.html', products=products)

@app.route('/admin/productos/nuevo', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_product_new():
    form = ProductForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            slug=slugify(form.name.data),
            description=form.description.data,
            short_description=form.short_description.data,
            price=form.price.data,
            compare_price=form.compare_price.data,
            stock=form.stock.data,
            category_id=form.category_id.data,
            featured=form.featured.data,
            active=form.active.data
        )
        if 'image' in request.files:
            img = request.files['image']
            if img.filename:
                product.image = save_image(img, 'products')
        db.session.add(product)
        db.session.commit()
        flash('Producto creado correctamente.', 'success')
        return redirect(url_for('admin_products'))
    return render_template('admin/product_form.html', form=form, title='Nuevo Producto')

@app.route('/admin/productos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_product_edit(id):
    product = db.session.get(Product, id)
    if not product:
        abort(404)
    form = ProductForm(obj=product)
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        product.name = form.name.data
        product.slug = slugify(form.name.data)
        product.description = form.description.data
        product.short_description = form.short_description.data
        product.price = form.price.data
        product.compare_price = form.compare_price.data
        product.stock = form.stock.data
        product.category_id = form.category_id.data
        product.featured = form.featured.data
        product.active = form.active.data
        if 'image' in request.files:
            img = request.files['image']
            if img.filename:
                old_img = product.image
                product.image = save_image(img, 'products')
                if old_img:
                    old_path = os.path.join(app.config['UPLOAD_FOLDER'], old_img)
                    if os.path.exists(old_path):
                        os.remove(old_path)
        db.session.commit()
        flash('Producto actualizado.', 'success')
        return redirect(url_for('admin_products'))
    return render_template('admin/product_form.html', form=form, title='Editar Producto', product=product)

@app.route('/admin/productos/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_product_delete(id):
    product = db.session.get(Product, id)
    if product:
        if product.image:
            path = os.path.join(app.config['UPLOAD_FOLDER'], product.image)
            if os.path.exists(path):
                os.remove(path)
        db.session.delete(product)
        db.session.commit()
        flash('Producto eliminado.', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/pedidos')
@login_required
@admin_required
def admin_orders():
    page = request.args.get('page', 1, type=int)
    status = request.args.get('status')
    query = Order.query
    if status:
        query = query.filter_by(status=status)
    orders = query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=app.config['PER_PAGE'], error_out=False)
    return render_template('admin/orders.html', orders=orders)

@app.route('/admin/pedidos/<int:id>')
@login_required
@admin_required
def admin_order_detail(id):
    order = db.session.get(Order, id)
    if not order:
        abort(404)
    return render_template('admin/order_detail.html', order=order)

@app.route('/admin/pedidos/estado/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_order_status(id):
    order = db.session.get(Order, id)
    if order:
        order.status = request.form.get('status', order.status)
        db.session.commit()
        flash('Estado actualizado.', 'success')
    return redirect(url_for('admin_orders'))

@app.route('/admin/blog')
@login_required
@admin_required
def admin_blog():
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).paginate(
        page=page, per_page=app.config['PER_PAGE'], error_out=False)
    return render_template('admin/blog.html', posts=posts)

@app.route('/admin/blog/nuevo', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_blog_new():
    form = BlogForm()
    if form.validate_on_submit():
        post = BlogPost(
            title=form.title.data,
            slug=slugify(form.title.data),
            content=form.content.data,
            excerpt=form.excerpt.data,
            author=form.author.data or 'Perrone\'s INC',
            category=form.category.data,
            tags=form.tags.data,
            published=form.published.data,
            featured=form.featured.data
        )
        if 'image' in request.files:
            img = request.files['image']
            if img.filename:
                post.image = save_image(img, 'blog')
        db.session.add(post)
        db.session.commit()
        flash('Artículo creado.', 'success')
        return redirect(url_for('admin_blog'))
    return render_template('admin/blog_form.html', form=form, title='Nuevo Artículo')

@app.route('/admin/blog/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_blog_edit(id):
    post = db.session.get(BlogPost, id)
    if not post:
        abort(404)
    form = BlogForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.slug = slugify(form.title.data)
        post.content = form.content.data
        post.excerpt = form.excerpt.data
        post.author = form.author.data
        post.category = form.category.data
        post.tags = form.tags.data
        post.published = form.published.data
        post.featured = form.featured.data
        if 'image' in request.files:
            img = request.files['image']
            if img.filename:
                old_img = post.image
                post.image = save_image(img, 'blog')
                if old_img:
                    old_path = os.path.join(app.config['UPLOAD_FOLDER'], old_img)
                    if os.path.exists(old_path):
                        os.remove(old_path)
        db.session.commit()
        flash('Artículo actualizado.', 'success')
        return redirect(url_for('admin_blog'))
    return render_template('admin/blog_form.html', form=form, title='Editar Artículo', post=post)

@app.route('/admin/blog/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_blog_delete(id):
    post = db.session.get(BlogPost, id)
    if post:
        if post.image:
            path = os.path.join(app.config['UPLOAD_FOLDER'], post.image)
            if os.path.exists(path):
                os.remove(path)
        db.session.delete(post)
        db.session.commit()
        flash('Artículo eliminado.', 'success')
    return redirect(url_for('admin_blog'))

@app.route('/admin/mensajes')
@login_required
@admin_required
def admin_messages():
    messages = Contact.query.order_by(Contact.created_at.desc()).all()
    return render_template('admin/messages.html', messages=messages)

@app.route('/admin/mensajes/leer/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_message_read(id):
    msg = db.session.get(Contact, id)
    if msg:
        msg.read = True
        db.session.commit()
    return redirect(url_for('admin_messages'))

@app.route('/admin/categorias')
@login_required
@admin_required
def admin_categories():
    categories = Category.query.all()
    return render_template('admin/categories.html', categories=categories)

@app.route('/admin/categorias/nueva', methods=['POST'])
@login_required
@admin_required
def admin_category_new():
    name = request.form.get('name')
    if name:
        category = Category(
            name=name,
            slug=slugify(name),
            description=request.form.get('description', '')
        )
        if 'image' in request.files:
            img = request.files['image']
            if img.filename:
                category.image = save_image(img, 'products')
        db.session.add(category)
        db.session.commit()
        flash('Categoría creada.', 'success')
    return redirect(url_for('admin_categories'))

@app.route('/admin/categorias/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_required
def admin_category_delete(id):
    category = db.session.get(Category, id)
    if category:
        if category.products:
            flash('No se puede eliminar una categoría con productos.', 'error')
        else:
            db.session.delete(category)
            db.session.commit()
            flash('Categoría eliminada.', 'success')
    return redirect(url_for('admin_categories'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
