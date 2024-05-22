from djongo import models


# modelo del genero de las peliculas  
class Genero(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=50,unique=True)
    
    def __str__(self)->str:
        return self.nombre


# modelo de las peliculas
class Pelicula(models.Model):
    _id = models.ObjectIdField()
    codigo = models.CharField(max_length=9)
    titulo = models.CharField(max_length=50)
    protagonista = models.CharField(max_length=50)
    duracion = models.IntegerField()
    resumen = models.CharField(max_length=2000)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    
    def __str__(self)->str:
        return self.titulo