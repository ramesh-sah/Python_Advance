from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from About.models import about 
from enquiry.models import Enquiry
from refund.models import Refund
from terms.models import Terms
from cart.models import Cart
from itemwhitelist.models import WhiteList
from ChekOut.models import CheckOutDetail

from shop.models import MensCloths,MensShoes,MensWatches,WomensHandbags,WomensGlasses
CustomUser = get_user_model()



def home(request):
    men_cloths=MensCloths.objects.all().order_by('-product_name')[:1]
    men_shoes=MensShoes.objects.all().order_by('-product_name')[:1]
    men_watches=MensWatches.objects.all().all().order_by('-product_name')[:1]
    women_handbags=WomensHandbags.objects.all().all().order_by('-product_name')[:1]
    women_glasses=WomensGlasses.objects.all().all().order_by('-product_name')[:1]
    data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses}
    return render(request,"index.html",data)

def signup(request):
    if request.method=="POST":
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        country=request.POST.get('country')
        city=request.POST.get('city')
        address=request.POST.get('address')
        tel=request.POST.get('tel')
        mobile=request.POST.get('mobile')
        profile_image=request.POST.get('profile_image')
        print(first_name,last_name,email,country,city,address,tel,mobile,password)
        if CustomUser.objects.filter(email=email).exists():
            return redirect('login')
        user_obj=CustomUser.objects.create(first_name=first_name,
                                           last_name=last_name,
                                           email=email,
                                           country=country,
                                           city=city,
                                           address=address,
                                           tel=tel,
                                           mobile=mobile,
                                           profile_image=profile_image)
        user_obj.set_password(password)
        user_obj.save()
        return redirect('login')
    return render(request,"signup.html")

def Login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        request.session['email']=email
        account(request)
        cart(request)
        Whitelist(request)
        checkOut(request)
        orders(request)
        changePassword(request)
        print(email,password)

        if not CustomUser.objects.filter(email=email).exists():
            return redirect('signup')
        user_obj=authenticate(request, email=email , password=password )
        if user_obj:
            login(request,user_obj)
            return redirect('account')
        return redirect('home')
    return render(request,"login.html")

