# Djangoのショートカット関数をインポート（テンプレートをレンダリングするため）
from django.shortcuts import render  

# Djangoのtimezoneをインポート（現在の時間を取得するため）
from django.utils import timezone  

# Postモデルをインポート（ブログの記事データを扱う）
from .models import Post  

from django.shortcuts import render, get_object_or_404

# 記事一覧を表示するビュー関数
def post_list(request):  
    # 現在時刻より前に公開された記事を取得し、公開日順に並べる
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  
    
    # 'blog/post_list.html' のテンプレートをレンダリングし、postsのデータを渡す
    return render(request, 'blog/post_list.html', {'posts': posts})  

#投稿の詳細を表示するビュー関数
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})