from rest_framework   import serializers
from .models          import Article



class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Article
        fields = (

            "id",
            "title",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
        ) 
      
