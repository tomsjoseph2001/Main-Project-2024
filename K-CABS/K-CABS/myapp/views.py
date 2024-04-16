from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Q, Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import  datetime
from django.shortcuts import get_object_or_404
from .models import User

import base64

mediapath = "C:\\22-23\\trendtrove\\media\\"


from myapp.models import *


def login(request):

    request.session["lid"]=""

    return render(request, "admins/login.html")

def log_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        var1 = Login.objects.get(username=username, password=password)
        request.session['lid']=var1.id

        if var1.type=='admin':
            return redirect('/myapp/admins_home/')
        elif var1.type=='driver':
            dd=Driver.objects.get(LOGIN__id=request.session['lid'])
            dname=dd.name
            request.session['dname']=dname
            dphoto=dd.photo
            request.session['dphoto'] = dphoto
            return redirect('/myapp/driverhome/')

        elif var1.type=='user':
            uu = User.objects.get(LOGIN__id = request.session['lid'])
            uname = uu.name
            request.session['uname'] = uname
            uphoto = uu.photo
            request.session['uphoto'] = uphoto
            return redirect('/myapp/uhome/')

        elif var1.type=='mechanic':
            mm = Mechanic.objects.get(LOGIN__id=request.session['lid'])
            mname = mm.name
            request.session['mname'] = mname
            mphoto = mm.photo
            request.session['mphoto'] = mphoto
            return redirect('/myapp/mhome/')
        else:
            return HttpResponse('''<script>alert("No user found. Invalid username or password");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("No user found. Invalid username or password");window.location="/myapp/login/"</script>''')



def home(request):

    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:

        return render(request, "admins/home.html")


def mhome(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "mechanic/index.html")



def admins_add_driver(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "admins/add_driver.html")


def admins_add_driver_post(request):
    name= request.POST["textfield"]
    gender= request.POST["select"]
    housename= request.POST["textfield2"]
    place= request.POST["textfield3"]
    city= request.POST["textfield4"]
    state= request.POST["textfield5"]
    email= request.POST["textfield6"]
    phone= request.POST["textfield7"]
    file= request.FILES["fileField"]
    import random

    fs= FileSystemStorage()
    from datetime import  datetime
    filename= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs.save(filename,file)

    l=Login()
    l.username= email
    l.password = str(random.randint(1000000,900000000))
    l.type="driver"
    l.save()

    cobj=Driver()
    cobj.name=name
    cobj.gender= gender
    cobj.housename=housename
    cobj.place=place
    cobj.email=email
    cobj.city= city
    cobj.state=state
    cobj.phone=phone
    cobj.LOGIN=l
    cobj.photo= fs.url(filename)
    cobj.save()

    return HttpResponse("<script>alert('Driver added successfully');window.location='/myapp/admins_add_driver/'</script>")





def admins_add_mechanic(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "admins/add_mechanic.html")

def admins_add_mechanic_post(request):
    name= request.POST["textfield"]
    gender= request.POST["select"]
    housename= request.POST["textfield2"]
    place= request.POST["textfield3"]
    city= request.POST["textfield4"]
    state= request.POST["textfield5"]
    email= request.POST["textfield6"]
    phone= request.POST["textfield7"]
    file= request.FILES["fileField"]
    import random

    fs= FileSystemStorage()
    from datetime import  datetime
    filename= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs.save(filename,file)

    l=Login()
    l.username= email
    l.password = str(random.randint(1000000,900000000))
    l.type="mechanic"
    l.save()

    cobj=Mechanic()
    cobj.name=name
    cobj.gender= gender
    cobj.housename=housename
    cobj.place=place
    cobj.email=email
    cobj.city= city
    cobj.state=state
    cobj.phone=phone
    cobj.LOGIN=l
    cobj.photo= fs.url(filename)
    cobj.save()

    return HttpResponse("<script>alert('Mechanic added successfully');window.location='/myapp/admins_add_driver/'</script>")



















############### service  mngmnt ###############################

def add_scategory(request):
    return render(request,"admins/addservicecategory.html")


def add_scategory_post(request):
    scategory=request.POST['textfield']
    ss=Service_category()
    ss.sname=scategory
    ss.save()
    return  HttpResponse("<script>alert('added successfully');window.location='/myapp/add_scategory/'</script>")


def admin_view_servicecategory(request):
    res=Service_category.objects.all()
    return render(request,"admins/ViewCategory.html",{"data":res})



