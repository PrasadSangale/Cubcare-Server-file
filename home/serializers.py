from email.headerregistry import Address
from rest_framework import serializers

from home.models import Trainer, Vet,Breed_info,Places,Product,Dog_info

class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ('name', 'Contact_info','Address','link')
        
class VetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vet
        fields = ('name', 'Contact_info','Address','link')
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name','Price','link')
                
        
class Dog_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog_info
        fields = ('name', 'food','breed','link')
        
        
class PlacesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Places
        fields = ('name', 'Open_time','Close_time','Address','link')
        
class Breed_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed_info
        fields = ('name','information','link')
        
