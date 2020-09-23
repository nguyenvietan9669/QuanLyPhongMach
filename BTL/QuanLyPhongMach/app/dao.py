from app.models import *
from app import app

def read(id):
    bndk = db.session.query(Benhnhandangkykham).all()
    for p in bndk:
        if p.manguoidangky == id:
            return p

    return None

def read_bn(id):
    bn = db.session.query(BenhNhan).all()
    for p in bn:
        if p.mabenhnhan == id:
            return p

    return None

def read_toathuoc(id):
    thuoc = db.session.query(Thuoc).all()
    idbn =  PhieuKham.query.get(id)
    idtoa = idbn.id_toathuoc

    for p in thuoc:
        if p.chitiets.id_toathuoc == idtoa :
            return p

    return None
def phieukham(id):
    pk = db.session.query(PhieuKham).all()
    for p in pk:
        if p.id_benhnhan == id:
            return p

    return None

def kiemtra(ngay):
    dem = 0
    tim = "%{}%".format(ngay)
    benhnhan = Benhnhandangkykham.query.filter(BenhNhan.tenbenhnhan.like(tim))
    for d in benhnhan:
        d.tenbenhnhan
        dem = dem +1

    return dem

def read_pk(id):
    phieukham = db.session.query(PhieuKham).all()
    for pk in phieukham:
        if pk.id_benhnhan == id:
            return pk
    return None

def read_toathuoc(id):
    toathuoc = db.session.query(ToaThuoc).all()
    for tt in toathuoc:
        if tt.matoathuoc == id:
            return tt

def read_bn(id):
    bn = db.session.query(BenhNhan).all()
    for b in bn:
        if b.mabenhnhan == id:
            return b

def read_chitiet(id):
    chitiet = db.session.query(ChiTietToaThuoc).all()
    for ct in chitiet:
        if ct.id_toathuoc == id:
            return ct

def read_thuoc(id):
    bn = read_bn(id)
    phieukham = read_pk(bn.mabenhnhan)
    tt = read_toathuoc(phieukham.id_toathuoc)
    ct = read_chitiet(tt.matoathuoc)
    thuoc = db.session.query(Thuoc).all()
    for t in thuoc:
        if ct.id_toathuoc == tt.matoathuoc and ct.id_thuoc == t.mathuoc:
            return t

def tienthuoc(id):
    tienthuoc = 0
    bn = read_bn(id)
    phieukham = read_pk(bn.mabenhnhan)
    tt = read_toathuoc(phieukham.id_toathuoc)
    ct = db.session.query(ChiTietToaThuoc).all()
    thuoc = db.session.query(Thuoc).all()
    for c in ct:
        for t in thuoc:
            if c.id_toathuoc == tt.matoathuoc and c.id_thuoc == t.mathuoc:
                 tienthuoc = tienthuoc +(c.soluong * t.gia)
    return tienthuoc



