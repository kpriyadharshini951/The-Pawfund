from django.contrib import admin
from .models import Donation
from .models import Adoption

admin.site.register(Donation)
admin.site.register(Adoption)

