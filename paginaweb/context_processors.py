from .models import Carrito


def cart_renderer(request):
    
    try:
        if request.user.is_authenticated:
            carrito = Carritot.objects.get(user=request.user, completed=False)
            
        else:
            carrito = Carrito.objects.get(session_id = request.session['nonuser'], completed=False)
            
    except:
        carrito = {"num_of_items":0}
            
    return {"carrito": carrito}