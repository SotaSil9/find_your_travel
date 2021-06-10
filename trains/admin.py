from django.contrib import admin

from trains.models import Train


class TrainAdmin(admin.ModelAdmin):  # регистарция необходимых параметров
    class Meta:
        model = Train
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_editable = ('travel_time',)


admin.site.register(Train, TrainAdmin)
