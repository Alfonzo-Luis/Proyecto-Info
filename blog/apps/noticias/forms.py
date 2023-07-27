from django import forms
from .models import Noticia, Comment

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria_noticia']

# CREAR COMENTARIOS
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] #campos de mi formulario
        exclude = ['author']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.author = user.username
