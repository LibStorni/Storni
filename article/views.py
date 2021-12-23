from django.db.models          import Q
from django.http.response      import Http404
from django.http               import Http404
from rest_framework.views      import APIView
from rest_framework.response   import Response
from rest_framework.decorators import api_view
from .models                   import Article
from .serializers              import ArticleSerializer


class LatestArticleList(APIView):
    
    def get(self,request,format=None):
        articles   = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

class ArticleDetail(APIView):
    
    def get_object(self,article_slug):
        try:
            return Article.objects.get(slug=article_slug)
        except Article.DoesNotExist:
            raise Http404 
   
    def get(self,request,article_slug,format=None):
        article    = self.get_object(article_slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

@api_view(['POST'])

def search(request):
    query = request.data.get('query','')

    if query:
        articles   = Article.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    else:
        return Response ({"articles":[]})
