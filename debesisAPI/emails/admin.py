from django.contrib import admin
from .models import Mailbox, Email, Template

admin.site.register(Mailbox)
admin.site.register(Email)
admin.site.register(Template)
# admin.site.register(ArrayField)
