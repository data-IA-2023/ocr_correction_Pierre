# ocr_correction_Pierre

Création d’un environnement virtuel : python3 -m venv .venv
Appliquer un environnement : source .venv/bin/activate
Lancer fast API : uvicorn (nom de l’appli):app --reload --port 8000


VARIABLES D'ENVIRONNEMENT
OCR_API
VISION_KEY
VISION_ENDPOINT
DATABASE_URL=sqlite:///ocr.sqlite
DISCORD_WEBHOOK_URL

Docker
docker build -t ocr-correction-pierre .
docker rm ocr-correction-
docker run -p 3000:3000 -e MYVAR=XXX --name ocr-correction-pierre ocr-correction-pierre

Dans Azure:
docker login regocrpierre.azurecr.io
docker tag ocr-correction-pierre regocrpierre.azurecr.io/ocr-correction-pierre
docker push regocrpierre.azurecr.io/ocr-correction-pierre