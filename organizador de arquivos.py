import shutil
from pathlib import Path

# 1. Entrada de dados limpando aspas e espaços
caminho_entrada = input("Digite o caminho da pasta: ").strip().replace('"', '').replace("'", "")
caminho_pasta = Path(caminho_entrada)

# 2. Dicionário de formatos
formatos = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Executaveis': ['.exe', '.msi'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Videos': ['.mp4', '.mov', '.wmv', '.mkv']
}

def organizar_pasta(diretorio):
    # Verifica se o diretório existe
    if not diretorio.exists() or not diretorio.is_dir():
        print(f"❌ Erro: O caminho '{diretorio}' não é válido.")
        return

    print(f"📂 Organizando: {diretorio}\n")

    # Lista apenas os ARQUIVOS dentro da pasta
    for item in diretorio.iterdir():
        if item.is_file():
            extensao = item.suffix.lower()
            
            for categoria, extensoes_permitidas in formatos.items():
                if extensao in extensoes_permitidas:
                    # Define a pasta de destino (ex: Downloads/Imagens)
                    pasta_destino = diretorio / categoria
                    
                    # Cria a pasta se ela não existir
                    pasta_destino.mkdir(exist_ok=True)
                    
                    # Caminho final do arquivo
                    caminho_final = pasta_destino / item.name
                    
                    try:
                        print(f"✅ Movendo: {item.name} -> {categoria}")
                        shutil.move(str(item), str(caminho_final))
                    except Exception as e:
                        print(f"⚠️ Erro ao mover {item.name}: {e}")

if __name__ == "__main__":
    organizar_pasta(caminho_pasta)
    print("\n Processo concluído!")