def forgetPassword(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=CustomUser.objects.get(email=email)
        user_obj.set_password(password)
        user_obj.save()
        return redirect('login')
            
    return render(request,"forgetpassword.html")

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def account(request):
    data={}
    email=request.session.get('email')
    if email is not None:
        user=CustomUser.objects.get(email=email)
        data={'user': user}
            
    try:
        if request.method == 'POST':
            user_fname=request.POST.get('fname')
            user_lname=request.POST.get('lname')
            user_country=request.POST.get('country')
            user_city=request.POST.get('city')
            user_address=request.POST.get('address')
            user_tel=request.POST.get('tel')
            user_mobile=request.POST.get('mobile')
            user_email=request.POST.get('email')
            st=CustomUser.objects.get(email=email)
            st.first_name=user_fname
            st.last_name=user_lname
            st.email=user_email
            st.country=user_country
            st.city=user_city
            st.address=user_address
            st.tel=user_tel
            st.mobile=user_mobile
            st.save()
    except:
            pass

           
    return render(request,"account.html",data)


def AboutUs(request):
    abouts=about.objects.all()[:1]
    data={'abouts' : abouts}
    return render(request,"about.html",data)

@login_required(login_url='login')
def cart(request,slug=None):
            if MensCloths.objects.filter(slug=slug).exists() :
                        product_info=MensCloths.objects.get(slug=slug)
                        product_name=product_info.product_name
                        description=product_info.product_short_description
                        product_price=product_info.product_price
                        product_image=product_info.product_image
                        customer_email=request.session.get('email')
                        
                        print(customer_email,product_name,description,product_price)
                        st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email,product_image=product_image)
                        st.save()
                        # return redirect('cart')
            elif MensShoes.objects.filter(slug=slug).exists():
                        product_info=MensShoes.objects.get(slug=slug)
                        product_name=product_info.product_name
                        description=product_info.product_short_description
                        product_price=product_info.product_price
                        product_image=product_info.product_image
                        customer_email=request.session.get('email')
                        st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email,product_image=product_image)
                        st.save()
                        # return redirect('cart')
            elif MensWatches.objects.filter(slug=slug).exists():
                        product_info=MensWatches.objects.get(slug=slug)
                        product_name=product_info.product_name
                        description=product_info.product_short_description
                        product_price=product_info.product_price
                        product_image=product_info.product_image
                        customer_email=request.session.get('email')
                        st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email,product_image=product_image)
                        st.save()
                        # return redirect('cart')
                    
            elif WomensHandbags.objects.filter(slug=slug).exists():
                        product_info=WomensHandbags.objects.get(slug=slug)
                        product_name=product_info.product_name
                        description=product_info.product_short_description
                        product_price=product_info.product_price
                        product_image=product_info.product_image
                        customer_email=request.session.get('email')
                        st=Cart(product_name=product_name, description=description,product_price=product_price)
                        st.save()
                        # return redirect('cart')
                    
            elif WomensGlasses.objects.filter(slug=slug).exists():
                        product_info=WomensGlasses.objects.get(slug=slug)
                        product_name=product_info.product_name
                        description=product_info.product_short_description
                        product_price=product_info.product_price
                        product_image=product_info.product_image
                        customer_email=request.session.get('email')
                        st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email,product_image=product_image)
                        st.save()
                        # return redirect('cart')
                    
            else:
                        print("error creating")
            email=request.session.get('email')
            if Cart.objects.filter(customer_email=email).exists():
                cart_obj=Cart.objects.filter(customer_email=email).order_by('-id')[:4]
                total_product=Cart.objects.filter(customer_email=email)
                total_cart_product=total_product.count()
                total_cart_item_list=[int(i.no_of_product_item) for i in total_product]
                total_cart_item=sum(total_cart_item_list)
                print(total_cart_item)
                
                total_amount_list = [int(item.product_price) for item in total_product]
                total_amount = sum(total_amount_list) 
                print(total_amount)
                
                
                data={'cart_obj':cart_obj,'total_cart_product':total_cart_product,'total_item':total_cart_item,
                    'total_amount':total_amount}
            

                
            return render(request,"cart.html",data)
def DeleteCartItem(request,slug=None):
    cart_obj=Cart.objects.filter(slug=slug)
    cart_obj.delete()
    return redirect('cartview')
                
  
    

@login_required(login_url='login')
def changePassword(request):
    email=request.session.get('email')
    if request.method == 'POST':
        old_password=request.POST.get('old_password')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        user_obj=CustomUser.objects.get(email=email)
        if user_obj.check_password(old_password) and new_password==confirm_password:
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
    user=CustomUser.objects.get(email=email)
    data={'user': user}
    return render(request,"change-password.html",data)

