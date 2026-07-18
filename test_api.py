#!/usr/bin/env python3
"""Test ultra-simple de l'API Anthropic"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

# Test 1 : essayer de lister les modèles disponibles
print("🔍 Test 1 : Vérifier la clé API")
api_key = os.getenv('ANTHROPIC_API_KEY')
print(f"✅ Clé chargée : {api_key[:20]}..." if api_key else "❌ Pas de clé trouvée")

print("\n🔍 Test 2 : Appel API ultra-simple")
try:
    response = client.messages.create(
        model="claude-3-5-sonnet",
        max_tokens=100,
        messages=[
            {"role": "user", "content": "Dis bonjour en une seule ligne"}
        ]
    )
    print("✅ SUCCESS!")
    print(f"Réponse: {response.content[0].text}")
except Exception as e:
    print(f"❌ Erreur: {type(e).__name__}")
    print(f"Message: {e}")
