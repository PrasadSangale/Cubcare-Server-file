from django.contrib import admin
from home.models import Breed_info, Dog_info, Places, Product, Trainer, Vet

# Register your models here.
admin.site.register(Vet)
admin.site.register(Trainer)
admin.site.register(Places)
admin.site.register(Dog_info)
admin.site.register(Product)
admin.site.register(Breed_info)


