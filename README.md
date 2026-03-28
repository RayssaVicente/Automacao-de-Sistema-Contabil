# 🤖 Automação de Lançamentos - Simula Contábil

Este projeto é um script de automação desenvolvido em **Python** utilizando a biblioteca **Playwright**. O objetivo é ler dados financeiros de uma planilha Excel (`.xlsx`) e realizar o cadastro automático de lançamentos em um sistema de simulação contábil.

---

## 🚀 Funcionalidades

* **Login Automático:** Realiza o acesso ao sistema com credenciais pré-configuradas.
* **Integração com Excel:** Utiliza a biblioteca `openpyxl` para ler dados de lançamentos (Descrição, Valor, Data, Tipo, Categoria e Status).
* **Preenchimento Dinâmico:** Identifica campos via `data-testid` e Roles, garantindo maior precisão na automação.
* **Tratamento de Condicionais:** Diferencia automaticamente entre lançamentos do tipo "Receita" e "Despesa".

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Playwright:** Para automação de navegador (Chromium).
* **Openpyxl:** Para manipulação e leitura de arquivos Excel.
* **Regex (re):** Para localização precisa de elementos de interface.

---

## 📋 Pré-requisitos

Antes de rodar o projeto, você precisará ter o Python instalado e as seguintes bibliotecas:

1.  **Instale as dependências:**
    ```bash
    pip install playwright openpyxl
    ```

2.  **Instale os navegadores do Playwright:**
    ```bash
    playwright install chromium
    ```

---

## 📂 Estrutura da Planilha (`lancamentos.xlsx`)

O script espera um arquivo Excel na raiz do projeto com o nome `lancamentos.xlsx` e uma aba chamada **Lançamentos**. A estrutura deve ser:

| Descrição | Valor | Data | Tipo | Categoria | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Exemplo Item | 150.00 | 20/10/2023 | Receita | Vendas | Pago |

---

## ▶️ Como Usar

1.  Clone este repositório ou baixe o script.
2.  Certifique-se de que o arquivo `lancamentos.xlsx` está na mesma pasta do script.
3.  Execute o script:
    ```bash
    python nome_do_seu_arquivo.py
    ```
4.  O navegador abrirá no modo visível (`headless=False`) para que você acompanhe o processo.
5.  Ao finalizar, o terminal solicitará um **ENTER** para encerrar a sessão do navegador.

---

## ⚠️ Observações Técnicas

* **Timeouts:** O script possui um tempo de espera padrão de 30s para ações e 60s para navegação.
* **Viewport:** A janela do navegador é iniciada na resolução **1920x1080**.
* **Localidade:** Configurado para `pt-BR`.

---
Desenvolvido para fins de estudo e automação de processos contábeis.
