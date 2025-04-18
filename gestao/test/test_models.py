from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Categoria, Departamento, Fornecedor, Bem, Movimentacao
from django.urls import reverse
from datetime import date

class ModelTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.departamento = Departamento.objects.create(nome="TI")
        self.fornecedor = Fornecedor.objects.create(nome="Tech Supplier", contato="1234-5678")
        self.user = User.objects.create_user(username="testuser", password="password")
        self.bem = Bem.objects.create(
            nome="Notebook Dell",
            categoria=self.categoria,
            departamento=self.departamento,
            fornecedor=self.fornecedor,
            data_aquisicao=date.today(),
            status='Em uso',
            usuario_responsavel=self.user,
            valor=5000.00
        )
        self.movimentacao = Movimentacao.objects.create(
            bem=self.bem,
            destino=self.departamento,
            descricao="Movido para suporte técnico"
        )
    
    def test_categoria_str(self):
        self.assertEqual(str(self.categoria), "Eletrônicos")
    
    def test_departamento_str(self):
        self.assertEqual(str(self.departamento), "TI")
    
    def test_fornecedor_str(self):
        self.assertEqual(str(self.fornecedor), "Tech Supplier")
    
    def test_bem_str(self):
        self.assertEqual(str(self.bem), "Notebook Dell")
    
    def test_movimentacao_str(self):
        self.assertIn("Notebook Dell", str(self.movimentacao))
