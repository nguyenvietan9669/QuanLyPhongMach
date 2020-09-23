from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey,Boolean,Date
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin ,current_user,logout_user
from flask import redirect
from app import db, admin


class User(db.Model,UserMixin):
    __tablename__="user"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    active = Column(Boolean,default=True)
    username = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)
    type = Column(Integer,nullable=False)

    def __str__(self):
        return self.name

class Soluongbenhnhan(db.Model):
    __tablename__="soluongbenhnhan"
    id = Column(Integer,primary_key=True,autoincrement=True)
    soluong = Column(Integer,default=40)

    def __str__(self):
        return self.name

class BenhNhan(db.Model):

    __tablename__ = "benhnhan"

    mabenhnhan = Column(Integer,primary_key= True,autoincrement=True)
    tenbenhnhan = Column(String(50), nullable=True)
    namsinh = Column(Date,nullable=False)
    diachi = Column(String(100),nullable=False)
    gioitinh = Column(String(10),nullable=False)
    sodienthoai = Column(Integer,nullable=True)
    ngaykham = Column(DateTime(timezone=True), default=datetime.utcnow)
    phieukhams = relationship('PhieuKham',backref='benhnhan',lazy = True)

    def __init__(self, tenbenhnhan, namsinh, diachi, gioitinh, sodienthoai, ngaykham):
        self.tenbenhnhan = tenbenhnhan
        self.namsinh = namsinh
        self.diachi = diachi
        self.gioitinh = gioitinh
        self.sodienthoai = sodienthoai
        self.ngaykham = ngaykham

    def __str__(self):
        return self.name


class Benhnhandangkykham(db.Model):

    __tablename__ = "benhnhandangkykham"

    manguoidangky = Column(Integer,primary_key= True,autoincrement=True)
    tenbenhnhan = Column(String(50), nullable=False)
    namsinh = Column(Date, nullable=False)
    diachi = Column(String(100), nullable=False)
    gioitinh = Column(String(10), nullable=False)
    sodienthoai = Column(Integer, nullable=True)
    thoigiandenkham = Column(Date, nullable=False)
    status = Column(Integer,default=0)

    def __init__(self,tenbenhnhan,namsinh,diachi,gioitinh,sodienthoai,thoigiandenkham,status):
        self.tenbenhnhan = tenbenhnhan
        self.namsinh = namsinh
        self.diachi = diachi
        self.gioitinh = gioitinh
        self.sodienthoai = sodienthoai
        self.thoigiandenkham = thoigiandenkham
        self.status = status

class TienKham(db.Model):
    __tablename__ = "tienkham"

    matien = Column(Integer, primary_key=True, autoincrement=True)
    sotien = Column(Float,default=0)
    phieukhams = relationship('PhieuKham', backref='tienkham', lazy=True)


    def __str__(self):
        return self.name


class LoaiBenh(db.Model):

    __tablename__ = "loaibenh"

    mabenh = Column(Integer, primary_key=True, autoincrement=True)
    tenloaibenh = Column(String(50),nullable=False)
    chitiets = relationship('ChiTietPhieuKham',backref = 'loaibenh',lazy = True)

    def __str__(self):
        return self.name


class ToaThuoc(db.Model):

    __tablename__ = "toathuoc"

    matoathuoc = Column(Integer, primary_key=True, autoincrement=True)
    ngayketoa = Column(DateTime(timezone=True), default=datetime.utcnow)
    nguoiketoa = Column(String(100),nullable=False)
    phieukhams = relationship('PhieuKham',backref='toathuoc',lazy = True)
    chitiets = relationship('ChiTietToaThuoc',backref='toathuoc',lazy = True)

    def __init__(self, ngayketoa, nguoiketoa):
        self.ngayketoa = ngayketoa
        self.nguoiketoa = nguoiketoa

    def __str__(self):
        return self.name


class PhieuKham(db.Model):

    __tablename__ = "phieukham"

    maphieukham = Column(Integer,primary_key= True,autoincrement=True)
    id_benhnhan = Column(Integer, ForeignKey(BenhNhan.mabenhnhan),primary_key=True,)
    id_toathuoc = Column(Integer, ForeignKey(ToaThuoc.matoathuoc),nullable=True)
    id_tien = Column(Integer,ForeignKey(TienKham.matien),nullable=False)
    hoadons = relationship('HoaDon',backref='phieukham',lazy = True)
    chitiets= relationship('ChiTietPhieuKham',backref = 'phieukham',lazy =True)

    def __init__(self,id_benhnhan,id_toathuoc,id_tien):
        self.id_benhnhan = id_benhnhan
        self.id_toathuoc = id_toathuoc
        self.id_tien = id_tien