@login_required(login_url='login')
def checkOut(request,slug=None,id=None):
    email=request.session.get('email')
    if  Cart.objects.filter(slug=slug).exists():
            obj_show=Cart.objects.get(slug=slug)
            product_price=obj_show.product_price
            discount_amount = 0.13 * int(product_price)
            final_price=100+int(product_price)-discount_amount
    elif WhiteList.objects.filter(id=id).exists():
            obj_show=WhiteList.objects.get(id=id)
            product_price=obj_show.product_price
            discount_amount = 0.13 * int(product_price)
            final_price=100+int(product_price)-discount_amount
    data={'email':email,'item_price':product_price,'final_price':final_price,'discount_amount':discount_amount}
   
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        pemail=request.POST.get('email')
        country=request.POST.get('country')
        city=request.POST.get('city')
        address=request.POST.get('address')
        login_email=request.POST.get('lemail')
        tel=request.POST.get('tel')
        mobile=request.POST.get('mobile')
        ordernote=request.POST.get('ordernote')
        payment=request.POST.get('payment')
        if  Cart.objects.filter(slug=slug).exists():
                obj=Cart.objects.get(slug=slug)
                product_name=obj.product_name
                no_of_product_item=obj.no_of_product_item
                checkout_obj=CheckOutDetail(first_name=first_name, last_name=last_name,email=pemail,country=country,slug=slug,
                                      city=city, address=address,login_email=login_email,tel=tel,mobile=mobile,ordernote=ordernote,payment=payment,
                                      product_name=product_name,product_price=product_price,no_of_product_item=no_of_product_item)
                checkout_obj.save()
                cart_obj=Cart.objects.filter(slug=slug)
                cart_obj.delete()
                
                return redirect('orders')
        elif  WhiteList.objects.filter(id=id).exists():
                obj=WhiteList.objects.get(id=id)
                product_name=obj.product_name
              
                checkout_obj=CheckOutDetail(first_name=first_name, last_name=last_name,email=pemail,country=country,slug=id,
                                      city=city, address=address,login_email=login_email,tel=tel,mobile=mobile,ordernote=ordernote,payment=payment,
                                      product_name=product_name)
                checkout_obj.save()
                cart_obj=WhiteList.objects.filter(id=id)
                cart_obj.delete()
                
                return redirect('orders')
        
            
            
    return render(request,"checkout.html",data)


def contact(request):
    if request.method=="POST":
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(first_name, last_name, email, message)
        if Enquiry.objects.filter(email=email).exists():
            return redirect('home')
        user=Enquiry(first_name=first_name, last_name=last_name, email=email, message=message)
        user.save()
        return redirect('home')
    return render(request,"contact.html")

@login_required(login_url='login')
def orders(request):
    email=request.session.get('email')
    if CustomUser.objects.filter(email=email).exists():
        obj1=CustomUser.objects.get(email=email)
        
    if CheckOutDetail.objects.filter(email=email).exists():
        obj2=CheckOutDetail.objects.filter(email=email)
    data={'obj1':obj1,'obj2':obj2}  
    return render(request,"orders.html",data)

@login_required(login_url='login')
def product(request,slug):
    men_cloths=MensCloths.objects.first()
    men_shoes=MensShoes.objects.first()
    men_watches=MensWatches.objects.all().first()
    women_handbags=WomensHandbags.objects.all().first()
    women_glasses=WomensGlasses.objects.all().first()
    data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses}
    if slug is not None:
        if MensCloths.objects.filter(slug=slug).exists():
            obj=MensCloths.objects.filter(slug=slug)
            print(obj)
            product_name=obj.product_name
            description=obj.product_short_description
            product_price=obj.product_price
            customer_email=request.session.get('email')
            print(customer_email,product_name,description,product_price)
            st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email)
            st.save()
            data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses,'obj': obj}
        elif MensShoes.objects.filter(slug=slug).exists():
            obj=MensShoes.objects.get(slug=slug)
            print(obj)
            product_name=obj.product_name
            description=obj.product_short_description
            product_price=obj.product_price
            customer_email=request.session.get('email')
            print(customer_email,product_name,description,product_price)
            st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email)
            st.save()
            data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses,'obj': obj}
        elif MensWatches.objects.filter(slug=slug).exists():
            obj=MensWatches.objects.get(slug=slug)
            print(obj)
            product_name=obj.product_name
            description=obj.product_short_description
            product_price=obj.product_price
            customer_email=request.session.get('email')
            print(customer_email,product_name,description,product_price)
            st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email)
            st.save()
            data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses,'obj': obj}
        elif WomensHandbags.objects.filter(slug=slug).exists():
            obj=WomensHandbags.objects.get(slug=slug)
            
            print(obj)
            product_name=obj.product_name
            description=obj.product_short_description
            product_price=obj.product_price
            customer_email=request.session.get('email')
            print(customer_email,product_name,description,product_price)
            st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email)
            st.save()
            data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses,'obj': obj}
        elif WomensGlasses.objects.filter(slug=slug).exists():
            obj=WomensGlasses.objects.get(slug=slug)
            print(obj)
            product_name=obj.product_name
            description=obj.product_short_description
            product_price=obj.product_price
            customer_email=request.session.get('email')
            print(customer_email,product_name,description,product_price)
            st=Cart(product_name=product_name, description=description,product_price=product_price,customer_email=customer_email)
            st.save()
            data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses,'obj': obj}
        else:
            print("error")
        if request.method=="POST":
            no_of_product_item=request.POST.get('no-of-product-item')
            if no_of_product_item is not None:
                if Cart.objects.filter(slug=slug).exists():
                    obj=Cart.objects.get(slug=slug)
                    obj.no_of_product_item=no_of_product_item
                    obj.save()
                    return redirect('cartview')
    
         
    return render(request,"product.html",data)

