# -*- coding: utf-8 -*-

#
# mainprodutos is responsable for managing the Product information in the GUI
#

import re
from functools import partial

from PyQt5.QtCore import Qt, QByteArray, QUrl, QBuffer
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView

from Views.janelaProdutos import Ui_ct_MainProdutos
from Views.formularioProdutos import Ui_ct_FormProdutos
from Crud.CrudProduto import CrudProduto
from Crud.CrudCategoriaProduto import CrudCategoriaProduto
from Crud.CrudMarcaProduto import CrudMarcaProduto

class MainProdutos(Ui_ct_MainProdutos, Ui_ct_FormProdutos):

    # funcao junta GUI e dados para janela de Produtos
    def mainprodutos(self, frame):
        super(MainProdutos, self).setMainProdutos(frame)
        self.frameMainProdutos.show()

        # Icone Botao busca Janela
        self.IconeBotaoMenu(self.bt_BuscaProdutos,
                            self.resourcepath('Images/iconSearch.png'))
        # Campo Busca
        self.tx_BuscaProdutos.textEdited.connect(self.ListarProduto)
        # Botao Adicionar Produto
        self.bt_AddNovoProdutos.clicked.connect(self.FormProdutos)

        # Desabilitando Signals tabela
        self.tb_Produtos.blockSignals(True)
        # define tamanho colunas tabela
        self.tb_Produtos.setColumnHidden(0, True)
        self.tb_Produtos.setColumnWidth(1, 50)
        self.tb_Produtos.setColumnWidth(2, 250)
        self.tb_Produtos.setColumnWidth(3, 150)
        self.tb_Produtos.setColumnWidth(4, 100)
        self.tb_Produtos.setColumnWidth(5, 150)
        self.tb_Produtos.setColumnWidth(6, 150)
        self.tb_Produtos.setColumnWidth(7, 50)
        # Populando tabela produtos
        self.ListarProduto()

    # Dados Tabela Produto
    def ListarProduto(self):
        lista = CrudProduto()
        # se o texto ta vazio vai buscar tudo
        lista.produto = self.tx_BuscaProdutos.text()
        lista.listaProduto()

        while self.tb_Produtos.rowCount() > 0:
            self.tb_Produtos.removeRow(0)

        i = 0
        # lista.produto vira array apos select
        if len(lista.produto) >= 1:
            while i < len(lista.produto):
                self.tb_Produtos.insertRow(i)
                self.alinharDadosTabela(self.tb_Produtos, i, 0, str(lista.id[i]))
                self.SetTabelaID(self.tb_Produtos, i, 1, lista.id[i])
                self.SetFormataDadosPessoaisTabela(self.tb_Produtos, i, 2,
                                        lista.produto[i],
                                        lista.descricao[i])
                self.SetFormataDadosPessoaisTabela(self.tb_Produtos, i, 3,
                                        lista.categoria[i],
                                        lista.marca[i])
                self.SetTabelaStatusEstoque(self.tb_Produtos, i, 4,
                                        str(lista.qtdEstoque[i]),
                                        self.GetCorStatusEstoque(lista.qtdEstoque[i], lista.qtdMinimoEstoque[i]))
                self.SetValorTable(self.tb_Produtos, i, 5, lista.valorUnitario[i])
                self.SetValorTable(self.tb_Produtos, i, 6, lista.totalEstoque[i])
                # click edit
                self.botaoTabela(self.tb_Produtos, i, 7,
                                partial(self.DetalhamentoProduto, lista.id[i]), "#7AB32E")
                i += 1

    """Drilldown Produto por ID"""
    def DetalhamentoProduto(self, valor):
        id = valor
        self.FormProdutos()
        self.tx_idProduto.setText(str(id))

        busca = CrudProduto()
        busca.id = id
        busca.DetalhamentoProdutoId()

        if hasattr(busca, 'imagem') and busca.imagem:
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray.fromBase64(busca.imagem))
            self.lb_FotoProduto.setPixmap(pixmap.scaledToWidth(200, Qt.TransformationMode(Qt.FastTransformation)))
            self.bt_AdicionarImagem.setHidden(True)
            self.bt_DeletarImagem.setVisible(True)
        self.tx_NomeProduto.setText(busca.produto)
        self.tx_Descricao.setText(busca.descricao)
        self.cb_Categoria.setCurrentIndex(self.cb_Categoria.findData(busca.categoria))
        self.cb_Marca.setCurrentIndex(self.cb_Marca.findData(busca.marca))
        self.tx_QtdMinimoEstoque.setText(str(busca.qtdMinimoEstoque))
        self.tx_QtdEstoque.setText(str(busca.qtdEstoque))
        self.tx_ValorUnitario.setText(str(busca.valorUnitario))
        self.tx_TotalEstoque.setText(str(busca.totalEstoque))

    """Frame Formulário Produto"""
    def FormProdutos(self):
        self.DesativaBotaoProdutos()
        self.LimpaFrame(self.ct_containerProdutos)
        super(MainProdutos, self).setFormProdutos(self.ct_containerProdutos)
        self.fr_FormProdutos.show()
        # Oculta alguns Campos
        self.bt_DeletarImagem.setHidden(True)
        # Checando se existe ID válido
        self.IdCheckProduto()
        # Icone Botoes
        self.IconeBotaoMenu(self.bt_BuscaProdutos, self.resourcepath('Images/iconSearch.png'))
        self.IconeBotaoMenu(self.bt_AdicionarImagem, self.resourcepath('Images/edit-add.png'))
        self.IconeBotaoMenu(self.bt_DeletarImagem, self.resourcepath('Images/edit-delete.png'))
        self.bt_codigoBarra.setPixmap(QPixmap(self.resourcepath('Images/CodBarra.png')))

        # Validar campos int
        validarInt = QIntValidator(0, 999, self)
        # Validar campos float
        validarValorFloat = QDoubleValidator(0.50, 999.99, 2, self)
        validarValorFloat.setNotation(QDoubleValidator.StandardNotation)
        validarValorFloat.setDecimals(2)

        self.tx_QtdMinimoEstoque.setValidator(validarInt)
        self.tx_QtdEstoque.setValidator(validarInt)
        self.tx_ValorUnitario.setValidator(validarValorFloat)

        # Botao Adicionar e Remover Imagem
        self.bt_AdicionarImagem.clicked.connect(self.UploadImagem)
        self.bt_DeletarImagem.clicked.connect(self.DeleteImagem)
        # Botao Add Categoria e populando combobox e check
        self.ListaCategoria()
        self.cb_Categoria.currentIndexChanged.connect(self.ListaMarca)
        # Calculo valor em estoque
        self.tx_QtdEstoque.textEdited.connect(self.AtualizarTotalEstoque)
        self.tx_ValorUnitario.textEdited.connect(self.AtualizarTotalEstoque)
        # acoes
        self.bt_Voltar.clicked.connect(self.janelaProdutos)
        self.bt_Salvar.clicked.connect(self.ValidarDadosProduto)

    # checando campo Id se é Edicao ou Novo Produto
    def IdCheckProduto(self):
        if not self.tx_idProduto.text():
            busca = CrudProduto()
            self.tx_idProduto.setText(str(busca.lastIdProduto()))

    # Verificando Inputs
    def ValidarDadosProduto(self):
        if not self.tx_NomeProduto.text():
            self.tx_NomeProduto.setFocus()
        elif self.cb_Categoria.currentIndex() == 0:
            self.cb_Categoria.setFocus()
        elif self.cb_Marca.currentIndex() == 0:
            self.cb_Marca.setFocus()
        elif not self.tx_QtdMinimoEstoque.text():
            self.tx_QtdMinimoEstoque.setFocus()
        elif not self.tx_QtdEstoque.text():
            self.tx_QtdEstoque.setFocus()
        elif not self.tx_ValorUnitario.text():
            self.tx_ValorUnitario.setFocus()
        else:
            self.CadastraProdutoDB()

    # Cadastro Produto
    def CadastraProdutoDB(self):
        INSERIR = CrudProduto()
        INSERIR.id = self.tx_idProduto.text()
        INSERIR.produto = self.tx_NomeProduto.text().upper()
        INSERIR.descricao = self.tx_Descricao.text().upper()
        # converts image for base64 to save in DB
        if self.lb_FotoProduto.pixmap():
            imagem = QPixmap(self.lb_FotoProduto.pixmap())
            data = QByteArray()
            buf = QBuffer(data)
            imagem.save(buf, 'PNG')
            INSERIR.imagem = str(data.toBase64()).encode('utf8')[2:-1]
        else:
            INSERIR.imagem = False
        INSERIR.categoria = self.cb_Categoria.currentData()
        INSERIR.marca = self.cb_Marca.currentData()
        INSERIR.qtdMinimoEstoque = self.tx_QtdMinimoEstoque.text()
        INSERIR.qtdEstoque = self.tx_QtdEstoque.text()
        INSERIR.valorUnitario = self.tx_ValorUnitario.text().replace(",", ".")
        INSERIR.addProduto()
        self.janelaProdutos()

    def DesativaBotaoProdutos(self):
        self.bt_AddNovoProdutos.setEnabled(False)
        self.tx_BuscaProdutos.setEnabled(False)
        self.bt_BuscaProdutos.setEnabled(False)

    def AtivaBotaoProdutos(self):
        self.bt_AddNovoProdutos.setEnabled(True)
        self.tx_BuscaProdutos.setEnabled(True)
        self.bt_BuscaProdutos.setEnabled(True)

    def UploadImagem(self):
        Dialog = QFileDialog()
        Dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        filename = Dialog.getOpenFileName(self, "Selecionar Imagem", "", "Image files (*.jpg *.png)")[0]

        self.lb_FotoProduto.setPixmap(QPixmap(filename).scaledToWidth(
            200, Qt.TransformationMode(Qt.FastTransformation)))
        self.bt_AdicionarImagem.setHidden(True)
        self.bt_DeletarImagem.setVisible(True)

    def DeleteImagem(self):
        self.lb_FotoProduto.clear()
        self.bt_DeletarImagem.setHidden(True)
        self.bt_AdicionarImagem.setVisible(True)

    # Lista combobox categoria
    def ListaCategoria(self):
        busca = CrudCategoriaProduto()
        busca.listaCategoriaProduto()
        for categoria in busca.query:
            self.cb_Categoria.addItem(
                categoria.categoria_produto, str(categoria.id))

    # Listando marca por categoria
    def ListaMarca(self, index):
        self.cb_Marca.clear()
        self.cb_Marca.addItem("SELECIONE")
        lista = CrudMarcaProduto()

        if self.cb_Categoria.count() > 0:
            id = self.cb_Categoria.currentData()
            lista.id = id
        lista.ListaMarcaProdutos()

        for marca in lista.query:
            self.cb_Marca.addItem(marca.marca_produto, str(marca.id))

    # atualizar valor total estoque
    def AtualizarTotalEstoque(self):
        if not self.tx_QtdEstoque.text():
            return
        if not self.tx_ValorUnitario.text():
            return
        total = int(self.tx_QtdEstoque.text()) * float(self.tx_ValorUnitario.text())
        self.tx_TotalEstoque.setText(str(total))

