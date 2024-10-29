import os
import json
import boto3
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class BedrockClient:
    def __init__(self):
        self.client = boto3.client(
            service_name='bedrock-runtime',
            region_name=os.getenv('AWS_DEFAULT_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

    def generate_text(self, prompt, model_id="anthropic.claude-v2", max_tokens=1000):
        """
        Genera texto usando Amazon Bedrock
        
        :param prompt: El prompt para generar texto
        :param model_id: ID del modelo a usar
        :param max_tokens: Número máximo de tokens en la respuesta
        :return: Texto generado
        """
        try:
            body = json.dumps({
                "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
                "max_tokens_to_sample": max_tokens,
                "temperature": 0.7,
                "top_p": 1,
            })

            response = self.client.invoke_model(
                modelId=model_id,
                body=body
            )

            response_body = json.loads(response.get('body').read())
            return response_body.get('completion')

        except Exception as e:
            print(f"Error al generar texto: {str(e)}")
            return None

    def generate_seo_metadata(self, url, keyword):
        """
        Genera metadatos SEO usando Amazon Bedrock
        
        :param url: URL del sitio
        :param keyword: Palabra clave principal
        :return: Diccionario con los metadatos generados
        """
        prompt = f"""
        Genera metadatos SEO optimizados para:
        URL: {url}
        Palabra clave: {keyword}
        
        Por favor, proporciona:
        1. Un meta título optimizado (máximo 60 caracteres)
        2. Una meta descripción optimizada (máximo 155 caracteres)
        3. Un H1 optimizado (máximo 95 caracteres)
        
        Formato deseado:
        Meta título: [título]
        Meta descripción: [descripción]
        H1: [h1]
        """

        response = self.generate_text(prompt)
        if not response:
            return None

        # Procesar la respuesta para extraer los metadatos
        try:
            lines = response.split('\n')
            metadata = {}
            
            for line in lines:
                if line.startswith('Meta título:'):
                    metadata['meta_title'] = line.replace('Meta título:', '').strip()
                elif line.startswith('Meta descripción:'):
                    metadata['meta_description'] = line.replace('Meta descripción:', '').strip()
                elif line.startswith('H1:'):
                    metadata['h1'] = line.replace('H1:', '').strip()
            
            return metadata
        except Exception as e:
            print(f"Error al procesar la respuesta: {str(e)}")
            return None