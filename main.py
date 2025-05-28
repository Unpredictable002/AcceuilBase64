from google import genai  # Importe la bibliothèque officielle de Google pour interagir avec les modèles Gemini
import os  # Permet d'accéder aux variables d’environnement

GEMINI_KEY = os.getenv("GEMINI_API_KEY")  # Récupère la clé API Gemini stockée dans les variables d’environnement

client = genai.Client(api_key=GEMINI_KEY)  # Initialise le client Gemini avec la clé API pour authentification

response = client.models.generate_content( 
    model="gemini-2.0-flash",  
    contents="Comment vas tu", 
)


