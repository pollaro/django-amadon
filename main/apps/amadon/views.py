from django.shortcuts import render, redirect

def index(request):
    return render(request,'amadon/index.html')

def buy(request):
    print request.POST['item_id']
    if request.POST['item_id'] == '1001':
        order_price = int(request.POST['quantity']) * 19.99
    elif request.POST['item_id'] == '1002':
        order_price = int(request.POST['quantity']) * 29.99
    elif request.POST['item_id'] == '1003':
        order_price = int(request.POST['quantity']) * 4.99
    elif request.POST['item_id'] == '1004':
        order_price = int(request.POST['quantity']) * 49.99
    request.session['order_price'] = order_price
    if 'orders' not in request.session:
        request.session['orders'] = 1
        request.session['total'] = request.session['order_price']
    else:
        request.session['orders'] += 1
        request.session['total'] += request.session['order_price']
    return redirect(checkout)

def checkout(request):
    return render(request,'amadon/checkout.html')
