from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.user_name}>'

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.JSON, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class PedidoProducto(db.Model):
    __tablename__ = 'pedido_productos'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    sucursal_id = db.Column(db.String(50), nullable=False)
    productos = db.relationship('PedidoProducto', backref='pedido', lazy=True)
    fecha = db.Column(db.DateTime, nullable=False)

class Despacho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(70), unique=True)
    proceso = db.Column(db.String(100))
        
    def __init__(self, producto, proceso):
        self.producto = producto
        self.proceso = proceso
