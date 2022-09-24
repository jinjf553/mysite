from typing import Dict, Optional, Sequence

from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    search_fields: Sequence[str] = ('status', 'created', 'publish', 'author')
    prepopulated_fields: Dict[str, Sequence[str]] = {'slug': ('title', )}
    raw_id_fields: Sequence[str] = ('author', )
    date_hierarchy: Optional[str] = 'publish'
    ordering: Optional[Sequence[str]] = ('status', 'publish')
