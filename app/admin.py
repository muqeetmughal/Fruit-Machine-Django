from app.models import Draw, UniqueCode, Prize
from django.contrib import admin

from app.symbol import Symbol


class DrawAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'email', 'code', 'prize', 'symbol1', 'symbol2', 'symbol3', 'winner']
    list_filter = ['prize__winner', 'date']
    search_fields = ['code', 'email', 'prize__label']

    def symbol1(self, obj):
        return Symbol(obj.reel1).name

    def symbol2(self, obj):
        return Symbol(obj.reel2).name

    def symbol3(self, obj):
        return Symbol(obj.reel3).name


    def winner(self, obj):
        return obj.prize.winner

    def try_again(self, obj):
        return obj.prize.try_again


class UniqueCodeAdmin(admin.ModelAdmin):
    readonly_fields = ["code"]
    list_display = ['id', 'date', 'code', 'used']
    list_filter = ['used', 'date']


class PrizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'label', 'winner']
    list_filter = ['winner']


admin.site.register(UniqueCode, UniqueCodeAdmin)
admin.site.register(Draw, DrawAdmin)
admin.site.register(Prize, PrizeAdmin)
