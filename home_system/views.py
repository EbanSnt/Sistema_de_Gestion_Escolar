from django.shortcuts import render,redirect
from .models import ActionsHistory,Attendances,Grades,SchoolInformation,SchoolStaff,SchoolUsers,SchoolYear,StudentFile,Students,StudentsPayments,Subjects
import datetime

### TEMPLATES "LOGIN, SIGN UP, HOME Y PERMISSION DENNIED" ###

def login(request):
    return render(request,"login.html")


def sign_up(request):
    return render(request,"sign_up.html")


def home(request):
    if request.session['active'] == True:
        return render(request,"home.html")
    else:
        return redirect("permision_dennied_login")


def permision_dennied(request):
    return render(request,"permision_dennied.html")


def permision_dennied_login(request):
    return render(request,"permision_dennied_login.html")

### CREATE USER #### Solo se crea. El admin solo puede modificar y eliminar los datos

def create_user(request):
    try:
        if request.method == "POST":
            dni = int(request.POST["dni"])
            username = request.POST["username"]
            password = request.POST["password"]
            email = request.POST["email"]

            SchoolUsers.objects.create(dni=dni,username=username,password=password,email=email)

            details = f"Creacion de usuario\nNombre: {username}. DNI: {dni}. Email: {email}"

            ActionsHistory.objects.create(date=datetime.datetime.now(),details=details,action_type="Creacion de Usuario")
            return redirect("login.html")
        else:
            return render(request,"sign_up.html")
    except:
        return render(request,"sign_up.html")
        
### Todos los "CREATE"

def create_school_information(request):
    """Se sube la informacion de la escuela"""
    try:
        if request.session['active'] == True:
            if request.session['position'] == "admin":
                if request.method == "POST":
                    school_logo = request.FILES.get("school_logo")
                    name = request.POST["name"]
                    address = request.POST["address"]
                    district = request.POST["district"]
                    locality = request.POST["telephone_number"]
                    telephone_number = request.POST["telephone_number"]
                    telephone_number2 = request.POST["telephone_number2"]
                    telephone_number3 = request.POST["telephone_number3"]
                    telephone_number4 = request.POST["telephone_number4"]
                    email = request.POST["email"]
                    alternative_email = request.POST["alternative_email"]
                    school_type = request.POST["school_type"]
                    facebook = request.POST["facebook"]
                    instagram = request.POST["instagram"]
                    twitter_x = request.POST["twitter_x"]
                    linkedin = request.POST["linkedin"]
                    youtube = request.POST["youtube"]
                    telegram = request.POST["telegram"]
                    whatsapp = request.POST["whatsapp"]
                    web_site = request.POST["web_site"]

                    SchoolInformation.objects.create(school_logo=school_logo,name=name,address=address,district=district,locality=locality,telephone_number=telephone_number,telephone_number2=telephone_number2,telephone_number3=telephone_number3,telephone_number4=telephone_number4,email=email,alternative_email=alternative_email,school_type=school_type,facebook=facebook,instagram=instagram,twitter_x=twitter_x,linkedin=linkedin,youtube=youtube,telegram=telegram,whatsapp=whatsapp,web_site=web_site)

                    details = {"name":name,"address":address,"district":district,"locality":locality,"telephone_number":telephone_number,"telephone_number2":telephone_number2,"telephone_number3":telephone_number3,"telephone_number4":telephone_number4,"email":email,"alternative_email":alternative_email,"school_type":school_type,"facebook":facebook,"instagram":instagram,"twitter_x":twitter_x,"linkedin":linkedin,"youtube":youtube,"telegram":telegram,"whatsapp":whatsapp,"web_site":web_site}

                    ActionsHistory.objects.create(date=datetime.datetime.now(),details=details,action_type="Suba de Informacion acerca de la Escuela")

                    return redirect("home")
                else:
                    return render(request,"create_school_information.html")
            else:
                return redirect("permision_dennied_login")      
        else:
            return redirect("permision_dennied")        
    except:
        return render(request,"create_school_information.html")
