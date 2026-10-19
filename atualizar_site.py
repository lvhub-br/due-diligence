try:
    from git import Repo
    from git.exc import InvalidGitRepositoryError, NoSuchPathError
except ImportError:  # pragma: no cover - mensagem amigável se GitPython não estiver instalado
    raise SystemExit(
        "Dependência ausente: 'GitPython' não está instalado.\n"
        "Instale com: pip install GitPython"
    )

# Caminho da pasta local no seu computador (Google Drive)
PATH_DIR = r"K:\Meu Drive\Marketing\Site\due-diligence"


def fazer_deploy_automatico():
    try:
        # Abre o repositório git local
        try:
            repo = Repo(PATH_DIR)
        except NoSuchPathError:
            print(f"Erro: o caminho não existe: {PATH_DIR}")
            return
        except InvalidGitRepositoryError:
            print(
                f"Erro: '{PATH_DIR}' não é um repositório git.\n"
                "Dica: rode 'git init', adicione o remote com "
                "'git remote add origin <url>' e faça o primeiro commit/push."
            )
            return

        # Verifica se há modificações pendentes
        if not repo.is_dirty(untracked_files=True):
            print("Nenhuma alteração nova detectada na pasta.")
            return

        print("Alterações detectadas. Adicionando arquivos...")
        repo.git.add(A=True)

        # Realiza o commit automático
        mensagem_commit = "Atualização automática do formulário de Due Diligence via script Python"
        repo.index.commit(mensagem_commit)
        print(f"Commit realizado com sucesso: '{mensagem_commit}'")

        # Faz o push para o GitHub (origin main)
        if not repo.remotes or not hasattr(repo.remotes, "origin"):
            print(
                "Commit feito localmente, mas nenhum remote 'origin' foi configurado.\n"
                "Configure com: git remote add origin <url-do-github>"
            )
            return
        origin = repo.remotes.origin
        origin.push()
        print("Push realizado com sucesso para o GitHub! O Vercel atualizará o site em instantes.")

    except Exception as e:
        print(f"Erro ao realizar o processo de commit e push: {e}")


if __name__ == "__main__":
    fazer_deploy_automatico()
