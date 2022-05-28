from django.contrib import admin

from crm.models import Order, Status, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    list_display = ('text', 'created_at', 'order')
    readonly_fields = ('created_at',)
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'name', 'phone', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name', 'phone')
    list_filter = ('status',)
    list_editable = ('status',)
    fields = ('status', 'name', 'phone', 'created_at')
    readonly_fields = ('created_at',)
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'order')
    readonly_fields = ('created_at',)


admin.site.register(Status)
