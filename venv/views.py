from re import U, X
from flask import Blueprint, app, config, render_template, request, flash, jsonify
import flask
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.sql.expression import select
from werkzeug.utils import redirect, secure_filename
from .models import *
from .models import Products,HistoryProducts,TransactionProducts,Transactions
from . import db
import os

views = Blueprint('views', __name__,static_folder='static')


@views.route('/', methods=['GET', 'POST'])
def home():
    data = Products.query.all()
    
    for row in data:
        print(row.id, row.barang, row.harga, row.user_id, row.jumlah)    
        
    return render_template("index.html",data=data)


@views.route("/admin")
@login_required
@requires_roles('admin')
def admin():
    return redirect("admin/products")

@views.route('/admin/products', methods=['GET', 'POST'])
@login_required
@requires_roles('admin')
def product_list():
    headings = ("ID", "Nama Barang", "Harga Barang", "Jumlah Barang", "User ID","Gambar Barang")

    data = Products.query.all()

    for row in data:
        print(row.id, row.barang, row.harga, row.user_id, row.jumlah)

    return render_template("admin/products/list.html", data=data,user=current_user,headings=headings)

@views.route('/admin/products/add', methods=['GET', 'POST'])
@login_required
@requires_roles('admin')
def products_add():
    if request.method == 'POST':
        nama_barang = request.form.get('barang')
        harga_barang = request.form.get('harga')
        jumlah_barang = request.form.get('jumlah')
        image = request.files['foto']
        
        if len(nama_barang) == 0:
            flash('Pastikan data terisi dengan benar !', category='error')
        else:
            new_Products = Products(barang=nama_barang,harga=harga_barang, jumlah=jumlah_barang,user_id=current_user.id)
            db.session.add(new_Products)
            db.session.commit()
            tempid = new_Products.id
            fileid = str(new_Products.id)
            flash('Data Ditambahkan added!', category='success')
            image.filename = fileid + ".jpg"
            image.save(os.path.join("venv/", "static/" , "image/", secure_filename(image.filename)))
            new_HistoryProducts = HistoryProducts(id_barang=tempid, id_user=current_user.id, action="Insert")
            db.session.add(new_HistoryProducts)
            db.session.commit()
    return render_template("admin/products/form_add.html")



@views.route('/admin/products/edit', methods=['GET','POST'])
@login_required
@requires_roles('admin')
def products_edit(): 
    id_barang = request.args.get('id')
    

    if (request.method == 'POST'):
        nama_barang = request.form.get('barang')
        harga_barang = request.form.get('harga')
        jumlah_barang = request.form.get('jumlah')
        image = request.files['foto']
        print("Edit berjalan")
        if len(nama_barang) == 0:
            flash('Pastikan data terisi dengan benar !', category='error')
        else:
            new_Products = Products.query.filter_by(id=id_barang).first()
            new_Products.name = nama_barang
            new_Products.price = harga_barang
            new_Products.jumlah = jumlah_barang
            db.session.commit()
            fileid = str(new_Products.id)
            flash('Inventory added!', category='success')
            image.filename = fileid + ".jpg"
            image.save(os.path.join("venv/", "static/" , "image/", secure_filename(image.filename)))
            new_HistoryProducts = HistoryProducts(id_barang=id_barang, id_user=current_user.id, action="Insert")
            db.session.add(new_HistoryProducts)
            db.session.commit()
            return redirect("/admin/products")                    
    return render_template("admin/products/form_edit.html", id_barang=id_barang) 

@views.route('/admin/products/delete', methods=['GET','POST'])
@login_required
@requires_roles('admin')
def products_delete():
    id_barang = request.args.get('id')
    deletepro = Products.query.filter_by(id=id_barang).first()
    db.session.delete(deletepro)
    db.session.commit()
    new_HistoryProducts = HistoryProducts(id_barang=id_barang, id_user=current_user.id, action="Delete")
    db.session.add(new_HistoryProducts)
    db.session.commit()
    return redirect("/admin/products")


#transaksi
@views.route("/admin/transactions")
@login_required
@requires_roles('admin')
def transactions_list():
    
    transactions = Transactions.query.all()

    return render_template("admin/transactions/list.html",data=transactions)

@views.route("/admin/transactions/add", methods=["GET","POST"])
@login_required
@requires_roles('admin')
def transactions_add():
	if request.method == "POST":
		# ambil data dari form html
		products = request.form.getlist("products")
		products_qty = request.form.getlist("products_qty")

		# buat transacsi utamanya
		transactions = Transactions()
		db.session.add(transactions)
		# flush terlebih dahulu untuk mencegah transaksi apabila gagal
		db.session.flush()

		# loop product
		for i, product in enumerate(products):
			transactions_products = TransactionProducts()
			transactions_products.transaction_id = transactions.id
			transactions_products.product_id = int(product)
			transactions_products.product_qty = int(products_qty[i])
			db.session.add(transactions_products)
			db.session.flush()

		# commit semua transaksi
		db.session.commit()
	return render_template("admin/transactions/form_add.html")






    


