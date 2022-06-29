from django.contrib import admin
from .models import Post, Comment
from import_export.admin import ImportExportModelAdmin

@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass


@admin.register(Comment)
class CommentImportExport(ImportExportModelAdmin):
    pass