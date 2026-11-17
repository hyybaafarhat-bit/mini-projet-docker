# Image de base Python
FROM python:3.12-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

# Définir les variables d'environnement
ENV APP_NAME="Mon application Docker"
ENV ENVIRONMENT="Production"

# Exposer le port 5000
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
