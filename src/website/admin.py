from djangoseo.admin import register_seo_admin
from django.contrib import admin
from mysite.seo import MyMetadata

# Register your models here.
from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","email","received"]
    class Meta:
        model = Contact

register_seo_admin(admin.site, MyMetadata)
admin.site.register(Contact, ContactAdmin)
