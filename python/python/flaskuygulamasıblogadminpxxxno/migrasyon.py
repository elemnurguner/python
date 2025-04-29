from playhouse.migrate import SqliteMigrator, migrate
from models import db  # models.py'den db'yi içe aktarın
from peewee import CharField
# Migrator nesnesi oluştur
migrator = SqliteMigrator(db)

# Yeni sütun ekleme
migrate(
    migrator.add_column('user', 'profile_picture', CharField(null=True))
)