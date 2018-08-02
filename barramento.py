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

# Importar numpy e pandas
import numpy as np
import pandas as pd

## Ler arquivo .tsv
df = pd.read_table('https://raw.githubusercontent.com/harndt93/data/master/pedidos_barramento.tsv', sep=';')

df2 = pd.read_table('https://raw.githubusercontent.com/harndt93/data/master/pedidos_barramento.tsv', sep=';')

## Remover colunas definitivamente
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

## Alterar nome das colunas
df.columns = ['Operacao', 'Empresa', 'Pedido_Cliente', 'Pedido_Jund', 'Integracao', 'Status', 'Data' ]

## Tratar coluna status
df['Status'] = df['Status'].map({1: 'Em Fila', 4: 'Sucesso', 5: 'Insucesso', 10: 'Duplicidade'})

## Imprimir tabela
df

## Gerar arquivo .xlsx
df.to_excel('pedidos_barramento.xlsx', sheet_name='Sheet1')