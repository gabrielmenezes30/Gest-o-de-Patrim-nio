from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from gestao.models import Categoria, Departamento, Fornecedor, Bem, Movimentacao
from gestao.forms import CategoriaForm
from datetime import date

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.categoria = Categoria.objects.create(nome='Eletrônicos')
        self.departamento = Departamento.objects.create(nome='TI')
        self.fornecedor = Fornecedor.objects.create(nome='Tech Supplier', contato='12345678')
        self.bem = Bem.objects.create(
            nome='Notebook',
            categoria=self.categoria,
            departamento=self.departamento,
            fornecedor=self.fornecedor,
            data_aquisicao=date.today(),
            status='Em uso',
            usuario_responsavel=self.user,
            valor=5000.00
        )
        
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_categoria_create_view(self):
        response = self.client.post(reverse('categoria_create'), {'nome': 'Móveis'})
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertEqual(Categoria.objects.count(), 2)

    def test_categoria_list_view(self):
        response = self.client.get(reverse('categoria_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list/categoria_list.html')

    def test_bem_create_view(self):
        response = self.client.post(reverse('bem_create'), {
            'nome': 'Monitor',
            'categoria': self.categoria.id,
            'departamento': self.departamento.id,
            'fornecedor': self.fornecedor.id,
            'data_aquisicao': date.today(),
            'status': 'Em uso',
            'usuario_responsavel': self.user.id,
            'valor': 1200.00
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Bem.objects.count(), 2)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)  # Redireciona após login

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redireciona para login

    def test_movimentacao_create_view(self):
        response = self.client.post(reverse('movimentacao_create'), {
            'bem': self.bem.id,
            'destino': self.departamento.id,
            'descricao': 'Transferido para suporte'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Movimentacao.objects.count(), 1)

    def test_bem_edit_view(self):
        response = self.client.post(reverse('bem_editar', args=[self.bem.id]), {
            'nome': 'Notebook Dell',
            'categoria': self.categoria.id,
            'departamento': self.departamento.id,
            'fornecedor': self.fornecedor.id,
            'data_aquisicao': date.today(),
            'status': 'Manutenção',
            'usuario_responsavel': self.user.id,
            'valor': 5500.00
        })
        self.assertEqual(response.status_code, 302)
        self.bem.refresh_from_db()
        self.assertEqual(self.bem.nome, 'Notebook Dell')
        self.assertEqual(self.bem.status, 'Manutenção')