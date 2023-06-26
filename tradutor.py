from google.cloud import translate

def traduzir_texto(texto, destino='en'):
    client = translate.TranslationServiceClient()

    projeto_id = 'seu-projeto-id'
    localizacao = 'global'

    parent = f"projects/{projeto_id}/locations/{localizacao}"
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [texto],
            "target_language_code": destino,
            "mime_type": "text/plain",
        }
    )

    traducao = response.translations[0].translated_text
    return traducao

# Exemplo de uso
texto_original = 'Olá, como você está?'
texto_traduzido = traduzir_texto(texto_original, destino='en')

print(f'Texto original: {texto_original}')
print(f'Texto traduzido: {texto_traduzido}')
