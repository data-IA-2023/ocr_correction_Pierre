# ocr_correction_Pierre


OCR_API
VISION_KEY
VISION_ENDPOINT
DATABASE_URL=sqlite:///ocr.sqlite
DISCORD_WEBHOOK_URL

Création d’un environnement virtuel : python3 -m venv .venv
Appliquer un environnement : source .venv/bin/activate
Lancer fast API : uvicorn (nom de l’appli):app --reload --port 8000


Lancer docker : docker run -p 3000:3000 -e MYVAR=XXX --name ocr_co
rrection_pierre ocr_correction_pierre