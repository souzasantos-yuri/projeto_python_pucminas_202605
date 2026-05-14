# Projeto Python — PUC Minas

Projeto desenvolvido para estudos de Engenharia de Dados e análise de dados utilizando Python, Pandas e Jupyter Notebook.

---

# 📌 Objetivo

Este projeto tem como objetivo realizar:

- processamento de dados;
- análise exploratória;
- validação de dados;
- geração de métricas e KPIs;
- visualizações com Matplotlib;
- organização de pipelines de dados.

---

# 🛠️ Tecnologias Utilizadas

- Python 3.12+
- Pandas
- Matplotlib
- Jupyter Notebook
- UV
- PyArrow

---

# 📁 Estrutura do Projeto

```text
.
├── data/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── processed/
│
├── notebooks/
│   └── analise.ipynb
│
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── utils/
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🚀 Como Executar o Projeto

## 1. Clone o repositório

```bash
git clone https://github.com/souzasantos-yuri/projeto_python_pucminas_202605.git
```

Entre na pasta:

```bash
cd projeto_python_pucminas_202605
```

---

# 2. Instale o UV

Caso não tenha instalado:

## Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Documentação oficial:

https://docs.astral.sh/uv/

---

# 3. Criar ambiente virtual

```bash
uv venv
```

Ative o ambiente virtual.

## Linux / macOS

```bash
source .venv/bin/activate
```

## Windows

```powershell
.venv\Scripts\activate
```

---

# 4. Instalar dependências

```bash
uv sync
```

Isso irá instalar todas as dependências definidas no `pyproject.toml`.

---

# 5. Executar o Jupyter Notebook

```bash
uv run jupyter notebook
```

ou

```bash
uv run jupyter lab
```

---

# 📊 Principais Análises

O projeto contém análises sobre:

- correlação entre grid e resultado final;
- taxa de vitória por posição de largada;
- evolução histórica da Fórmula 1;
- equipes e pilotos dominantes;
- análise exploratória de temporadas.

---

# ✅ Boas Práticas Aplicadas

- organização em camadas (`bronze/silver/gold`);
- tratamento de dados;
- validação de qualidade;
- separação entre EDA e transformação;
- uso de funções reutilizáveis;
- versionamento com Git.
