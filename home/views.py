from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from home.models import Account, Shop,Menu
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Create your views here.

@login_required(login_url='login')
def index(request):
    # Fetch the list of all shops for the user
    shops = Shop.objects.all()
    return render(request,'index.html',{'shps':shops})

def Login(request):
    if request.method=='POST':
        usr=request.POST.get("username")
        password1=request.POST.get("password")
        print("USER: ",usr)
        print("PASSW: ",password1)
        user = auth.authenticate(username=usr, password=password1)
        if user is not None:
            auth.login(request, user)
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'login.html')

        # redirect to user index page or to restaurant manage page based on user type
        user_type = Account.objects.get(user=user).user_type
        if(user_type == 'restaurant_owner'):
            return redirect('restaurant/manage')
        return index(request)
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        user_type = request.POST.get('user_type')
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'User Exists!')
            else:
                user = User.objects.create_user(username=username, password=pass1,email=email)
                user.save()
                # Save details to the Account table
                ac = Account(user=user,user_type=user_type)
                ac.save()

               
                return Login(request)
        else:
            messages.warning(request,'Password not maching!')
            return render(request,'signup.html')
        
    return render(request,'signup.html')

def menu(request,id):
    # fetch the items from the shop
    items = Menu.objects.filter(shop__id = id)
    return render(request,'menu.html',{'itms':items})

# -------------------------------------------------------------------------------
# Restaurant manage
def rest_manage(request):
    shops = Shop.objects.filter(owner__user = request.user)
    return render(request,'rest_manage.html',{'shps':shops})

def rest_menu(request,id):
    # fetch the items from the shop
    items = Menu.objects.filter(shop__id = id)
    return render(request,'rest_menu.html',{'itms':items,'shp_id':id})

# delete an item

def delete_item(request,id):
    item = Menu.objects.get(id=id)
    shp = item.shop.id
    item.delete()
    return redirect(f'/rest_menu/{shp}')

# add item
def add_item(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        shop = Shop.objects.get(id=id)

        # Save item to database
        item = Menu(shop = shop,item_name=name,price=price)
        item.save()
        return redirect(f'/rest_menu/{id}')
    return render(request,'add_item.html',{'shp_id':id})

# delete shop
def delete_shop(request,id):
    item = Shop.objects.get(id=id)
    item.delete()
    return redirect('/restaurant/manage')

# add shop
def add_shop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        owner = Account.objects.get(user=request.user)

        # Save item to database
        item = Shop(owner = owner,name=name)
        item.save()
        return redirect('/restaurant/manage')
    return render(request,'add_shop.html')