def admin_view_servicecategory_post(request):
    sname=request.POST['textfield']
    res=Service_category.objects.filter(sname__icontains=sname)
    return render(request, "admins/ViewCategory.html", {"data": res})



def delete_category(request,id):
    d=Service_category.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Delete successfully');window.location='/myapp/admin_view_servicecategory/'</script>")


def add_services(request):
    res=Service_category.objects.all()
    return render(request,"admins/add_service.html",{"data":res})

def add_services_post(request):
    sname=request.POST['textfield']
    amount=request.POST['textfield1']
    details=request.POST['textfield2']
    photo=request.FILES['file']
    cat=request.POST['select2']

    fs = FileSystemStorage()
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(filename, photo)

    sobj=Service()
    sobj.servicename=sname
    sobj.amount=amount
    sobj.details=details
    sobj.photo=fs.url(filename)
    sobj.CATEGORY_id=cat
    sobj.save()
    return HttpResponse(
        "<script>alert('Service added successfully');window.location='/myapp/add_services/'</script>")



def admin_view_service(request):
    res=Service.objects.all()
    return render(request,"admins/ViewService.html",{"data":res})

def admin_view_service_post(request):
    sname=request.POST['textfield']
    res=Service.objects.filter(servicename__icontains=sname)
    return render(request,"admins/ViewService.html",{"data":res})



def edit_services(request,id):
    res=Service_category.objects.all()
    res1 = Service.objects.get(id=id)
    return render(request,"admins/edit_service.html",{"data":res,"data1":res1})

def edit_services_post(request):
    sname=request.POST['textfield']
    amount=request.POST['textfield1']
    details=request.POST['textfield2']
    cat=request.POST['select2']
    id=request.POST['id']
    sobj = Service.objects.get(id=id)
    if 'file' in request.FILES:
        photo = request.FILES['file']

        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, photo)
        sobj.photo = fs.url(filename)
        sobj.save()
    sobj.servicename=sname
    sobj.amount=amount
    sobj.details=details
    sobj.CATEGORY_id=cat
    sobj.save()
    return HttpResponse(
        "<script>alert('Service Update successfully');window.location='/myapp/admin_view_service/'</script>")


def delete_service(request,id):
    d=Service.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Delete successfully');window.location='/myapp/admin_view_service/'</script>")






def driver_view_servicecategory(request):
    res=Service_category.objects.all()
    return render(request,"driver/ViewCategory.html",{"data":res})



def driver_view_servicecategory_post(request):
    sname=request.POST['textfield']
    res=Service_category.objects.filter(sname__icontains=sname)
    return render(request, "driver/ViewCategory.html", {"data": res})




def driver_view_service(request,id):
    res=Service.objects.filter(CATEGORY__id=id)
    return render(request,"driver/ViewService.html",{"data":res})

def driver_view_service_post(request):
    sname=request.POST['textfield']
    res=Service.objects.filter(servicename__icontains=sname)
    return render(request,"driver/ViewService.html",{"data":res})


def addtocart(request,sid):

    did=request.session['lid']

    obj=servicecart()
    obj.SERVICE_id=sid
    obj.DRIVER=Driver.objects.get(LOGIN__id=did)
    obj.save()
    return HttpResponse(
        "<script>alert('Request Sending Successfully');window.location='/myapp/driver_view_servicecategory/'</script>")


def view_cart(request):
    res=servicecart.objects.filter(DRIVER__LOGIN__id=request.session['lid'])
    return render(request,"driver/ViewCart.html",{"data":res})

def delete_cart(request,id):
    res = servicecart.objects.get(id=id)
    res.delete()
    return HttpResponse(
        "<script>alert('Cart Deleted Successfully');window.location='/myapp/view_cart/'</script>")


