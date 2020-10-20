from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from Events.models import Category, News, Imgs, Comment


class NewsImgInline(admin.TabularInline):
    model = Imgs
    extra = 4


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title', 'status']  # admin panal listesi
    list_filter = ['status']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'image_tag']
    readonly_fields = ['image_tag']
    list_filter = ['status', 'category']
    inlines = [NewsImgInline]

    prepopulated_fields = {'slug':('title',)}


class CategoryAdmin1(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            News,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                News,
                                                'category',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'



class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'news', 'status']

    list_filter = ['status', ]


admin.site.register(Category, CategoryAdmin1)


admin.site.register(News,NewsAdmin)

admin.site.register(Comment,CommentAdmin)
admin.site.register(Imgs)


