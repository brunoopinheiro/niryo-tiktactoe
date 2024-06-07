# niryo_tic_tac_toe

## Criando o Ambiente:
> **Atenção:** O `pyniryo2` apresenta algumas inconsistências de instalação no Windows, por isso, é recomendado a utilização de um ambiente conda para a execução do projeto. E um processo em 3 etapas para instalação completa.

No powershell, execute o comando:
```powershell
conda env create -f environment.yml
```

Isso vai criar um ambiente base isolado, apenas com as dependências necessárias para rodar o projeto.
Em seguida, ative o ambiente com:

```powershell
conda activate niryo_tic_tac_toe
```
No ambiente conda, instale o pacote do `pyniryo2` com o comando:
```powershell
pip install pyniryo2
```