def driver_sendrequest(request):

    res = servicecart.objects.filter(DRIVER__LOGIN_id=request.session['lid'])
    boj = Service_request()
    boj.DRIVER = Driver.objects.get(LOGIN_id=request.session['lid'])
    # t=i.amount*i.qty
    boj.amount = 0
    import datetime
    boj.date = datetime.datetime.now().date().today()
    boj.status = "pending"
    # boj = Stock.objects.get(PRODUCT_id=[0])
    boj.save()
    for i in res:
            print(i)

            # print(boj,"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            # mytotal = 0
            # st = 0

                # print(j)
            bs = Service_request_sub()
            bs.SERVICEREQUEST_id = boj.id
            bs.SERVICE_id = i.SERVICE.id
            bs.save()
            from django.db.models import Sum
            aa=Service_request_sub.objects.filter(SERVICEREQUEST__DRIVER__LOGIN__id=request.session['lid']).annotate(total_amount=Sum('SERVICE__amount'))

            mytotal=aa
            print(mytotal)

                # stock+=(float (int(j.Stock.PRODUCT))-int(j.quantity))

            # print(mytotal)
            # print(stock)
    # servicecart.objects.filter(DRIVER__LOGIN_id=request.session['lid']).delete()



    # print(boj)
    # boj = Service_request.objects.get(id=boj.id)
    # boj.amount = mytotal
    # boj.save()
    #
    # res = servicecart.objects.filter(DRIVER__LOGIN__id=request.session['lid'])
    #
    # for i in res:
    #     print(i)
    #     res2 = servicecart.objects.filter(USER__LOGIN_id=request.session['lid'])
    #     print(res2, "hiii")
    #
    #     boj = Service_request()
    #     boj.DRIVER= Driver.objects.get(LOGIN_id=request.session['lid'])
    #     # t=i.amount*i.qty
    #     boj.amount = 0
    #     import datetime
    #     boj.date = datetime.datetime.now().date().today()
    #     # boj = Stock.objects.get(PRODUCT_id=[0])
    #     boj.save()
    #     # res3 =
    #     mytotal = 0
    #     st = 0
    #         # print(j)
    #     bs = Service_request_sub()
    #     bs.SERVICEREQUEST_id = boj.id
    #     bs.SERVICE_id = j.SERVICE.id
    #     bs.save()
    #     ab=service_totals = Service_request_sub.objects.filter(SERVICEREQUEST__DRIVER__LOGIN__id=request.session['lid']).annotate(total_amount=Sum('SERVICE__amount'))
    #     mytotal = ab.total_amount
    #     print(mytotal)
    #     boj = Service_request.objects.get(id=boj.id)
    #     boj.amount = mytotal
    #     boj.save()
    return HttpResponse("<script>alert('Request Sending Successfully');window.location='/myapp/view_cart/'</script>")


def admin_view_request(request):
    res=Service_request.objects.filter(status="pending")
    return render(request,"admins/ViewService_request.html",{"data":res})

def admin_view_request_post(request):
    fd=request.POST['textfield']
    td=request.POST['textfield2']
    res=Service_request.objects.filter(status="pending",date__range=[fd,td])
    return render(request,"admins/ViewService_request.html",{"data":res})

def admin_view_request_more(request,oid):
    # oid=request.session['oid']
    res=Service_request_sub.objects.filter(SERVICEREQUEST__id=oid)
    print(res,"haii")
    return render(request,"admins/ViewService_request_more.html",{"data":res})

def admin_view_request_approved(request):
    res=Service_request.objects.filter(status="approved")
    return render(request,"admins/ViewService_request_accepted.html",{"data":res})

def admin_view_request_post_approved(request):
    fd=request.POST['textfield']
    td=request.POST['textfield2']
    res=Service_request.objects.filter(status="approved",date__range=[fd,td])
    return render(request, "admins/ViewService_request_accepted.html", {"data": res})



def admin_view_request_more_approved(request,id):
    # oid=request.session['oid']
    res=Service_request_sub.objects.filter(SERVICEREQUEST__id=id)
    print(res,"haii")
    return render(request,"admins/ViewService_request_more.html",{"data":res})

def driver_view_request_approved(request):
    res=Service_request.objects.filter(DRIVER__LOGIN__id=request.session['lid'])
    return render(request,"driver/ViewService_request_accepted.html",{"data":res})

def driver_view_request_post_approved(request):
    fd=request.POST['textfield']
    td=request.POST['textfield2']
    res=Service_request.objects.filter(DRIVER__LOGIN__id=request.session['lid'],date__range=[fd,td])
    return render(request, "driver/VViewService_request_accepted.html", {"data": res})

def driver_view_request_more_approved(request,oid):
    # oid=request.session['oid']
    res=Service_request_sub.objects.filter(SERVICEREQUEST__id=oid)
    print(res,"haii")
    return render(request,"admins/ViewService_request_more_approved.html",{"data":res})


# def driver_view_request_more(request):
#     # oid=request.session['oid']
#     res=Service_request_sub.objects.filter(SERVICEREQUEST__DRIVER__LOGIN__id=request.session['lid'])
#     print(res,"haii")
#     return render(request,"driver/ViewService_request_more_approved.html",{"data":res})









