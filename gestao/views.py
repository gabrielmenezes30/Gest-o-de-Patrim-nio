from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Bem, Categoria, Departamento, Fornecedor, Movimentacao
from .forms import CategoriaForm, DepartamentoForm, FornecedorForm, BemForm, MovimentacaoForm
from django.db.models import Count, Sum
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm

@login_required
def home(request):
    query = request.GET.get('q', '')  # Obtém o termo de busca digitado
    bens = Bem.objects.all()

    if query:
        bens = bens.filter(nome__icontains=query)  # Filtra os bens pelo nome

    total_bens = bens.count()  # Total de bens cadastrados
    categorias = Categoria.objects.count()  # Total de categorias
    manutencao = bens.filter(status='Manutenção').count()  # Bens em manutenção
    
    # Distribuição dos bens por categoria
    categoria_distribuicao = Categoria.objects.annotate(total_bens=Count('bem')).all()
    
    # Movimentações recentes
    movimentacoes_recent = Movimentacao.objects.order_by('-data')[:5]  # Últimas 5 movimentações

    # Valor total do patrimônio (assumindo que há um campo `valor` na model `Bem`)
    valor_total = bens.aggregate(total=Sum('valor'))['total'] or 0  # Somando os valores dos bens

    return render(request, 'home.html', {
        'bens': bens,
        'total_bens': total_bens,
        'categorias': categorias,
        'manutencao': manutencao,
        'categoria_distribuicao': categoria_distribuicao,
        'movimentacoes_recent': movimentacoes_recent,
        'valor_total': valor_total,
        'query': query,  # Enviando a query para o template
    })

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


#CREATE

@login_required
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list/categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'form/categoria_form.html', {'form': form})


@login_required
def departamento_create(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DepartamentoForm()
    return render(request, 'form/departamento_form.html', {'form': form})


@login_required
def fornecedor_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list/fornecedor_list')
    else:
        form = FornecedorForm()
    return render(request, 'form/fornecedor_form.html', {'form': form})


@login_required
def bem_create(request):
    if request.method == 'POST':
        form = BemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BemForm()
    return render(request, 'form/bem_form.html', {'form': form})


@login_required
def movimentacao_create(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovimentacaoForm()
    return render(request, 'form/movimentacao_form.html', {'form': form})


#LIST

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'list/categoria_list.html', {'categorias': categorias})

def departamento_list(request):
    departamentos = Departamento.objects.all()
    return render(request, 'list/departamento_list.html', {'departamentos': departamentos})

def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'list/fornecedor_list.html', {'fornecedores': fornecedores})

def bem_list(request):
    bens = Bem.objects.all()
    return render(request, 'list/bem_list.html', {'bens': bens})

def movimentacao_list(request):
    movimentacoes = Movimentacao.objects.all()
    return render(request, 'list/movimentacao_list.html', {'movimentacoes': movimentacoes})

#DETAIL
def categoria_detail(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, 'detail/categoria_detail.html', {'categoria': categoria})

def departamento_detail(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    return render(request, 'detail/departamento_detail.html', {'departamento': departamento})

def fornecedor_detail(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    return render(request, 'detail/fornecedor_detail.html', {'fornecedor': fornecedor})

def bem_detail(request, id):
    bem = get_object_or_404(Bem, id=id)
    return render(request, 'detail/bem_detail.html', {'bem': bem})

def movimentacao_detail(request, id):
    movimentacao = get_object_or_404(Movimentacao, id=id)
    return render(request, 'detail/movimentacao_detail.html', {'movimentacao': movimentacao})

#EDIT
def bem_edit(request, id):
    bem = get_object_or_404(Bem, id=id)

    if request.method == 'POST':
        form = BemForm(request.POST, instance=bem)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BemForm(instance=bem)

    return render(request, 'form/bem_form.html', {'form': form})