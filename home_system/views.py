from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.sessions.middleware import SessionMiddleware
from .models import ActionsHistory,Attendances,Grades,SchoolInformation,SchoolStaff,SchoolUsers,SchoolYear,StudentFile,Students,StudentsPayments,Subjects
import datetime


### MIDDLEWARE PARA CERRA SESION DESPUES DE CIERTO TIEMPO DE INACTIVIDAD ####

class SessionTimeoutMiddleware(SessionMiddleware):
    def process_request(self, request):
        super().process_request(request)
        
        # Obtener la marca de tiempo de la última actividad del usuario
        last_activity = request.session.get('last_activity')
        if last_activity:
            session_age = request.session.get_expiry_age()
            if timezone.now() > last_activity + timezone.timedelta(seconds=session_age):
                # Si ha pasado más tiempo del definido en SESSION_COOKIE_AGE desde la última actividad, cerrar la sesión
                request.session.flush()

        # Actualizar la marca de tiempo de la última actividad del usuario
        request.session['last_activity'] = timezone.now()


### TEMPLATES "LOGIN, SIGN UP, HOME Y PERMISSION DENNIED" ###

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = SchoolUsers.objects.filter(username=username,password=password)
        if user.active == False:
            return render(request,"login.html",{"mensaje":"El usuario no se encuentra activado"})
        elif not user:
            return render(request,"login.html",{"mensaje":"Usuario y/o contraseña incorrecto/s"})
        else:
            request.session['active'] = True
            request.session['username'] = user.username
            request.session['position'] = user.position
            request.session['dni'] = user.dni
            return redirect("home")

    return render(request,"login.html")


def logout_session(request):
    request.session.flush()
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
    """Creacion de un usuario"""
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
        
### SCHOOL INFORMATION ###

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
                return redirect("permision_dennied")    
        else:
            return redirect("permision_dennied_login")   
                   
    except:
        return render(request,"create_school_information.html")
    

def update_school_information(request):
    """Se edita la informacion de la escuela"""
    try:
        if request.session['active'] == True:
            if request.session['position'] == "admin":
                school = SchoolInformation.objects.get(id=1)
                context = {"school":school}
                if request.method == "POST":
                    school.school_logo = request.FILES.get("school_logo")
                    school.name = request.POST["name"]
                    school.address = request.POST["address"]
                    school.district = request.POST["district"]
                    school.locality = request.POST["telephone_number"]
                    school.telephone_number = request.POST["telephone_number"]
                    school.telephone_number2 = request.POST["telephone_number2"]
                    school.telephone_number3 = request.POST["telephone_number3"]
                    school.telephone_number4 = request.POST["telephone_number4"]
                    school.email = request.POST["email"]
                    school.alternative_email = request.POST["alternative_email"]
                    school.school_type = request.POST["school_type"]
                    school.facebook = request.POST["facebook"]
                    school.instagram = request.POST["instagram"]
                    school.twitter_x = request.POST["twitter_x"]
                    school.linkedin = request.POST["linkedin"]
                    school.youtube = request.POST["youtube"]
                    school.telegram = request.POST["telegram"]
                    school.whatsapp = request.POST["whatsapp"]
                    school.web_site = request.POST["web_site"]

                    school.save()
                    details = request.POST.dict()

                    ActionsHistory.objects.create(date=datetime.datetime.now(),details=details,action_type="Modificacion de Informacion de Escuela")
                    return redirect("home")
                else:
                    return render(request,"update_school_information.html",context)
            else:
                return redirect("permision_dennied")  
        else:
            return redirect("permision_dennied_login")  
    except:
        return render(request,"update_school_information.html",context)