def admin_accept_request(request,id):
    res=Service_request.objects.filter(id=id).update(status="approved")
    return HttpResponse(
        "<script>alert('Approved Successfully');window.location='/myapp/admin_view_service/'</script>")

def admin_reject_request(request,id):
    res=Service_request.objects.filter(id=id).update(status="rejected")
    return HttpResponse(
        "<script>alert('Rejected Successfully');window.location='/myapp/admin_view_service/'</script>")


def admin_view_request_accepted(request):
    res = Service_request.objects.filter(status="approved")
    return render(request, "admins/ViewService_request_accepted.html", {"data": res})


def admin_view_request_post_accepted(request):
    fd = request.POST['textfield']
    td = request.POST['textfield2']
    res = Service_request.objects.filter(status="approved", date__range=[fd, td])
    return render(request, "admins/ViewService_request_accepted.html", {"data": res})



def driver_view_request_status(request):
    res=Service_request.objects.filter(DRIVER__LOGIN__id=request.session['lid'])
    return render(request,"driver/View_request_status.html",{"data":res})


#########################################################################


def admins_view_mechanic(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')
    else:
        cl = Mechanic.objects.all()
        return render(request, "admins/ViewMechanic.html", {'data': cl})



def admins_view_mechanic_post(request):

    s=request.POST["textfield"]
    cl = Mechanic.objects.filter(name__icontains=s)

    return render(request, "admins/ViewMechanic.html", {'data': cl})


def admins_delete_mechanic(request, id):
    Mechanic.objects.get(id=id).delete()

    return HttpResponse("<script>alert('Mechanic  deleted successfully');window.location='/myapp/admins_view_mechanic/'</script>")


def admins_edit_mechanic(request, id):
    c=Mechanic.objects.get(id=id)

    return render(request, "admins/edit_mechanic.html", {'data': c})

def admins_edit_mechanic_post(request):
    id = request.POST["id"]
    name = request.POST["textfield"]
    gender = request.POST["select"]
    housename = request.POST["textfield2"]
    place = request.POST["textfield3"]
    city = request.POST["textfield4"]
    state = request.POST["textfield5"]
    email = request.POST["textfield6"]
    phone = request.POST["textfield7"]

    cobj = Mechanic.objects.get(id=id)
    cobj.name = name
    cobj.gender = gender
    cobj.housename = housename
    cobj.place = place
    cobj.email = email
    cobj.city = city
    cobj.state = state
    cobj.phone = phone

    if 'fileField' in request.FILES:
        import random
        file = request.FILES["fileField"]
        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, file)
        cobj.photo = fs.url(filename)

    cobj.save()

    return HttpResponse("<script>alert('Mechanic edited successfully');window.location='/myapp/admins_view_mechanic/'</script>")









def admins_view_driver(request):

    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        cl = Driver.objects.all()

        return render(request, "admins/Viewdriver.html", {'data': cl})


def admins_view_driver_post(request):

    s=request.POST["textfield"]
    cl = Driver.objects.filter(name__icontains=s)

    return render(request, "admins/Viewdriver.html", {'data': cl})
def admins_delete_driver(request, id):
    Driver.objects.get(id=id).delete()

    return HttpResponse("<script>alert('Driver  deleted successfully');window.location='/myapp/admins_view_driver/'</script>")
def admins_edit_driver(request, id):
    c=Driver.objects.get(id=id)

    return render(request, "admins/edit_driver.html", {'data': c})
def admins_edit_driver_post(request):
    id = request.POST["id"]
    name = request.POST["textfield"]
    gender = request.POST["select"]
    housename = request.POST["textfield2"]
    place = request.POST["textfield3"]
    city = request.POST["textfield4"]
    state = request.POST["textfield5"]
    email = request.POST["textfield6"]
    phone = request.POST["textfield7"]

    cobj = Driver.objects.get(id=id)
    cobj.name = name
    cobj.gender = gender
    cobj.housename = housename
    cobj.place = place
    cobj.email = email
    cobj.city = city
    cobj.state = state
    cobj.phone = phone

    if 'fileField' in request.FILES:
        import random
        file = request.FILES["fileField"]
        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, file)
        cobj.photo = fs.url(filename)

    cobj.save()

    return HttpResponse("<script>alert('Clerk added successfully');window.location='/myapp/admins_view_driver/'</script>")



