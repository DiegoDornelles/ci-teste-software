# Trabalho N2 – Teste de Software (Python + Pytest)

## Objetivos
Este projeto implementa o **cenário de Faturamento e Pagamentos**, conforme a orientação do professor na disciplina de **Teste de Software**.  
O foco foi aplicar práticas de **TDD**, **mocks/stubs**, **testes parametrizados**, e **integração contínua (CI)** via **GitHub Actions**.

------

## ⚙️ Estrutura do Projeto
ci-teste-software/
├── .github/
│ └── workflows/
│ └── ci.yml # Pipeline de CI (executa pytest e gera cobertura)
│
├── .pytest_cache/ # Cache de execuções do pytest
├── .vscode/ # Configurações locais do VS Code
│
├── python/ # Código-fonte do trabalho N2 (Python + Pytest)
│ ├── src/
│ │ └── fatura.py # Regras de negócio (faturamento e pagamento)
│ │
│ ├── tests/
│ │ └── test_fatura.py # Testes unitários e de integração
│ │
│ ├── requirements.txt # Dependências do projeto (pytest, coverage)
│ └── pytest.ini # Configuração de marcas e opções do pytest
│
├── venv/ # Ambiente virtual (não enviado ao GitHub)
│
├── htmlcov/ # Relatório de cobertura (gerado pelo coverage)
│
├── ci-teste-software.rar # Backup opcional do projeto
└── README.md # Documentação principal do projeto

------

## ⚙️ Execução Local

1. **Ativar o ambiente virtual**
   ```bash
   venv\Scripts\activate
------
Instalar as dependências:
pip install -r python/requirements.txt

------
Executar os testes:
python -m pytest -v

------
Gerar relatório de cobertura:
python -m coverage run -m pytest
python -m coverage html

------
Abrir o relatório no navegador:

start python/htmlcov/index.html