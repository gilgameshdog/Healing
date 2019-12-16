from rest_framework import serializers
from .models import Post, Categoria

class CategoriaSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()
    estado= serializers.BooleanField(default=True)

    #creacion de categoria#
    def create(self, validate_data):
        instance = Categoria()
        instance.nombre = validate_data.get('nombre')
        instance.estado = validate_data.get('estado')
        instance.save()
        return instance

    def validate_nombre(self, data):
        categorias = Categoria.objects.filter(nombre=data)
        if len(categorias) != 0:
            raise serializers.ValidationError(
                "Este nombre de categoria ya existe, ingrese uno nuevo")
        else:
            return data
