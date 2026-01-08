from rest_framework import serializers
from .models import Category, Task



class RegisterSerializers(serializers.ModelSerializer):
    pass
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title',)

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("__all__")
    def to_representation(self, instance):
        repr1 = super().to_representation(instance)
        repr1['count'] = 12
        return  repr1