from peewee import *

# SQLite veritabanı bağlantısı
db = SqliteDatabase('myblog.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    profile_picture = CharField(null=True)  # Profil resmi dosya yolu

class Post(BaseModel):
    title = CharField()
    content = TextField()
    author = ForeignKeyField(User, backref='posts')
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

# Veritabanı tablolarını oluştur
def create_tables():
    with db:
        db.create_tables([User, Post])

# Veritabanı bağlantısını başlat
def initialize_db():
    db.connect()
    create_tables()