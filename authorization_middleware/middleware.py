from django.urls import reverse
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME


class UserAuthorization:

    def __init__(self, get_response):
        self.get_responce = get_response
        self.login_url = reverse('login_page')
        self.registration_url = reverse('registration_page')
        self.other_guest_user_allowed_urls =[]
        self.unauthenticated_allowed_urls = [self.login_url, self.registration_url] + [reverse(url) for url in self.other_guest_user_allowed_urls]

    def __call__(self, request):
        responce = self.get_responce(request)
        current_url = request.path_info
        if current_url not in self.unauthenticated_allowed_urls:
            if not request.user.is_authenticated:
                path = request.get_full_path()
                return redirect_to_login(path, login_url=self.login_url, redirect_field_name=REDIRECT_FIELD_NAME)
        return responce
   