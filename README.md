# organizador-arquivos-python
# Organizador de Arquivos Automático 📁

Este projeto é um script em Python desenvolvido para organizar pastas bagunçadas, movendo arquivos para pastas específicas baseadas em suas extensões (PDF, Imagens, Vídeos, etc).

## 🚀 Tecnologias Utilizadas
*   **Python 3**
*   **Pathlib**: Para manipulação inteligente de caminhos de diretórios.
*   **Shutil**: Para a movimentação física dos arquivos no sistema.

## 🧠 Conceitos Aplicados
Durante o desenvolvimento deste projeto, apliquei conceitos fundamentais de programação:
*   **Dicionários**: Para mapear extensões às suas respectivas pastas.
*   **Loops (For)**: Para percorrer arquivos e listas de formatos.
*   **Tratamento de Erros (Try/Except)**: Para garantir que o programa não trave caso um arquivo esteja em uso.
*   **Criação Dinâmica de Pastas**: Uso do `mkdir(exist_ok=True)` para evitar erros de duplicidade.

## 🛠️ Como usar
1. Execute o script.
2. Cole o caminho da pasta que deseja organizar.
3. O script criará as pastas automaticamente e moverá os arquivos.
