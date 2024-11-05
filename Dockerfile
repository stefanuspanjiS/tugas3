# Gunakan image Python
FROM python:3.10

# Set Working Directory
WORKDIR /app

# requirements.txt dan install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# menyalin semua file ke dalam container
COPY . .

# Perintah untuk menjalankan server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
