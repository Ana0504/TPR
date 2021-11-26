from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TprLab1Strategy, TprLab1Dohod, TprLab1DohodsExample, TprLab1StrategyExample

# Register your models here.

@admin.register(TprLab1Strategy)
class TprLab1StrategyAdmin(ImportExportModelAdmin):
    list_display = ('numStrategy', 'good_good', 'good_bad', 'bad_good', 'bad_bad')


@admin.register(TprLab1Dohod)
class TprLab1DohodAdmin(ImportExportModelAdmin):
    list_display = ('numDohod', 'good_good', 'good_bad', 'bad_good', 'bad_bad')


@admin.register(TprLab1StrategyExample)
class TprLab1StrategyExampleAdmin(ImportExportModelAdmin):
    list_display = ('one_one','one_two','one_three','two_one','two_two','two_three','three_one','three_two','three_three')


@admin.register(TprLab1DohodsExample)
class TprLab1DohodsExampleAdmin(ImportExportModelAdmin):
    list_display = ('one_one','one_two','one_three','two_one','two_two','two_three','three_one','three_two','three_three')