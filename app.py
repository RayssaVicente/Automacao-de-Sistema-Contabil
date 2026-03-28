from playwright.sync_api import sync_playwright
from openpyxl import *
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        accept_downloads=True,
        locale="pt-BR",
    )
    page = context.new_page()
    page.set_default_timeout(30000) # 30s para ações/waits
    page.set_default_navigation_timeout(60000) # 60s para navegações
    # Navegar até o site
    page.goto('https://simulacontabil.netlify.app',wait_until='domcontentloaded')
    # Realizar o login
    page.get_by_role('textbox',name='Email').click()
    page.get_by_role('textbox',name='Email').fill('admin@simulacontabil.com.br')
    
    page.get_by_role('textbox',name='Senha').click()
    page.get_by_role('textbox',name='Senha').fill('admin')
    
    page.get_by_role('button',name='Entrar').click()
    
    # Clicar em lançamentos
    page.get_by_role('link',name='Lançamentos').click()
    # Carregar planilha
    planilha = load_workbook('lancamentos.xlsx')
    # Acessar página de lançamentos
    pagina_lancamentos = planilha['Lançamentos']
    # Passar por cada linha dentro da minha planilha
    for linha in pagina_lancamentos.iter_rows(min_row=2,values_only=True):
        descricao = linha[0]
        valor = str(linha[1])
        data = linha[2]
        tipo = linha[3]
        categoria = linha[4]
        status = linha[5]
        
        # Clicar em novo lançamento
        page.get_by_role('button',name='Novo Lançamento').click()
        # Preencher Descrição
        page.get_by_test_id("input-description").click()
        page.get_by_test_id("input-description").fill(descricao)
        # Preencher Valor
        page.get_by_test_id("input-amount").click()
        page.get_by_test_id("input-amount").fill(valor)
        # Preencher Data
        page.get_by_test_id("input-date").click()
        page.get_by_test_id("input-date").fill(data)
        # Preencher Tipo
        if tipo == 'Receita':
            page.get_by_test_id("select-type").select_option("RECEITA")
        else:
            page.get_by_test_id("select-type").select_option("DESPESA")
        
        # Preencher Categoria
        page.get_by_test_id("select-category").select_option(categoria)
        # Preencher Status
        page.locator("div").filter(has_text=re.compile(r"^StatusPendentePagoAtrasado$")).get_by_role("combobox").select_option(status.upper())
        # Clicar em salvar
        page.get_by_test_id("btn-save").click()
        page.wait_for_timeout(2000)
    
    # Ler os dados da planilha e Realizar os lançamentos, um por um
    
    input('Digite ENTER para encerrar a automação')
    browser.close()