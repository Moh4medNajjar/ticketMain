# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
#
# from .models import Cart
# from event.models import Event  # Assuming you want to add events to the cart
#
#
# @login_required
# def cart_detail(request):
#     """
#     Displays the contents of the user's cart.
#     """
#     cart = Cart.objects.filter(user=request.user).first()
#     if not cart:
#         cart = Cart.objects.create(user=request.user)
#
#     context = {
#         'cart': cart,
#     }
#     return render(request, 'cart/cart_detail.html', context)
#
#
# @login_required
# def add_to_cart(request, event_id):
#     """
#     Adds an event to the user's cart.
#     """
#     event = get_object_or_404(Event, pk=event_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     if event in cart.items.all():
#         # Item already exists in cart, handle it (e.g., display message)
#         message = 'Event already exists in your cart.'
#     else:
#         cart.items.add(event)
#         message = f'Event "{event.title}" added to your cart.'
#     context = {
#         'message': message,
#     }
#     return redirect('cart:cart_detail')  # Redirect to cart detail page after adding
#
#
# @login_required
# def remove_from_cart(request, event_id):
#     """
#     Removes an event from the user's cart.
#     """
#     event = get_object_or_404(Event, pk=event_id)
#     cart = get_object_or_404(Cart, user=request.user)
#     cart.items.remove(event)
#     message = f'Event "{event.title}" removed from your cart.'
#     context = {
#         'message': message,
#     }
#     return redirect('cart:cart_detail')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Cart
from event.models import Event  # Assuming you want to add events to the cart
from .serializers import CartSerializer


@login_required
def cart_detail(request):
    """
    Displays the contents of the user's cart (for potential future UI).
    """
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart.objects.create(user=request.user)

    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)  # Optional template view


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request):
    """
    API endpoint to retrieve the user's cart data.
    """
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart.objects.create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, event_id):
    """
    API endpoint to add an event to the user's cart.
    """
    event = get_object_or_404(Event, pk=event_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if event in cart.items.all():
        # Item already exists in cart, handle it (e.g., return appropriate message)
        return Response({'message': 'Event already exists in your cart.'})
    else:
        cart.items.add(event)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(['DELETE', 'POST'])  # Can also use separate DELETE and PUT for remove/update
@permission_classes([IsAuthenticated])
def manage_cart_item(request, event_id):
    """
    API endpoint to manage cart items (add or remove).
    """
    event = get_object_or_404(Event, pk=event_id)
    cart = get_object_or_404(Cart, user=request.user)

    if request.method == 'DELETE':
        cart.items.remove(event)
        message = f'Event "{event.title}" removed from your cart.'
    elif request.method == 'POST':
        # Implement logic to update cart item quantity (if applicable)
        message = f'Event "{event.title}" quantity updated in your cart.'  # Placeholder

    serializer = CartSerializer(cart)
    return Response({'message': message, 'data': serializer.data})
