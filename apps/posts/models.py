from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome


class Postagem(models.Model):
    titulo = models.CharField('Título', max_length=150)
    noticia = models.TextField('Notícia')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField('Imagem', upload_to='imagens', blank=True, null=True)
    criada_em = models.DateTimeField('Criada em', auto_now_add=True)
    atualizada_em = models.DateTimeField('Atualizada em', auto_now=True)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
    
    def __str__(self):
        return self.titulo