@login_required(login_url='login')
def refund(request):
    obj=Refund.objects.all()
    data={'obj' : obj}
    return render(request,"refund.html",data)

@login_required(login_url='login')
def shop(request):
    men_cloths=MensCloths.objects.all()
    men_shoes=MensShoes.objects.all()
    men_watches=MensWatches.objects.all()
    women_handbags=WomensHandbags.objects.all()
    women_glasses=WomensGlasses.objects.all()
    data={'men_cloths': men_cloths,'men_shoes': men_shoes,'men_watches': men_watches, 'women_handbags': women_handbags, 'women_glasses': women_glasses}
         
          
    
    return render(request,"shop.html",data)


@login_required(login_url='login')
def terms(request):
    objs=Terms.objects.all()
    data={'objs': objs}
    return render(request,'terms.html',data)

@login_required(login_url='login')
def Whitelist(request,slug=None):
    
    if slug is not None:
        if MensCloths.objects.filter(slug=slug).exists():
            obj=MensCloths.objects.get(slug=slug)
            product_price=obj.product_price
            product_name=obj.product_name
            product_image=obj.product_image
            customer_email=request.session.get('email')
            st.save()
            
        elif MensShoes.objects.filter(slug=slug).exists():
            obj=MensShoes.objects.get(slug=slug)
            product_price=obj.product_price
            product_name=obj.product_name
            product_image=obj.product_image
            customer_email=request.session.get('email')
            st=WhiteList(product_name=product_name,product_price=product_price, product_image=product_image, customer_email=customer_email)
            st.save()
            
        elif MensWatches.objects.filter(slug=slug).exists():
            obj=MensWatches.objects.get(slug=slug)
            product_price=obj.product_price
            product_name=obj.product_name
            product_image=obj.product_image
            customer_email=request.session.get('email')
            st=WhiteList(product_name=product_name,product_price=product_price, product_image=product_image, customer_email=customer_email)
            st.save()
          
        elif WomensHandbags.objects.filter(slug=slug).exists():
            obj=WomensHandbags.objects.get(slug=slug)
            product_price=obj.product_price
            
            product_name=obj.product_name
            product_image=obj.product_image
            customer_email=request.session.get('email')
            st=WhiteList(product_name=product_name,product_price=product_price, product_image=product_image, customer_email=customer_email)
            st.save()
    
        elif WomensGlasses.objects.filter(slug=slug).exists():
            obj=WomensGlasses.objects.get(slug=slug)
            product_price=obj.product_price
            product_name=obj.product_name
            product_image=obj.product_image
            customer_email=request.session.get('email')
            print(product_name,customer_email)
            st=WhiteList(product_name=product_name,product_price=product_price, product_image=product_image, customer_email=customer_email)
            st.save()
           
        else:
            print("error")
    customer_email=request.session.get('email')
    if WhiteList.objects.filter(customer_email=customer_email).exists():
        obj=WhiteList.objects.filter(customer_email=customer_email)
        data={'obj': obj}
    return render(request, 'whitelist.html',data)

def PrintBill(request,id=None):
    if CheckOutDetail.objects.filter(id=id):
        obj=CheckOutDetail.objects.get(id=id)
        data={'obj': obj}
        print(obj)
        
    return render(request,'printbill.html',data)