def admin_addvehicle(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return  render(request,"admins/add_vehicle.html")

def admin_addvehicle_post(request):
    regno= request.POST["textfield"]
    model= request.POST["textfield1"]
    engineno= request.POST["textfield2"]
    totalseat= request.POST["textfield3"]
    ac= request.POST["select"]
    vehicletype= request.POST["select2"]
    file= request.FILES["file"]




    v=Vehicle()
    v.vehicleregno= regno
    v.vehiclemodel= model
    v.enginenumber= engineno
    v.ac_nonac=ac
    v.totalseats= totalseat
    v.vehicletype= vehicletype
    fs = FileSystemStorage()
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(filename, file)


    v.photo= fs.url(filename)

    file1 = request.FILES["file1"]
    fs = FileSystemStorage()
    from datetime import datetime
    filename = "fff" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(filename, file1)

    v.rcfile= fs.url(filename)
    v.save()
    return  HttpResponse("<script>alert('Vehicle added successfully');window.location='/myapp/admin_addvehicle/'</script>")

def admin_view_vehicle(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        allveh= Vehicle.objects.all()
        return render(request,"admins/Viewvehicle.html",{'data': allveh})

def admin_view_vehicle_post(request):
    s=request.POST["textfield"]
    allveh= Vehicle.objects.filter(vehicleregno__icontains=s)
    return render(request,"admins/Viewvehicle.html",{'data': allveh})

def admin_delete_vehicles(request,vid):
    Vehicle.objects.filter(id=vid).delete()
    return HttpResponse(
        "<script>alert('Vehicle delete successfully');window.location='/myapp/admin_view_vehicle/'</script>")

def admin_edit_vehicles(request,id):
    s= Vehicle.objects.get(id=id)
    return render(request, "admins/edit_vehicle.html", {'data': s})


def admin_editvehicle_post(request):
    id= request.POST["id"]
    regno= request.POST["textfield"]
    model= request.POST["textfield1"]
    engineno= request.POST["textfield2"]
    totalseat= request.POST["textfield3"]
    ac= request.POST["select"]
    vehicletype= request.POST["select2"]


    v=Vehicle.objects.get(id=id)
    v.vehicleregno= regno
    v.vehiclemodel= model
    v.enginenumber= engineno
    v.ac_nonac=ac
    v.totalseats= totalseat
    v.vehicletype= vehicletype

    if 'file' in request.FILES:

        file = request.FILES["file"]
        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, file)
        v.photo= fs.url(filename)
    v.save()
    return  HttpResponse("<script>alert('Vehicle edietd successfully');window.location='/myapp/admin_view_vehicle/'</script>")


def admins_view_complaints(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        c=Complaint.objects.all()
        return render(request, "admins/Viewcomplaint.html", {'data': c})



def admins_view_complaints_post(request):
    f=request.POST["f"]
    t=request.POST["t"]
    c = Complaint.objects.filter(date__range=[f,t])
    return render(request, "admins/Viewcomplaint.html", {'data': c})

def admins_sent_reply(request,id):
    return render(request,"admins/sentreply.html",{'id':id})

def admins_sent_reply_post(request):
    id= request.POST["id"]
    reply= request.POST["reply"]
    c=Complaint.objects.get(id=id)
    c.reply= reply
    c.status="replied"
    c.save()
    return HttpResponse("<script>alert('Replied successfully');window.location='/myapp/admins_view_complaints/'</script>")



def admin_change_password(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "admins/change password.html")

def admin_changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res=Login.objects.filter(password=currentpassword,id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword==confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else :
            return HttpResponse('''<script>alert("Password mismatch");window.location="/myapp/login/"</script>''')
    else :
        return HttpResponse('''<script>alert("Invalid password. Please try again");window.location="/myapp/login/"</script>''')


def admin_car_driver_assign(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:

        v=Vehicle.objects.all()
        s=[]

        for i in v:

            if not Carassign.objects.filter(VEHICLE=i).exists():
                s.append(i)

        v=s



        d=Driver.objects.all()
        s = []
        for i in d:
            if not Carassign.objects.filter(DRIVER=i).exists():
                s.append(i)

        d=s





        return render(request,"admins/car_assign.html",{ 'v':v, 'd':d })





def admin_car_driver_assign_post(request):
    car= request.POST["car"]
    driver= request.POST["driver"]

    c=Carassign()
    c.VEHICLE_id= car
    c.DRIVER_id=driver
    c.save()

    return HttpResponse("<script>alert('Car Assigned successfully');window.location='/myapp/admin_car_driver_assign/'</script>")



def admin_view_car_driver_assign(request):

    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        a=Carassign.objects.all()

        return render(request,"admins/viewcar_driver_assign.html", {'data': a})




def admin_view_car_driver_assign_post(request):
    a=Carassign.objects.filter()

    return render(request,"admins/viewcar_driver_assign.html", {'data': a})



def admin_delete_car_assign(request,id):

    Carassign.objects.filter(id=id).delete()
    return HttpResponse(
        "<script>alert('Assignment deleted successfully');window.location='/myapp/admin_view_car_driver_assign/'</script>")


def admin_view_users(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')
    else:
        u=User.objects.all()
        return  render(request,"admins/Viewuser.html",{'data': u})


def admin_view_users_post(request):


    name= request.POST["textfield"]

    u=User.objects.filter(name__icontains=name)

    return  render(request,"admins/Viewuser.html",{'data': u})



##################user portion

def uhome(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request,"user/home.html")

def user_signup(request):
    return render(request, "user/signup.html")


def user_signup_post(request):
    name = request.POST["textfield"]
    gender = request.POST["select"]
    housename = request.POST["textfield2"]
    place = request.POST["textfield3"]
    city = request.POST["textfield4"]
    state = request.POST["textfield5"]
    email = request.POST["textfield6"]
    phone = request.POST["textfield7"]

    password = request.POST["textfield10"]
    file = request.FILES["fileField"]
    fs = FileSystemStorage()
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(filename, file)
    l = Login()
    l.username = email
    l.password= password
    l.type = "user"
    l.save()

    cobj = User()
    cobj.name = name
    cobj.gender = gender
    cobj.housename = housename
    cobj.place = place
    cobj.email = email
    cobj.city = city
    cobj.state = state
    cobj.phone = phone
    cobj.LOGIN = l
    cobj.photo = fs.url(filename)
    cobj.save()
    return HttpResponse("<script>alert('Account created successfully');window.location='/myapp/login/'</script>")













def user_view_profile(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')
    else:
        u = User.objects.get(LOGIN__id=request.session['lid'])
        return render(request, "user/viewprofile.html", {'u': u})


def user_edit_profile(request):
    u = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request, "user/editprofile.html", {'data': u})



def user_editprofile_post(request):
    name = request.POST["textfield"]
    gender = request.POST["select"]
    housename = request.POST["textfield2"]
    place = request.POST["textfield3"]
    city = request.POST["textfield4"]
    state = request.POST["textfield5"]
    email = request.POST["textfield6"]
    phone = request.POST["textfield7"]


    cobj = User.objects.get(LOGIN_id=request.session['lid'])
    cobj.name = name
    cobj.gender = gender
    cobj.housename = housename
    cobj.place = place
    cobj.email = email
    cobj.city = city
    cobj.state = state
    cobj.phone = phone

    if 'fileField' in request.FILES:
        file = request.FILES["fileField"]

        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, file)


    cobj.save()

    return HttpResponse("<script>alert('Account edited successfully');window.location='/myapp/user_view_profile/'</script>")


def user_add_complaint(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request,"user/sentcomplaint.html")
def user_add_complaint_post(request):
    complaint= request.POST["complaint"]

    c=Complaint()
    c.USER= User.objects.get(LOGIN_id= request.session['lid'])
    c.complaint=complaint
    c.reply="pending"
    c.status="pending"
    c.date=datetime.now()
    c.save()





    return HttpResponse("<script>alert('Complaint sent successfully');window.location='/myapp/user_add_complaint/'</script>")




def user_view_complaint(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        fall = Complaint.objects.filter(USER__LOGIN_id= request.session['lid'])
        return render(request, "user/Viewcomplaint.html", {'fall': fall})

def user_view_complaint_post(request):

    f=request.POST["f"]
    t=request.POST["t"]

    fall = Complaint.objects.filter(USER__LOGIN_id= request.session['lid'], date__range=[f,t])
    return render(request, "user/Viewcomplaint.html", {'fall': fall})



def user_view_cabs_post(request):

    totalseats=request.POST["textfield3"]
    vehicletype=request.POST["select2"]
    acstatus=request.POST["select"]

    v=Vehicle.objects.filter(Q(totalseats=totalseats) & Q(vehicletype=vehicletype) & Q(ac_nonac=acstatus))

    return render(request,"user/Viewvehicle.html", {'data': v })



def user_view_cabs(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        v=Vehicle.objects.all()
        return render(request,"user/Viewvehicle.html", {'data': v })


def user_booking(request,vid):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:

        return render(request,"user/booking.html",{'vid':vid})

def user_booking_post(request):
    pickup=request.POST["textfield"]
    drop=request.POST["textfield2"]
    vid=request.POST["vid"]
    # time=request.POST["textfield3"]




    bobj= booking()
    bobj.USER= User.objects.get(LOGIN_id= request.session['lid'])
    bobj.date= datetime.now()
    bobj.pick= pickup
    bobj.drop= drop
    bobj.VEHICLE_id=vid
    bobj.status="booked"
    bobj.time=datetime.now().time().strftime("%H:%M:%S")
    # bobj.time=datetime.now().time()
    bobj.save()

    return HttpResponse("<script>alert('Cab booking done successfully');window.location='/myapp/user_view_cabs/'</script>")







def userpayment(request,bid,totalkm):

    amount= 15 * float(totalkm) * 100
    request.session["id"]=bid
    return redirect('/myapp/raz_pay/'+str(amount))

    # return render(request,"user/pay.html",{'bid':bid, 'amount': amount})

def userpayment_post(request):

    id = request.session["id"]



    bobj = booking.objects.get(id=id)

    bobj.status = "paid"

    bobj.save()

    return HttpResponse(
        "<script>alert('Payment done successfully');window.location='/myapp/user_view_booking/'</script>")


def user_change_password(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "user/change password.html")

def user_changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword == confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(
                password=confirmpassword)
            return HttpResponse(
                '''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Password mismatch");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("Invalid password");window.location="/myapp/login/"</script>''')



def user_view_booking(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        res= booking.objects.filter(USER__LOGIN_id= request.session['lid'])

        return  render(request,"user/view_booking.html",{'data': res})




def user_view_booking_post(request):

    f= request.POST["f"]
    t= request.POST["t"]
    res= booking.objects.filter(USER__LOGIN_id= request.session['lid'], date__range=[f,t])

    return  render(request,"user/view_booking.html",{'data': res})







##############driver

def driverhome(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request,"driver/home.html")




def driver_view_profile(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        print(request.session['lid'],"HIHIHIHHIHII")
        u = Driver.objects.get(LOGIN_id=request.session['lid'])
        return render(request, "driver/viewprofile.html", {'u': u})




def driver_view_booking_new(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        s= Carassign.objects.filter(DRIVER__LOGIN_id= request.session['lid'])
        if s.exists():
            s=s[0]
            s=booking.objects.filter(VEHICLE= s.VEHICLE)


            return render(request,"driver/view_booking_new.html", {'data': s})

        else:
            return HttpResponse(
                '''<script>alert("You have no vehicle assigned");window.location="/myapp/driverhome/"</script>''')



def driver_view_booking_new_post(request):

    f=request.POST["f"]
    t=request.POST["t"]
    s= Carassign.objects.filter(DRIVER__LOGIN_id= request.session['lid'])
    if s.exists():
        s=s[0]
        s=booking.objects.filter(VEHICLE= s.VEHICLE, date__range=[f,t])


        return render(request,"driver/view_booking_new.html", {'data': s})

    else:
        return HttpResponse(
            '''<script>alert("You have no vehicle assigned");window.location="/myapp/driverhome/"</script>''')




def driver_picked(request,id):

    b=booking.objects.get(id=id)
    b.status="picked"
    b.save()

    return HttpResponse(
        '''<script>alert("Picked");window.location="/myapp/driver_view_booking_new/"</script>''')



def driver_cancelled(request,id):

    b=booking.objects.get(id=id)
    b.status="cancelled"
    b.save()

    return HttpResponse(
        '''<script>alert("Picked");window.location="/myapp/driver_view_booking_new/"</script>''')



def driver_dropped(request):

    id= request.POST["iid"]
    total= request.POST["total"]

    b=booking.objects.get(id=id)
    b.status="dropped"
    b.total_km= total
    b.save()

    return HttpResponse(
        '''<script>alert("Dropped");window.location="/myapp/driver_view_booking_new/"</script>''')


def driver_change_password(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "driver/change password.html")

def driver_changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword == confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(
                password=confirmpassword)
            return HttpResponse(
                '''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Password mismatch");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("Invalid password");window.location="/myapp/login/"</script>''')







# def email_exist(request):
#     email_ex = request.POST['email']
#     if User.objects.filter(email=email_ex).exists():
#         return JsonResponse({'status':'ok'})
#     else:
#         return JsonResponse({'status':'no'})

def forget_password(request):
    return render(request,'forgotpassword.html')

def forget_password_post(request):
    em = request.POST['textfield2']
    import random
    password = random.randint(00000000, 99999999)
    log = Login.objects.filter(username=em)
    if log.exists():
        logg = Login.objects.get(username=em)
        message = 'temporary password is ' + str(password)
        send_mail(
            'temp password',
            message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.password = password
        logg.save()
        return HttpResponse('<script>alert("success");window.location="/myapp/login/"</script>')
    else:
        return HttpResponse('<script>alert("invalid email");window.location="/myapp/login/"</script>')


def user_cancelled(request,id):

    b=booking.objects.get(id=id)
    b.status="cancelled"
    b.save()

    return HttpResponse(
        '''<script>alert("Cancelled");window.location="/myapp/user_view_booking/"</script>''')



def raz_pay(request,amount):

    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amount= float(amount)

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'user/pp.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id']})



def get_vehicles(request):
    department_id = request.GET.get('department_id')
    datas = Vehicle.objects.filter(vehicletype=department_id)
    data=[]
    for i in datas:
        data.append({
            'vehicleregno':i.vehicleregno,
            'vehiclemodel':i.vehiclemodel,
            'enginenumber':i.enginenumber,
            'totalseats':i.totalseats,
            'ac_nonac':i.ac_nonac,
            'vehicletype':i.vehicletype,
            'photo':i.photo,
            'rcfile':i.rcfile,
            'id':i.id,

        })
    return JsonResponse(data,safe=False)


def sa(request):
    return render(request,"sa.html")




def mechanic_view_request_approved(request):
    res=Service_request.objects.filter(status="approved")
    return render(request,"mechanic/ViewService_request.html",{"data":res})

def mechanic_view_request_post_approved(request):
    fd=request.POST['textfield']
    td=request.POST['textfield2']
    res=Service_request.objects.filter(status="approved",date__range=[fd,td])
    return render(request, "mechanic/ViewService_request.html", {"data": res})



def mechanic_view_request_more_approved(request,oid):
    # oid=request.session['oid']
    res=Service_request_sub.objects.filter(SERVICEREQUEST__id=oid)
    print(res,"haii")
    return render(request,"mechanic/ViewService_request_more.html",{"data":res})

def total_calculate(request):
    oid = request.POST.get('oid', None)
    amount=request.POST['textfield2']
    if oid is not None:
        # Fetch total amount for the given service request ID
        total_amount = Service_request_sub.objects.filter(SERVICEREQUEST__id=oid).aggregate(
            total_amount=Sum('SERVICE__amount'))

        # Access the total amount
        total_amount_value = total_amount.get('total_amount') if total_amount.get('total_amount') else 0

        print(total_amount_value, "=======================")

        tt=total_amount_value+float(amount)

        print(tt)


        rr=Service_request.objects.filter(id=oid).update(amount=tt)
        # Now you have the total amount for the given service request ID
        # You can use it as required, maybe store it in the session or pass it to a template

    return HttpResponse('''<script>alert("Successfull");window.location="/myapp/mhome/"</script>''')


from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

def generate_pdf_bill(request, oid):
    # Fetch data from models
    service_request = Service_request.objects.get(id=oid)
    service_request_subs = Service_request_sub.objects.filter(SERVICEREQUEST=service_request)

    # Create a PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill.pdf"'

    # Create a PDF document using ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Add title
    title = "Bill\n\n"
    elements.append(Paragraph(title))

    # Add service request details
    data = [
        ["Service Request ID:", str(service_request.id)],
        ["Name:", service_request.DRIVER.name],
        ["Amount:", service_request.amount],
        ["Status:", service_request.status],
        ["Date:", str(service_request.date)]
    ]
    table = Table(data, colWidths=[150, 300])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    # Add service request subs details
    sub_data = [["Service", "Amount"]]
    for sub in service_request_subs:
        sub_data.append([sub.SERVICE.servicename, sub.SERVICE.amount])
    sub_table = Table(sub_data, colWidths=[200, 150])
    sub_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(sub_table)

    # Build PDF document
    doc.build(elements)

    return response

def mechanic_view_profile(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        print(request.session['lid'],"HIHIHIHHIHII")
        u = Mechanic.objects.get(LOGIN_id=request.session['lid'])
        return render(request, "mechanic/viewprofile.html", {'u': u})


def mechanic_change_password(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "mechanic/change password.html")

def mechanic_changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword == confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(
                password=confirmpassword)
            return HttpResponse(
                '''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Password mismatch");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("Invalid password");window.location="/myapp/login/"</script>''')

