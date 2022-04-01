from django.shortcuts import render, redirect
from .models import User, Tag, Article
import uuid
from .forms import ArticleForm, LoginForm, RegisterForm, ProfileForm
# Create your views here.


def home(request):  # 暂时是选择展示所有人的文章(之后会设置成为展示支持者最多的文章)
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'BlogSystem/home.html', context)


def profile(request, pk=''):
    if pk != '':
        user = User.objects.get(id=uuid.UUID(pk))
        articles = Article.objects.filter(user=user)
        context = {'user': user, 'articles': articles}
        return render(request, 'BlogSystem/profile.html', context)
    elif 'id' in request.session:  # 只有处于登录状态的时候
        id = request.session['id']
        user = User.objects.get(id=uuid.UUID(id))
        articles = Article.objects.filter(user=user)
        context = {'user': user, 'articles': articles}
        return render(request, 'BlogSystem/profile.html', context)
    return redirect('login')


def editprofile(request, pk):
    user = User.objects.get(id=uuid.UUID(pk))
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=user
        )
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'BlogSystem/editprofile.html', {'form': form})


def post(request):
    form = ArticleForm()
    if 'id' not in request.session:
        return redirect('login')
    elif request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = uuid.UUID(request.session['id'])
            form.save()
            request.session['article_id'] = str(Article.objects.last().id)
            return redirect('article',request.session['article_id'])
    return render(request, 'BlogSystem/post.html', {'form': form})


def article(request, pk=''):
    if pk == '':
        user = User.objects.get(id=uuid.UUID(request.session.get('id')))
        article = Article.objects.get(
            id=uuid.UUID(request.session.get('article_id')))
        context = {'user': user, 'article': article}
        return render(request, 'BlogSystem/article.html', context)
    else:
        article = Article.objects.get(id=uuid.UUID(pk))
        user = article.user
        context = {'user': user, 'article': article}
        return render(request, 'BlogSystem/article.html', context)


def editarticle(request, pk):
    article = Article.objects.get(id=uuid.UUID(pk))
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(
            request.POST,
            request.FILES,
            instance=article
        )
        if form.is_valid():
            form.save()
            return redirect('article', pk)
    return render(request, 'BlogSystem/editarticle.html', {'form': form})


def deletearticle(request, pk):
    article = Article.objects.get(id=uuid.UUID(pk))
    article.delete()
    return redirect('profile')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                name=form.cleaned_data['name'],
                password=form.cleaned_data['password1']
            )
            user.save()
            request.session['id'] = str(user.id)
            return redirect('profile')
    return render(request, 'BlogSystem/register.html', {'form': form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid() and User.objects.get(
                name=form.cleaned_data['name'],
                password=form.cleaned_data['password']) is not None:
            user = User.objects.get(
                name=form.cleaned_data['name'],
                password=form.cleaned_data['password'])
            request.session['id'] = str(user.id)
            return redirect('profile')
    elif 'id' in request.session:  # 密码自动填充
        user = User.objects.get(id=uuid.UUID(request.session['id']))
        form = LoginForm(instance=user)
    return render(request, 'BlogSystem/login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect('login')