class HoaDon(db.Model):

    __tablename__ = "hoadon"

    mahoadon = Column(Integer,primary_key=True,autoincrement=True)
    id_phieukham = Column(Integer,ForeignKey(PhieuKham.maphieukham),nullable=False)

    def __init__(self,id_phieukham,):
        self.id_phieukham = id_phieukham

    def __str__(self):
        return self.name


class DonVi(db.Model):

    __tablename__ = "donvi"

    madonvi = Column(Integer, primary_key=True, autoincrement=True)
    tendonvi = Column(String(50),nullable=False)
    thuocs = relationship('Thuoc',backref='donvi', lazy=True)


class CachDung(db.Model):

    __tablename__ = "cachdung"

    macachdung = Column(Integer, primary_key=True, autoincrement=True)
    cachdung = Column(String(100),nullable=False)
    thuocs = relationship('Thuoc',backref ='cachdung',lazy=True)


class Thuoc(db.Model):

    __tablename__ = "thuoc"

    mathuoc = Column(Integer, primary_key=True, autoincrement=True)
    tenthuoc = Column(String(100),nullable=False)
    gia = Column(Float,default=0)
    id_cachdung = Column(Integer,ForeignKey(CachDung.macachdung),nullable=False)
    id_donvi = Column(Integer,ForeignKey(DonVi.madonvi),nullable=False)
    chitiets = relationship('ChiTietToaThuoc',backref='thuoc',lazy = True)


class ChiTietToaThuoc(db.Model):

    __tablename__ = "chitiettoathuoc"

    id_thuoc = Column(Integer,ForeignKey(Thuoc.mathuoc),primary_key=True)
    id_toathuoc = Column(Integer,ForeignKey(ToaThuoc.matoathuoc),primary_key=True)
    soluong = Column(Integer,nullable=False)

    def __init__(self,id_thuoc,id_toathuoc,soluong):
        self.id_thuoc = id_thuoc
        self.id_toathuoc = id_toathuoc
        self.soluong = soluong

    def __str__(self):
        return self.name


class ChiTietPhieuKham(db.Model):

    __tablename__ = "chitietphieukham"

    id_phieukham = Column(Integer,ForeignKey(PhieuKham.maphieukham),primary_key=True)
    id_loaibenh = Column(Integer,ForeignKey(LoaiBenh.mabenh),primary_key=True)
    trieuchung = Column(String(255),nullable=True)

    def __init__(self,id_phieukham,id_loaibenh,trieuchung):
        self.id_phieukham = id_phieukham
        self.id_loaibenh = id_loaibenh
        self.trieuchung = trieuchung

    def __str__(self):
        return self.name


class Logout(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


class BenhNhanModelView(ModelView):
    column_display_pk = True
    can_delete = True
    can_edit = True
    can_export = True
    can_create = True

    def is_accessible(self):
        return current_user.is_authenticated


class LoaiBenhModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = True

    def is_accessible(self):
        return current_user.is_authenticated

class SoLuongModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = False

    def is_accessible(self):
        return current_user.is_authenticated


class ThuocModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class DonviModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = True

    def is_accessible(self):
        return current_user.is_authenticated


class CachDungModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = True

    def is_accessible(self):
        return current_user.is_authenticated


class TienKhamModelView(ModelView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_delete = True

    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(BenhNhanModelView(BenhNhan,db.session))
admin.add_view(LoaiBenhModelView(LoaiBenh,db.session))
admin.add_view(ThuocModelView(Thuoc,db.session))
admin.add_view(DonviModelView(DonVi,db.session))
admin.add_view(SoLuongModelView(Soluongbenhnhan,db.session))
admin.add_view(CachDungModelView(CachDung,db.session))
admin.add_view(TienKhamModelView(TienKham,db.session))
admin.add_view(Logout(name="Đăng Xuất"))


if __name__ =='__main__':
    db.create_all()