from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

import webbrowser


class Relatorios:
    def printCliente(self):
        webbrowser.open("cliente.pdf")

    def gerarRelatorioCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRelatorio = self.en_codigo.get()
        self.nomeRelatorio = self.en_nome.get()
        self.telefoneRelatorio = self.en_telefone.get()
        self.cidadeRelatorio = self.en_cidade.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Cliente")

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, "Código: ")
        self.c.drawString(50, 670, "Nome: ")
        self.c.drawString(50, 640, "Telefone: ")
        self.c.drawString(50, 610, "Cidade: ")

        self.c.setFont("Helvetica", 18)
        self.c.drawString(140, 700, self.codigoRelatorio)
        self.c.drawString(140, 670, self.nomeRelatorio)
        self.c.drawString(140, 640, self.telefoneRelatorio)
        self.c.drawString(140, 610, self.cidadeRelatorio)

        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printCliente()
