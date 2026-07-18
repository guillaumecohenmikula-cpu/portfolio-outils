import os
import json
from dotenv import load_dotenv
import requests

# Charger la clé API depuis .env
load_dotenv()

api_key = os.getenv('OPENROUTER_API_KEY')
api_url = "https://openrouter.ai/api/v1/messages"

def generate_linkedin_content(raw_description: str) -> dict:
    """
    Prend une description brute d'une app/idée et la transforme
    en contenu LinkedIn bien structuré.
    """
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "LinkedIn Content Generator",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": f"""Tu es un expert en communication sur LinkedIn. 
                
Transforme cette description brute en contenu LinkedIn engageant et structuré.
Réponds UNIQUEMENT en JSON valide, avec ces clés exactement:
- "title": Un titre accrocheur (max 100 caractères)
- "hook": Une première ligne qui arrête le scroll (max 150 caractères)
- "body": Le corps du post, 2-3 paragraphes (max 300 caractères)
- "call_to_action": Un appel à l'action clair (max 100 caractères)
- "hashtags": 5 hashtags pertinents

Description brute:
{raw_description}

Réponds UNIQUEMENT le JSON, sans commentaires ni backticks."""
            }
        ]
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code != 200:
        return {"error": f"API Error {response.status_code}: {response.text}"}
    
    response_data = response.json()
    response_text = response_data['content'][0]['text']
    
    # Parser le JSON
    try:
        content = json.loads(response_text)
        return content
    except json.JSONDecodeError as e:
        print(f"Erreur parsing JSON: {e}")
        print(f"Réponse brute: {response_text}")
        return {"error": "Impossible de parser la réponse"}


def main():
    # Exemple d'utilisation
    raw_input = """
    J'ai créé une app qui permet de transformer des process métier Excel 
    en applications web modernes avec l'IA. Ça m'aide à automatiser les 
    tâches répétitives chez Vinci. Fonctionne avec Claude et Supabase.
    """
    
    print("=" * 60)
    print("🚀 Premier appel API Claude via OpenRouter")
    print("=" * 60)
    print(f"\n📝 Description brute:\n{raw_input}\n")
    
    print("⏳ Appel à Claude...")
    result = generate_linkedin_content(raw_input)
    
    if "error" not in result:
        print("\n✅ Contenu généré:\n")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"\n❌ {result['error']}")


if __name__ == "__main__":
    main()
