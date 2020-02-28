from django.contrib import admin
from .models import User, Province
from django.forms import ModelForm, TextInput
from suit.widgets import AutosizedTextarea



# Register your models here.


# class UserInline(admin.TabularInline):
#     model = User
#     suit_classes = 'suit-tab suit-tab-cities'

# class UserInline(admin.TabularInline):
#     model = User
#     suit_classes = 'suit-tab suit-tab-cities'

class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')


    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class UserAdmin(admin.ModelAdmin):
    # inlines = (UserInline,)
    # form = ProductForm
    list_display = ('name', 'level', 'email', 'mobile_phone', )
    fields = ('name', 'level', 'province', 'email', 'mobile_phone', 'elevators', 'create_time', 'update_time')
    search_fields = ('name',)
    readonly_fields = ('create_time', 'update_time')
    # suit_form_tabs = (('name', 'name'), ('level', 'level'),
    #                   )
    # date_hierarchy = 'create_time'
    radio_fields = {'level': admin.VERTICAL}
    autocomplete_fields = ['province']


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        province = form.base_fields["province"]

        province.widget.can_add_related = False
        province.widget.can_delete_related = False
        province.widget.can_change_related = False

        return form

admin.site.register(User, UserAdmin)
admin.site.register(Province, ProvinceAdmin)

