from django.db          import models
from io                 import BytesIO
from PIL                import Image
from django.core.files  import File



class Article(models.Model):

    title       = models.CharField(max_length=200)
    slug        = models.SlugField()
    description = models.CharField(max_length=200)
    price       = models.IntegerField(default=1)
    image       = models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail   = models.ImageField(upload_to='uploads/',blank=True,null=True)
    date        = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'

    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self,image, size=(300,200)):

        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io= BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail = File(thumb_io, name=image.title)

        return thumbnail





