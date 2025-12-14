import hashlib
import os

def calcular_hash_sha256(caminho_arquivo):
    """
    Calcula o Resumo Digital (Hash SHA-256) de um arquivo compactado.
    Este hash é a 'impressão digital' do seu software para registro no INPI.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"❌ ERRO: Arquivo não encontrado no caminho: {caminho_arquivo}")
        print("Certifique-se de que o arquivo compactado ZIP está no mesmo diretório.")
        return None

    hash_sha256 = hashlib.sha256()

    try:
        # Abre o arquivo em modo binário ('rb') para leitura
        with open(caminho_arquivo, 'rb') as arquivo:
            # Lê o arquivo em blocos (chunks) para lidar eficientemente com arquivos grandes
            while True:
                bloco = arquivo.read(4096)  # Lê 4KB por vez
                if not bloco:
                    break
                hash_sha256.update(bloco)
        
        # Retorna o hash em formato hexadecimal (o código alfanumérico longo)
        return hash_sha256.hexdigest()

    except Exception as e:
        print(f"❌ Ocorreu um erro ao calcular o hash: {e}")
        return None

# --------------------------------------------------------------------------------
# INSTRUÇÕES DE EXECUÇÃO
# --------------------------------------------------------------------------------

# 1. Defina o nome do arquivo que será o objeto do registro (Novo nome para o projeto PGPB).
# Este arquivo ZIP deve conter: prompt_pgpb.py, main_pgpb_analise.py, e o PDF do artigo PGPB.
NOME_ARQUIVO_REGISTRO = "Software_ValidacaoPGPB_v1.0.zip" 

print(f"Preparando para calcular o Hash SHA-256 do arquivo: {NOME_ARQUIVO_REGISTRO}")

# 2. Executa o cálculo
hash_do_registro = calcular_hash_sha256(NOME_ARQUIVO_REGISTRO)

if hash_do_registro:
    print("\n------------------------------------------------------------")
    print("✨ SUCESSO! CÓDIGO HASH SHA-256 PARA REGISTRO NO INPI (PROJETO PGPB) ✨")
    print("------------------------------------------------------------")
    print(f"Arquivo ZIP: {NOME_ARQUIVO_REGISTRO}")
    print(f"HASH SHA-256: {hash_do_registro}")
    print("------------------------------------------------------------")
    print("\n✅ Próxima Ação: Copie este código e insira-o no campo 'Resumo Digital Hash' do Sistema e-Software do INPI.")