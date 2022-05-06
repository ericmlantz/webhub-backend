from django.contrib import admin
from .models import User
from .models import Interest
from .models import Page
from .models import Search
from .models import Note

# Register your models here.
admin.site.register(User)
admin.site.register(Interest)
admin.site.register(Page)
admin.site.register(Search)
admin.site.register(Note)