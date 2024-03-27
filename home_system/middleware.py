from django.utils import timezone
from django.contrib.sessions.middleware import SessionMiddleware
import json
from datetime import datetime
from django.utils import timezone

### MIDDLEWARE PARA CERRA SESION DESPUES DE CIERTO TIEMPO DE INACTIVIDAD ####

class SessionTimeoutMiddleware(SessionMiddleware):
    def process_request(self, request):
        super().process_request(request)
        
        # Obtener la marca de tiempo de la última actividad del usuario
        last_activity_str = request.session.get('last_activity')
        if last_activity_str:
            # Convertir la cadena de fecha en formato ISO 8601 a objeto datetime
            last_activity = datetime.strptime(last_activity_str, '%Y-%m-%dT%H:%M:%S.%f%z')
            session_age = request.session.get_expiry_age()
            expiration_time = last_activity + timezone.timedelta(seconds=session_age)
            if timezone.now() > expiration_time:
                # Si ha pasado más tiempo del definido en SESSION_COOKIE_AGE desde la última actividad, cerrar la sesión
                request.session.flush()

        # Actualizar la marca de tiempo de la última actividad del usuario
        request.session['last_activity'] = timezone.now().isoformat()