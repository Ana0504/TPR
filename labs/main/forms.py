from import_export import resources
from .models import TprLab1Strategy, TprLab1Dohod, TprLab1StrategyExample, TprLab1DohodsExample

class TprLab1StrategyForm(resources.ModelResource):
    class meta: 
        model = TprLab1Strategy


class TprLab1DohodForm(resources.ModelResource):
    class meta: 
        model = TprLab1Dohod


class TprLab1StrategyExampleForm(resources.ModelResource):
    class meta: 
        model = TprLab1StrategyExample


class TprLab1DohodExampleForm(resources.ModelResource):
    class meta: 
        model = TprLab1DohodsExample