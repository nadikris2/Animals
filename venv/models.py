from sqlalchemy.sql.expression import true
from . import db
from flask_login import UserMixin,current_user
from functools import wraps
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import event
from werkzeug.security import generate_password_hash


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barang = db.Column(db.String(45), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    jumlah = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class HistoryProducts(db.Model):
    __tablename__ = "historyproducts"
    id = db.Column(db.Integer, primary_key=True)
    id_barang = db.Column(db.Integer, db.ForeignKey('products.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(150))




class TransactionProducts(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	transaction_id = db.Column(db.Integer, db.ForeignKey("transactions.id"), nullable=False)
	product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
	product_qty = db.Column(db.Integer, nullable=False)
	transaction = relationship("Transactions", backref="transaction_products")
	product = relationship("Products", backref="transaction_products")

@event.listens_for(db.session,"before_flush")
def reduce_stock_product(*args):
	sess = args[0]
	for obj in sess.new:
		if not isinstance(obj, TransactionProducts):
			continue
		product = Products.query.filter_by(id=obj.product_id).first()

		product.jumlah = product.jumlah - obj.product_qty
		db.session.add(product)

class Transactions(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	create_on = db.Column(db.DateTime, nullable=False)
	def __init__(self):
		self.create_on = datetime.now()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default ='0')
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(64), default='customer')

    def __repr__(self) -> str:
        return '<User %s>' % self.username

def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                # Redirect the user to an unauthorized notice!
                return "You are not authorized to access this page"
            return f(*args, **kwargs)
        return wrapped
    return wrapper

