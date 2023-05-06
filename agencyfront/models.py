from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    creation_date = models.DateField(auto_now_add=True)


class Property(models.Model):
    DEPARTMENTS = [
        ('Amazona', 'Amazona'),
        ('Antioquia', 'Antioquia'),
        ('Arauca', 'Arauca'),
        ('Atlántico', 'Atlántico'),
        ('Bolívar', 'Bolívar'),
        ('Boyacá', 'Boyacá'),
        ('Caldas', 'Caldas'),
        ('Caquetá', 'Caquetá'),
        ('Casanare', 'Casanare'),
        ('Cauca','Cauca'),
        ('Cesar','Cesar'),
        ('Chocó','Chocó'),
        ('Córdoba', 'Córdoba'),
        ('Cundinamarca', 'Cundinamarca'),
        ('Guainía', 'Guainía'),
         ('Guaviare', 'Guaviare'),
        ('Huila', 'Huila'),
        ('La_Guajira', 'La_Guajira'),
        ('Magdalena', 'Magdalena'),
        ('Meta', 'Meta'),
        ('Nariño', 'Nariño'),
        ('Norte_de_Santander', 'Norte_de_Santander'),
        ('Putumayo', 'Putumayo'),
        ('Quindío', 'Quindío'),
        ('Risaralda', 'Risaralda'),
        ('San_Andrés', 'San_Andrés'),
        ('Santander', 'Santander'),
        ('Sucre', 'Sucre'),
        ('Tolima', 'Tolima'),
        ('Valle_del_Cauca', 'Valle_del_Cauca'),
        ('Vichada', 'Vichada'),
        ('Vaupés', 'Vaupés'),
        ]
        
    name = models.CharField(max_length=100)
    department = models.CharField(
        choices= DEPARTMENTS,
        max_length=100
    )
    city = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

class LeasingPrice(models.Model):
    CURRENCIES = [
        ('COP', 'Peso Colombiano'),
        ('USD', 'USA Dollar')
    ]
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    actualzation_date = models.DateField(auto_now_add=True, auto_created=True)
    currency = models.CharField(choices=CURRENCIES, max_length=5)
    price = models.IntegerField()

class ImageProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images/%Y/%m/%d/")
    
class CommercialRelation(models.Model):
    lessor = models.ForeignKey(User, on_delete=models.PROTECT)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    leasing_price = models.ForeignKey(LeasingPrice, on_delete=models.PROTECT)