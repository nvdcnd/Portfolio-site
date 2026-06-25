from django.shortcuts import redirect

def index(request):
    """
    Redirect legacy projects paths to portfolio.
    """
    return redirect('portfolio:index', permanent=True)
