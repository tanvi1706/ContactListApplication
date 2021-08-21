from django.contrib import admin
from contacts.models import contact, address, phone, date
# Register your models here.
admin.site.register(contact)
admin.site.register(address)
admin.site.register(phone)
admin.site.register(date)