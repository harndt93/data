# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:41:11 2018

@author: Harndt
"""

# =============================================================================
# #%% DEFINES BLOCKS OF CODE
# import numpy as np # math library
# import scipy # scientific library
# import pylab as pl # plotting library
# #%% this will output some wisdom
# print('Python and Calcium Imaging, a marriage made in heaven')
# #%% this creates a random vector
# a = np.random.random([10,10])
# print(a)
# #%% this will plot something
# pl.imshow(a)
# =============================================================================

# Import numpy and pandas
import numpy as np
import pandas as pd

## Read orders and costumers .tsv files
df = pd.read_table('https://raw.githubusercontent.com/harndt93/data/master/pedidos_barramento.tsv', sep=';')
df2 = pd.read_table('https://raw.githubusercontent.com/harndt93/data/master/clientes_barramento.tsv', sep=';')

## Remove 39 columns from orders .tsv file
df.drop('idFilaPedido', axis=1, inplace=True)
df.drop('idCabecPedido', axis=1, inplace=True)
df.drop('idFilaCliente', axis=1, inplace=True)
df.drop('idWebService', axis=1, inplace=True)
df.drop('respostaJundEnderecoEntrega', axis=1, inplace=True)
df.drop('respostaJundItensPedido', axis=1, inplace=True)
df.drop('respostaJundPedidoSerial', axis=1, inplace=True)
df.drop('respostaJundConfirmaPagtoPedido', axis=1, inplace=True)
df.drop('respostaJundRastreamentoPedido', axis=1, inplace=True)
df.drop('dataHoraProcessadoPedido', axis=1, inplace=True)
df.drop('dataHoraProcessadoPedidoSerial', axis=1, inplace=True)
df.drop('dataHoraProcessadoConfirmaPagtoPedido', axis=1, inplace=True)
df.drop('ultimaDataHoraRastreamentoPedido', axis=1, inplace=True)
df.drop('rastreamentoFinalizado', axis=1, inplace=True)
df.drop('importacaoImeiFinalizada', axis=1, inplace=True)
df.drop('respostaServiceAtualizacaoPedidoERP', axis=1, inplace=True)
df.drop('subId', axis=1, inplace=True)
df.drop('ultimoStatusRastreamentoPedidoOI', axis=1, inplace=True)
df.drop('statusSiteIntegracaoAtualizado', axis=1, inplace=True)
df.drop('reprocessarPedido', axis=1, inplace=True)
df.drop('ultimoStatusResumidoRastreamentoPedidoOI', axis=1, inplace=True)
df.drop('engenhariaReversa', axis=1, inplace=True)
df.drop('pedidoJundDesmembrado', axis=1, inplace=True)
df.drop('duplicidadeValidada', axis=1, inplace=True)
df.drop('respostaJundCliente', axis=1, inplace=True)
df.drop('tipoPagamento', axis=1, inplace=True)
df.drop('dadosPedidoGravado', axis=1, inplace=True)
df.drop('importacaoOcorrenciaFinalizada', axis=1, inplace=True)
df.drop('pedidoJundDesmembradoJaImportado', axis=1, inplace=True)
df.drop('informacoesValidadas', axis=1, inplace=True)
df.drop('pedidoLiberadoParaRastreamento', axis=1, inplace=True)
df.drop('pedidoJundDesmembradoEncontrado', axis=1, inplace=True)
df.drop('idModoIntegracao', axis=1, inplace=True)
df.drop('pedidoOiIntegradoSite', axis=1, inplace=True)
df.drop('chaveUnica', axis=1, inplace=True)
df.drop('idLojaAntigo', axis=1, inplace=True)
df.drop('pedidoCancelado', axis=1, inplace=True)
df.drop('notaFiscal', axis=1, inplace=True)

## Remove 10 columns from costumers .tsv file
df2.drop('idFilaCliente', axis=1, inplace=True)
df2.drop('idWebService', axis=1, inplace=True)
df2.drop('idCliente', axis=1, inplace=True)
df2.drop('dataHoraProcessadoCliente', axis=1, inplace=True)
df2.drop('bandeira', axis=1, inplace=True)
df2.drop('tipoPessoa', axis=1, inplace=True)
df2.drop('dadosClienteGravado', axis=1, inplace=True)
df2.drop('informacoesValidadas', axis=1, inplace=True)
df2.drop('idModoIntegracao', axis=1, inplace=True)
df2.drop('pedidoCliente', axis=1, inplace=True)

## Alter orders columns names
df.columns = ['Operacao', 'Empresa', 'Pedido_Cliente', 'Pedido_Jund', 'Integracao', 'Status', 'Data' ]

## Alter costumers columns names
df2.columns = ['Operacao', 'Empresa', 'Cliente', 'Integracao', 'Status', 'Data']

## Replace int values into string in Status column in orders
df['Status'] = df['Status'].map({1: 'Em Fila', 4: 'Sucesso', 5: 'Insucesso', 10: 'Duplicidade'})

## Replace int values into string in Status column in costumers
df['Status'] = df['Status'].map({7: 'Em Fila', 2: 'Sucesso', 5: 'Insucesso', 6: 'Duplicidade'})

## Replace int values into string in Operacao column in orders
df['Operacao'] = df['Operacao'].map({1: 'Claudio', 2: 'RSA', 3: 'LOJA CLARO', 4: 'VIRTUALZAP', 5: 'OI ECOMMERCE', 6: 'LOJA SAMSUNG VIP',
7: 'ASSURANT', 8: 'WISEUP', 9: 'SAMSUNG VIP', 10: 'PORTAL OI - FRANQUIA', 11: 'PORTAL OI - VAREJO', 12: 'PORTLA OI - LOJAS PROPRIAS',
13: 'LOJA CLARO', 14: 'LG INSIDERS', 15: 'STEFANINI', 16: 'B2W', 17: 'LOJA TIM', 18: 'CNOVA', 19: 'MERCADO LIVRE', 20: 'OI OMNI',
21: 'PRC', 22: 'VIVO-MKT', 23: 'B2C-ACESS', 24: 'SIS', 25: 'TOKIO MARINE', 26: 'COMPRA FACILITADA', 27: 'INDEFINIDA', 28: 'SALESFORCE',
29: 'LOJA PEDIDOS VIVO', 30: 'PONTO NET', 31: 'MERCADO LIVRE - CLARO LOJA', 32: 'MERCADO LIVRE - INCREMENT', 33: 'GO PRO',
34: 'ZOOM', 35: 'BUSCAPE', 36: 'ZURICH', 37: 'EZCONET', 38: 'BRADESCO SHOPFACIL', 39: 'RICARDO ELETRO', 40: 'LG ONLINE', 41: 'NEXTEL',
42: 'AMAZON', 43: 'CARREFOUR', 44: 'MAGAZINE LUIZA', 45: 'MOBCOM B2W', 46: 'MOBCOM CNOVA', 47: 'MOBCOM MERCADO LIVRE',
48: 'MOBCOM MELI 1', 49: 'MOBCOM MELI 2', 50: 'MARISA', 51: 'LOJA MULTI LOJA', 52: 'LOJA MARISA', 53: 'LOJA FOTO NASCIMENTO'})

## Replace int values into string in Operacao column in costumers
df2['Operacao'] = df2['Operacao'].map({1: 'Claudio', 2: 'RSA', 3: 'LOJA CLARO', 4: 'VIRTUALZAP', 5: 'OI ECOMMERCE', 6: 'LOJA SAMSUNG VIP',
7: 'ASSURANT', 8: 'WISEUP', 9: 'SAMSUNG VIP', 10: 'PORTAL OI - FRANQUIA', 11: 'PORTAL OI - VAREJO', 12: 'PORTLA OI - LOJAS PROPRIAS',
13: 'LOJA CLARO', 14: 'LG INSIDERS', 15: 'STEFANINI', 16: 'B2W', 17: 'LOJA TIM', 18: 'CNOVA', 19: 'MERCADO LIVRE', 20: 'OI OMNI',
21: 'PRC', 22: 'VIVO-MKT', 23: 'B2C-ACESS', 24: 'SIS', 25: 'TOKIO MARINE', 26: 'COMPRA FACILITADA', 27: 'INDEFINIDA', 28: 'SALESFORCE',
29: 'LOJA PEDIDOS VIVO', 30: 'PONTO NET', 31: 'MERCADO LIVRE - CLARO LOJA', 32: 'MERCADO LIVRE - INCREMENT', 33: 'GO PRO',
34: 'ZOOM', 35: 'BUSCAPE', 36: 'ZURICH', 37: 'EZCONET', 38: 'BRADESCO SHOPFACIL', 39: 'RICARDO ELETRO', 40: 'LG ONLINE', 41: 'NEXTEL',
42: 'AMAZON', 43: 'CARREFOUR', 44: 'MAGAZINE LUIZA', 45: 'MOBCOM B2W', 46: 'MOBCOM CNOVA', 47: 'MOBCOM MERCADO LIVRE',
48: 'MOBCOM MELI 1', 49: 'MOBCOM MELI 2', 50: 'MARISA', 51: 'LOJA MULTI LOJA', 52: 'LOJA MARISA', 53: 'LOJA FOTO NASCIMENTO'})

## Print table
df
df2

## Generate .xlsx file based on the readed file
df.to_excel('pedidos_barramento.xlsx', sheet_name='Orders')
#df2.to_excel('pedidos_barramento.xlsx', sheet_name='Costumers')
