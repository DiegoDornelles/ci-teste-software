<<<<<<< HEAD
# Trabalho N2 — Teste de Software (Python + Pytest)

## Objetivos

Este projeto implementa o **Cenário de Faturamento e Pagamentos**, conforme o enunciado do Trabalho N2.  
O foco foi aplicar práticas de **TDD**, uso de **mocks/stubs**, **testes parametrizados**, **ciclo de vida**, e **pipeline de CI (GitHub Actions)** com **relatório de cobertura** automatizado.

---

## Estrutura do Projeto

=======
# 🧪 Trabalho N2 — Teste de Software (Python + Pytest)

## 🎯 Objetivos

Este projeto implementa o **Cenário de Faturamento e Pagamentos**, conforme o enunciado do Trabalho N2.  
O foco foi aplicar práticas de **TDD**, uso de **mocks/stubs**, **testes parametrizados**, **ciclo de vida com fixtures**, e **pipeline de CI (GitHub Actions)** com **relatório de cobertura** automatizado.

---

## 🧱 Estrutura do Projeto

>>>>>>> 94e7dba (Atualiza README principal)
ci-teste-software/
├──
.github/
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

---

## ⚙️ Execução Local

1. **Ativar o ambiente virtual**
   ```bash
   venv\Scripts\activate
Instalar as dependências

bash
Copiar código
pip install -r python/requirements.txt
Executar os testes

bash
Copiar código
python -m pytest -v
Gerar relatório de cobertura

bash
Copiar código
python -m coverage run -m pytest
python -m coverage html
Abrir o relatório no navegador

bash
Copiar código
start python/htmlcov/index.html