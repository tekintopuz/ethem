Tek yapman gereken mysqlde 'ethem' isimli bir user oluşturup 'ethem1234' şifresi vermen bir
de 'ethem' isimli bir database oluşturman ve ethem kullanıcısına tam yetki vermen

sonrasınada virtualenv oluşrurmak
dev.env yi .env olarak çevirmek
python -m venv venv

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic

