from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import MySQLdb
import datetime
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json
from datetime import date
from datetime import datetime
import datetime

db = MySQLdb.connect('localhost','root','','wishlist')
c = db.cursor()
# Create your views here.
def Customer_Registration(request):
    msg=""
    if request.POST:
        cname = request.POST.get("cname")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        district = request.POST.get("district")
        location = request.POST.get("location")
        email = request.POST.get("Email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("Password")
        type= "Customer"
        qry="insert into cusreg(cname,address,pincode,gender,age,district,location,email,mobile,password) values('"+ cname +"','"+ address +"','"+ pincode +"','"+ gender +"','"+ age +"','"+ district +"','"+ location +"','"+ email +"','"+ mobile +"','"+ password +"')"
        qr ="insert into login values('"+ email +"','"+ password +"','"+ type +"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        msg="Successfully Registered"
        # return render(request,'Customer Registration.html',{"msg":msg})

        return HttpResponseRedirect("/home/")

    return render(request,'Customer Registration.html',{"msg":msg})

def SignIn(request):  
    request.session['username']=""
    request.session['NAME']=""
    request.session['uid']=""
    request.session['cid']=""
    request.session['sid']=""

    if request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        m="select * from login where username='"+ email +"' and password='"+ password +"'"
        c.execute(m)
        print(m)
        ds = c.fetchone()
        request.session['username']=email
        print(ds[2])
        if ds[2] == 'Admin':
            return HttpResponseRedirect('/AdminHome/')
        elif ds[2] == 'Customer':
            c.execute("select * from cusreg where email='"+email+"' and password='"+password+"'")
            ds = c.fetchone()
            request.session['uid'] = ds[0]
            request.session['NAME'] = ds[1]
            return HttpResponseRedirect('/Customer_Home/')
        
        elif ds[2] == 'Shop':
            c.execute("select * from shopreg where email='"+email+"' and password='"+password+"'")

            ds = c.fetchone()
            request.session['sid'] = ds[0]
            return HttpResponseRedirect('/Shop_Home/')
    return render(request,'Login.html') 

def Club_Registration(request):
    if request.POST:
        cname = request.POST.get("cname")
        district = request.POST.get("district")
        location =request.POST.get("location")
        email =request.POST.get("Email")
        mobile= request.POST.get("mobile")
        regno = request.POST.get("regno")
        password = request.POST.get("Password")
        status = "Registered"
        type = "shop"
        qry = "insert into shopreg(clname,district,city,phone,email,reg_no,password,status) values('"+ cname +"','"+ district +"','"+ location +"','"+ mobile +"','"+ email +"','"+ regno +"','"+ password +"','"+ status +"')"
        qr ="insert into login values('"+ email +"','"+ password +"','"+ type +"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
    return render(request,'Club Registration.html')
def Admin_Home(request):
    return render(request,'Admin Home.html') 

def Common_Home(request):
    return render(request,'Common Home.html')

def Shop_Home(request):
    return render(request,'Shop Home.html')

def Customer_Home(request):
    return render(request,'Customer Home.html')

def About_Us(request):
    return render(request,'about.html') 

def Gallery(request):
    return render(request,'gallery.html') 

def Contact(request):
    return render(request,'contact.html')

def Shop_Registration(request):
    msg=""
    if request.POST:
        cname = request.POST.get("cname")
        district = request.POST.get("district")
        location = request.POST.get("location")
        email = request.POST.get("Email")
        mobile = request.POST.get("mobile")
        regno = request.POST.get("regno")
        password = request.POST.get("Password")
        qry = "insert into shopreg(shop,district,city,phone,email,reg_no,password,status) values('"+ cname +"','"+ district +"','"+ location +"','"+ mobile +"','"+ email +"','"+ regno +"','"+ password +"','Registered')"
        qr = "insert into login values('"+ email +"','"+ password +"','Shop')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        msg="Successfully Registered"
        return HttpResponseRedirect("/home/")
    return render(request,'Shop Registration.html',{"msg":msg})
  

def Admin_Add_Category(request):
    msg=""
    if request.POST:
        na = request.POST.get("cat_name")
        qry="insert into categories(cat_title) values('"+ na +"')"
        c.execute(qry)
        db.commit()
        msg = "Category Added Successfully."
    c.execute("select * from workshop_reg")
    data=c.fetchall() 
    return render(request,'Admin Add Category.html',{"data":data,"msg":msg})
def AdminRemoveCategory(request):
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from categories where cat_id = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/Admin_Add_Category/")
    return render(request,'AdminRemoveCategory.html')
def Admin_View_Customers(request):
    data = ""
    c.execute("select * from cusreg")
    data=c.fetchall() 
    return render (request,"Admin View Customers.html",{"data":data})

def Admin_View_Feedback(request):
    data = ""
    c.execute("select feedback.*,cusreg.* from feedback inner join cusreg on cusreg.cid=feedback.userid")
    data=c.fetchall()

    return render (request,"Admin View Feedback.html",{"data":data})
def Admin_View_Shop(request):
    c.execute("SELECT * from shopreg where status = 'Registered'")
    data = c.fetchall()
    if request.GET:
        cl = request.GET.get('id')
        st = request.GET.get('st')
        c.execute("update shopreg set status = '"+st+"' where sid = '"+cl+"'")
        db.commit()
        return HttpResponseRedirect("/AdminViewShop/")
    return render(request,"Admin View Shop.html",{"data":data})
def Admin_View_Approved_Shop(request):
    c.execute("SELECT * from shopreg where status = 'accept'")
    data = c.fetchall()
    if request.GET:
        cl = request.GET.get('id')
        st = request.GET.get('st')
        c.execute("update shopreg set status = '"+st+"' where sid = '"+cl+"'")
        db.commit()
        return HttpResponseRedirect("/AdminViewShop/")
    return render(request,"Admin View Approved Shop.html",{"data":data})
def Customerviewproduct(request):
    sid = request.session['sid']
    c.execute("select * from categories")
    data=c.fetchall()
   
    msg=""  
    if request.POST:
       
        b=request.POST.get("cat_title")
        c1=request.POST.get("name")   
        request.session["cate"]=b
        request.session["brand"]=c1
        return HttpResponseRedirect("/CustomerShopping/")
    return render(request,"CustomerViewProducts.html",{"cat":data})

def CustomerShopping(request):
    msg=""
    data=""
    cat=request.session["cate"]
    br=request.session["brand"]
    s="select count(*) from products inner join categories on products.product_cat=categories.cat_id inner join shopreg on products.shid=shopreg.sid where categories.cat_title='"+str(cat)+"' and products.product_keywords='"+str(br)+"'"
    c.execute(s)
    
    data1=c.fetchone()
    print(data1)
    p=data1[0]
    if p>0:
        s="select products.*,shopreg.shop,shopreg.email from products inner join categories on products.product_cat=categories.cat_id inner join shopreg on products.shid=shopreg.sid where categories.cat_title='"+str(cat)+"' and products.product_keywords='"+str(br)+"'"
        c.execute(s)
        
        data=c.fetchall()
        print(data)
        t="select * from categories"
        c.execute(t)
        data1=c.fetchall()
        print(data)
    else:
        msg="Products Not Available"
        return render(request,'CustomerShopping.html',{"data":data,"data1":data1,"msg":msg})

        return HttpResponseRedirect("/Customerviewproduct/")
    return render(request,'CustomerShopping.html',{"data":data,"data1":data1,"msg":msg})

def CustomerViewProDetails(Request):
    pid=Request.GET.get("id")
    sna=Request.GET.get("na")
    em=Request.GET.get("em")
    print(sna,em)
    s="select * from products where product_id = '"+str(pid)+"'"
    c.execute(s)
    data=c.fetchall()
    t="select * from categories"
    c.execute(t)
    data1=c.fetchall()
    # u="select * from brands"
    # c.execute(u)
    # data2=c.fetchall()

    if(Request.POST):
        cid = Request.session["uid"]
        price = data[0][4]
        qty = Request.POST.get("qty")
        am = int(qty) * int(price)
        c.execute("insert into cart (cid,pid,qty,price)values('"+str(cid)+"','"+str(pid)+"','"+str(qty)+"','"+str(am)+"')")
        db.commit()
    return render(Request,'CustomerViewProDetails.html',{"data":data,"data1":data1,"sna":sna,"em":em})

def CustomerViewCart(request):
    cid =  request.session['uid']
    request.session["userid"]=cid
    li=[]
    s="select * from cart inner join products on cart.pid = products.product_id where cart.cid = '"+str(cid)+"'"
    c.execute(s)
    data=c.fetchall()
    # merid = data[0][9]
    # price = data[0][6]
    # pid = data[0][3]
    # qty = data[0][5]
    t="select count(*) from cart where cid = '"+str(cid)+"'"
    c.execute(t)
    print(t)
    data1=c.fetchone()
    u="select sum(price) from cart where cid = '"+str(cid)+"'"
    c.execute(u)
    data2=c.fetchone()
    totalamount = data2[0]
    tot = totalamount
    request.session["pay"] = str(tot)
    if request.GET:
        ci = request.GET.get('id')
        c.execute("delete from cart where cid = '"+str(ci)+"'")
        db.commit()
        return HttpResponseRedirect("/CustomerViewCart")
    if(request.POST):
        m="select * from cart where cid = '"+str(cid)+"'"
        c.execute(m)
        data3 = c.fetchall()
        for d3 in data3:
            custid = d3[1]
            proid = d3[2]
            m="select product_title from products where product_id='"+str(proid)+"'"
            c.execute(m)
            da=c.fetchone()
            prn=da[0]
            amot = d3[4]
            quty = d3[3]
            carid = d3[0]
            li.append(prn)
            print(li)
            request.session["prlist"]=li
            c.execute("insert into customer_order (uid,pid,p_price,p_qty)values('"+str(cid)+"','"+str(proid)+"','"+str(amot)+"','"+str(quty)+"')")
            db.commit()
            c.execute("delete from cart where id = '"+str(carid)+"'")
            db.commit()
        return HttpResponseRedirect("/payment1")
    return render(request,'CustomerViewCart.html',{"data":data,"data1":data1[0],"data2":data2[0]})

def Shop_Add_Product(request):
    sid = request.session['sid']
    c.execute("select * from categories")
    data=c.fetchall()
   
    msg=""  
    if request.POST:
        a=request.POST.get("product_title")
        b=request.POST.get("cat_title")
        c1=request.POST.get("brand_title")   
        d=request.POST.get('price')
        e=request.POST.get('qty')
        f=request.POST.get('des')
        g=request.POST.get('key')
        if request.FILES.get("file"):
            myfile=request.FILES.get("file")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
            c.execute("insert into products(product_cat,product_brand,product_title,product_price,quantity,product_desc,product_image,product_keywords,shid) values('"+ str(b) +"','"+ str(c1) +"','"+ str(a) +"','"+ str(d) +"','"+ str(e) +"','"+ str(f) +"','"+ uploaded_file_url +"','"+ str(g) +"','"+ str(sid) +"')")
            db.commit()       
            msg = "Products Added Successfully."
    return render(request,"Shop Add Product.html",{"cat":data,"msg":msg})

def ShopRemoveProduct(request):
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from products where product_id = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/ShopViewMyProduct/")
    return render(request,'ShopRemoveProduct.html')

def Shop_View_Orders(request):
    shid = request.session['sid']
    m="SELECT customer_order.*, cusreg.*,products.* FROM customer_order INNER JOIN cusreg ON customer_order.uid=cusreg.cid inner join products on products.product_id=customer_order.pid where products.shid = '"+str(shid)+"'"
    c.execute(m)
    data = c.fetchall()
    print(data)
    return render(request,"Shop View Orders.html",{"data":data})

def Shop_View_My_Product(request):
    shid = request.session['sid']
    c.execute("select * from products where shid = '"+str(shid)+"'")
    data = c.fetchall()
    if request.GET:
        return HttpResponseRedirect("/ShopUpdateProduct/")
    return render(request,"Shop View My Product.html",{"data":data})

def Shop_View_payment(request):
    shid = request.session['sid']
    c.execute("select cusreg.email,cusreg.cname,products.*,customer_order.* from products inner join customer_order on customer_order.pid=products.product_id inner join cusreg where products.shid = '"+str(shid)+"'")
    data = c.fetchall()
    print(data)
    return render(request,"Shop view payment.html",{"data":data})

def ShopUpdateProduct(request):
    pid = request.GET.get('id')
    c.execute("select * from products where product_id = '"+str(pid)+"'")
    data = c.fetchall()
    if request.POST:
            price=request.POST.get("price")
            qty=request.POST.get("qty") 
            c.execute("update products set product_price = '"+str(price)+"', quantity = '"+str(qty)+"' where product_id = '"+str(pid)+"'")
            db.commit()
            return HttpResponseRedirect("/ShopViewMyProduct/")
    return render(request,"ShopUpdateProduct.html",{"data":data})
def payment1(request):
    
    if request.POST:
        card=request.POST.get("test")
        request.session["card"]=card
        cardno=request.POST.get("cardno")
        request.session["card_no"]=cardno
        pinno=request.POST.get("pinno")
        request.session["pinno"]=pinno
        return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html")

def payment2(request):
    cno=request.session["card_no"]
    amount=request.session["pay"]
    if request.POST:
        # name=request.POST.get("t1")
        # request.session["m"]=name
        # address=request.POST.get("t2")
        # email=request.POST.get("t3")
        # phno=request.POST.get("t4")
        # n="insert into delivery values('"+str(cno)+"','"+str(name)+"','"+str(address)+"','"+str(email)+"','"+str(phno)+"','"+str(amount)+"')"
        # print(n)
        # c.execute(n)
        # con.commit()
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    uid=request.session["userid"]
    cno=request.session["card_no"]
    today = date.today()
    name =  request.session['NAME'] 
    amount = request.session["pay"]
    # for i in li:
    #     d=li[i]
    if "go" in request.POST:
        li=request.session["prlist"]
        print(li)

        c.execute("select mobile from cusreg where cid='"+str(uid)+"'")
        ds = c.fetchone()
        ph=ds[0]
        
        msg="Your Products '"+str(li)+"' has been payed successsfully"
        return HttpResponseRedirect("http://dattaanjaneya.biz/API_Services/SMS_Service.php?content="+msg+"&mobile="+ph+"")
        print(msg)
    return render(request,"payment5.html",{"cno":cno,"today":today,"name":name,"amount":amount})

def CustomerViewMyBooking(request):
    cid=request.session["uid"]
    c.execute("select * from customer_order inner join products on customer_order.pid = products.product_id where customer_order.uid = '"+str(cid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewMyBooking.html",{"data":data})

def CustomerViewOrders(request):
    cid=request.session["uid"]
    c.execute("select * from customer_order inner join products on customer_order.pid = products.product_id inner join cust_reg on customer_order.uid = cust_reg.cid where customer_order.uid = '"+str(cid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewOrders.html",{"data":data})
def Customer_View_Profile(request):
    uid = request.session['uid']
    data=""
    if request.session['uid']:   
        c.execute(" select * from cusreg where cid='"+str(uid)+"'")
        data=c.fetchall()
        if "submit" in request.POST:
            Address=request.POST.get("Address")
            Phn=request.POST.get("Phn") 
            m="update cusreg set mobile='"+Phn+"',address='"+Address+"' where cid='"+str(uid)+"'"
            c.execute(m)
            db.commit()
            print(m)
            return HttpResponseRedirect("/CustomerViewProfile/")
    return render (request,"Customer View Profile.html",{"data":data})
def Customer_AddFeedback(request):
    msg=""
    if request.POST:
        descr=request.POST.get("Address")
        uid=request.session['uid']
        da=datetime.date.today()
        m="insert into feedback(feedback,date,userid) values('"+ str(descr) +"','"+ str(da) +"','"+ str(uid) +"')"
        c.execute(m)
        db.commit()       
        msg = "Added Successfully."
    return render (request,"Customer Add Feedback.html",{"msg":msg})

  

