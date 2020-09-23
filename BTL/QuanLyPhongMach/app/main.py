from flask import render_template, redirect, request, session, url_for, flash
from flask_login import login_user
from sqlalchemy import or_

from app import app,login
from app.models import *
from app import dao

import hashlib


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login-admin",methods=["get","post"])
def login_admin():
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password","")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                          User.password == password).first()
        if user:
            if user.type ==0:
                login_user(user=user)
            if user.type == 1:
                return render_template("baseuser/List.html")

    return redirect("/admin")


def logout():
    return render_template("Danhsach.html")


@app.route("/home/login")
def home_login():
    return render_template("homeadmin.html")

@app.route("/datlich")
def datlich():
    return render_template("DatLich.html")

@app.route("/thongtin")
def thongtin():
     result = db.session.query(Thuoc).all()
     results = db.session.query(TienKham).all()
     return render_template("about-us.html",tient = result,tienk = results)

@app.route("/home/index")
def home_index():
    return render_template("index.html")

@app.route("/danhsach", methods =['GET', 'POST'],defaults = {"page":1})
@app.route("/danhsach<int:page>",methods =['GET','POST'])
def load_list(page):
    page = page
    pages = 10
    benhnhandangky = Benhnhandangkykham.query.order_by(Benhnhandangkykham.manguoidangky.asc()).paginate(page, pages, error_out=False)
    return render_template("baseuser/Danhsach.html",list = benhnhandangky)


@app.route("/tracuu", methods=['GET', 'POST'],defaults = {"page":1})
@app.route("/tracuu<int:page>", methods=['GET', 'POST'])
def tracuu(page):
    page = page
    pages = 10
    benhnhan = BenhNhan.query.order_by(BenhNhan.mabenhnhan.asc()).paginate(page, pages, error_out=False)
    if request.method == 'POST' and 'keyword' in request.form and 'date' in request.form:
        date = request.form["date"]
        tim = "%{}%".format(date)
        tag = request.form["keyword"]
        search = "%{}%".format(tag)
        benhnhan = BenhNhan.query.filter(BenhNhan.tenbenhnhan.like(search),BenhNhan.ngaykham.like(tim)).paginate(per_page=pages, error_out=False)
    return render_template("baseuser/tracuu.html",benhnhan=benhnhan)


@app.route("/lapphieukham", methods = ['GET','POST'])
def lapphieu():
    if request.method =="POST":
        id = int(request.form.get("id"))
        bn = BenhNhan.query.get(id)
        tc = request.form.get("trieuchung")
        tt = None
        my_data = PhieuKham(bn.mabenhnhan, tt , TienKham.query.get(1).matien)
        db.session.add(my_data)
        db.session.commit()
        for loaibenh in request.form.getlist("loaibenh"):
            b = LoaiBenh.query.get(loaibenh)
            my_dataa = ChiTietPhieuKham(my_data.maphieukham,b.mabenh,tc)
            db.session.add(my_dataa)
            db.session.commit()
        list = dao.read_bn(id)
        thuoc = db.session.query(Thuoc).all()
        pk = dao.read_pk(bn.mabenhnhan)
        return render_template("baseuser/muathuoc.html",bn = list,thuoc = thuoc,pk=pk)
    if request.args.get("id"):
        id = int(request.args.get("id"))
        my_data = Benhnhandangkykham.query.get(id)
        if my_data.status == 0:
            bn = dao.read(id)
            name = bn.tenbenhnhan
            birth = bn.namsinh
            address = bn.diachi
            gender = bn.gioitinh
            phone = bn.sodienthoai
            date = bn.thoigiandenkham

            my_data = BenhNhan(name, birth, address, gender, phone, date)
            db.session.add(my_data)
            db.session.commit()
            my_dataa = Benhnhandangkykham.query.get(id)
            my_dataa.status = 1
            db.session.commit()
            list = dao.read_bn(my_data.mabenhnhan)
            lb = db.session.query(LoaiBenh).all()
    return render_template("baseuser/phieukham.html", bn = list,lb = lb)


@app.route("/themthuoc",methods = ['POST'])
def insertt():
    if request.method =='POST':
        kt = request.form.get("nouse")
        if kt == "0":
            id = int(request.form.get("id"))
            pk = dao.phieukham(id)
        else:
            id = int(request.form.get("id"))
            nguoike = request.form["nguoike"]
            ngayke = None
            my_data = ToaThuoc(ngayke, nguoike)
            db.session.add(my_data)
            db.session.commit()
            pk = dao.phieukham(id)
            pk.id_toathuoc = my_data.matoathuoc
            db.session.commit()
            for thuoc in request.form.getlist("thuoc"):
                t = request.form.get("thuoc")
                sl = "soluong"+t
                soluong = request.form.get(sl)
                t = Thuoc.query.get(thuoc)
                my_dataa = ChiTietToaThuoc(t.mathuoc,my_data.matoathuoc,soluong)
                db.session.add(my_dataa)
                db.session.commit()
    lpk = HoaDon(pk.maphieukham)
    db.session.add(lpk)
    db.session.commit()
    bn = db.session.query(BenhNhan).all()
    return render_template("baseuser/hoadon.html",bn=bn)


