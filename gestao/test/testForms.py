from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import CategoriaForm, DepartamentoForm, FornecedorForm, BemForm, MovimentacaoForm
from django.urls import reverse
from datetime import date


class FormTestCase(TestCase):
    def test_categoria_form_valid(self):
        form = CategoriaForm(data={'nome': 'Veículos'})
        self.assertTrue(form.is_valid())
    
    def test_departamento_form_valid(self):
        form = DepartamentoForm(data={'nome': 'Financeiro'})
        self.assertTrue(form.is_valid())
    
    def test_fornecedor_form_valid(self):
        form = FornecedorForm(data={'nome': 'Fornecedora X', 'contato': '9999-9999'})
        self.assertTrue(form.is_valid())
    
    def test_bem_form_invalid(self):
        form = BemForm(data={})  # Dados vazios
        self.assertFalse(form.is_valid())
    