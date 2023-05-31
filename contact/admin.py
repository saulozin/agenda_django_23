#Administração do Django

from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'phone', 'show',
    )

    ordering = (
        'id',
    )

    #list_filter = ('created_date',) #filtrar por data de criação do contato

    search_fields = (
        'id', 'first_name', 'last_name',
    )

    #Lista o número de contatos cadastrados mostrados na tela por página
    list_per_page = 10
    list_max_show_all = 200

    #Modifica os campos selecionados para edição já na exibição do contato: Cuidado
    list_editable = ('first_name', 'last_name', 'phone', 'show',)

    list_display_links = ('id',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = (
        'id',
    )
