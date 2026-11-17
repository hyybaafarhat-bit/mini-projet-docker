# Mini-projet Docker

Application web Flask conteneurisée avec Docker.

## Fonctionnalités
- Page d'accueil affichant le nom de l'application et l'environnement
- Route `/health` qui retourne `{"status": "healthy"}`
- Configuration par variables d'environnement : `APP_NAME` et `ENVIRONMENT`

## Prérequis
- Docker
- Git

## Construire l'image
```bash
docker build -t mini-projet-docker:1.0 .
```

## Lancer le conteneur
```bash
docker run -d --name mini-app -p 5002:5000 mini-projet-docker:1.0
```

Avec des variables personnalisées :
```bash
docker run -d --name mini-app-test -p 5003:5000 \
  -e APP_NAME="Mon Projet DevOps" -e ENVIRONMENT="Testing" \
  mini-projet-docker:1.0
```

## Tester
```bash
curl http://localhost:5002
curl http://localhost:5002/health
```

## Image Docker Hub
```bash
docker pull hybafarhat/mini-projet-docker:1.0
```
