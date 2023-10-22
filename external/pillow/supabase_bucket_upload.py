from os import environ as env
from sys import argv
from io import BytesIO
import supabase
from limit_image_dimensions_and_convert_to_JPEG import redimensionar_imagem
from datetime import datetime

def main():
    if len(argv) < 2:
        print("Informe o caminho para uma imagem JPEG ou PNG.")
        return
    imagem = argv[1]
    img = redimensionar_imagem(
        imagem=imagem, largura_maxima=1366, altura_maxima=768)

    img_as_bytes = BytesIO()
    img.save(img_as_bytes, format='JPEG')

    with open(".env", "r") as env_file:
        for line in env_file:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                env[key] = value

    client = supabase.create_client(
            env.get("SUPABASE_URL"), env.get("SUPABASE_API_KEY"))
    f = img_as_bytes.getvalue()

    now = datetime.now()
    data_hora_string = now.strftime("%Y-%m-%d %H:%M:%S.%f").replace(" ", "_")
    nome_arquivo = f"animal_{data_hora_string}.jpeg"
    res = client.storage.from_(
        env.get("SUPABASE_IMAGES_BUCKET_NAME")).upload(
            file=f, path=nome_arquivo, file_options={"content-type": "image/jpeg"})

if __name__ == '__main__':
    main()