@app.route("/dangky", methods = ['POST'])
def insert():

    if request.method == 'POST':
        id = int(request.form["id"])
        name = request.form['name']
        birth = request.form['birth']
        address = request.form['address']
        gender = request.form['gender']
        phone = request.form['phone']
        dateto = request.form['dateto']
        status = None

        kt = int(dao.kiemtra(dateto))
        sl = Soluongbenhnhan.query.get(1)
        if kt <= sl.soluong:
            my_data = Benhnhandangkykham(name, birth, address, gender, phone, dateto, status)
            db.session.add(my_data)
            db.session.commit()

            if id == 1:
                flash("Đăng Ký Khám Thành Công")
                return render_template("Datlich.html")
            if id == 2:
                flash("Thêm Bệnh Nhân Thành Công")
                return redirect(url_for('load_list'))
        else:
            if id == 1:
                flash("Đã đủ số lượng bệnh nhân")
                return render_template("Datlich.html")
            if id == 2:
                flash("Đã đủ số lượng bệnh nhân")
                return redirect(url_for('load_list'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Benhnhandangkykham.query.get(request.form.get('id'))

        my_data.tenbenhnhan = request.form['name']
        my_data.namsinh = request.form['birth']
        my_data.diachi = request.form['address']
        my_data.gioitinh = request.form['gender']
        my_data.sodienthoai = request.form['phone']
        my_data.thoigiandenkham = request.form['dateto']

        db.session.commit()
        flash("Cập Nhật Thành Công")
        return redirect(url_for('load_list'))
    BN = None
    if request.args.get("id"):
        BN = dao.read(id=int(request.args.get("id")))

    return render_template("baseuser/update.html",bn = BN)


@app.route('/updatebn', methods=['GET', 'POST'])
def updatebn():
    if request.method == 'POST':
        my_data = BenhNhan.query.get(request.form.get('id'))

        my_data.tenbenhnhan = request.form['name']
        my_data.namsinh = request.form['birth']
        my_data.diachi = request.form['address']
        my_data.gioitinh = request.form['gender']
        my_data.sodienthoai = request.form['phone']
        my_data.thoigiandenkham = request.form['date']

        db.session.commit()
        flash("Cập Nhật Thành Công")
        return redirect(url_for('tracuu'))
    BN = None
    if request.args.get("id"):
        BN = dao.read_bn(id=int(request.args.get("id")))

    return render_template("baseuser/updatebn.html",bn = BN)

@app.route("/baocao",methods=['GET', 'POST'])
def baocao():
    if request.method == 'POST':
        date = request.form["date"]
        tim = "%{}%".format(date)
        benh = []
        benhnhan = db.session.query(BenhNhan).filter(BenhNhan.ngaykham.like(tim)).group_by(BenhNhan.ngaykham).all()
        for bn in benhnhan:
            benh.insert(0,bn.ngaykham.date())
        return render_template("baseuser/ctbaocao.html", bn=benh)

    return render_template("baseuser/baocao.html")



@app.route("/hoadon")
def hoadon():
    bn = db.session.query(BenhNhan).all()
    return render_template("baseuser/hoadon.html",bn= bn)

@app.route("/chitiet")
def xem():
    id = int(request.args.get("id"))
    pk = dao.phieukham(id)
    if pk.id_toathuoc == None:
        tt = 0
        bn = dao.read_bn(id)
        t = db.session.query(TienKham).all()
        return render_template("baseuser/chitiet.html", bn=bn, tt=tt, tienkham=t)
    else:
        tt = dao.tienthuoc(id)
        bn = dao.read_bn(id)
        t = db.session.query(TienKham).all()
        return render_template("baseuser/chitiet.html",bn=bn,tt=tt,tienkham = t)

@app.route("/chitietbc")
def xembc():
    tient = 0
    dem = 0
    date = request.args.get("id")
    tim = "%{}%".format(date)
    bn = db.session.query(BenhNhan).filter(BenhNhan.ngaykham.like(tim)).all()
    for b in bn:
        pk = dao.phieukham(b.mabenhnhan)
        if pk.id_toathuoc == None:
            tient = tient + 30000
            dem = dem +1
        else:
            dem = dem +1
            tien = dao.tienthuoc(b.mabenhnhan)
            tient = tient + tien

    return  render_template("baseuser/xembc.html",date = date,tient = tient,dem = dem)

@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)

if __name__ =="__main__":
    app.run(debug = True)