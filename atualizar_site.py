import os
from git import Repo

# Caminho da pasta local no seu computador (Google Drive)
PATH_DIR = r"K:\Meu Drive\Marketing\Site\due-diligence"

def fazer_deploy_automatico():
    try:
        # Abre o repositório git local
        repo = Repo(PATH_DIR)
        
        # Verifica se há modificações pendentes
        if not repo.is_dirty(untracked_files=True):
            print("Nenhuma alteração nova detectada na pasta.")
            return

        print("Alterações detectadas. Adicionando arquivos...")
        repo.git.add(A=True)

        # Realiza o commit automático
        mensagem_commit = "Atualizacao automatica do formulario de Due Diligence via script Python"
        repo.index.commit(mensagem_commit)
        print(f"Commit realizado com sucesso: '{mensagem_commit}'")

        # Faz o push explicitamente para a branch main do origin
        origin = repo.remotes.origin
        print("Enviando atualizações para o GitHub...")
        origin.push(refspec='main:main')
        print("Push realizado com sucesso para o GitHub! O Vercel atualizará o site em instantes.")

    except Exception as e:
        print(f"Erro ao realizar o processo de commit e push: {e}")

if __name__ == "__main__":
    fazer_deploy_automatico()