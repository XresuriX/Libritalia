from django.shortcuts import get_object_or_404
from ninja_extra import NinjaExtraAPI, api_controller, route, permissions, throttle # type: ignore
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from allauth.account.views import SignupView
from django.http import HttpRequest
from .models import User, Profile
from .schemas import UserSchema, UserCreationSchema, ProfileSchema

app = NinjaExtraAPI()

@api_controller('/account', tags=['User'], permissions=[permissions.IsAuthenticatedOrReadOnly])
class UserController:

    @route.get("/list/all", response=list[UserSchema], permissions=[])
    def get_all_users(self):
        return User.objects.all()
    
    @route.get("/user/{id}/", response=UserSchema)
    def get_user(self, id: int):
        user = get_object_or_404(User, id=id)
        return user

    @route.post("/user/register/", response={201: dict})
    def register(self, request: HttpRequest, data: UserCreationSchema):
        # Populate the form with the provided data
        signup_form = SignupForm(data.dict())
        
        # Validate and save the form
        if signup_form.is_valid():
            signup_view = SignupView()
            signup_view.request = request
            signup_view.form = signup_form
            response = signup_view.form_valid(signup_form)
            return 201, {"message": "User registered successfully"}
        else:
            return 400, {"errors": signup_form.errors}
        
@api_controller('/profiles', tags=['Profile'], permissions=[permissions.IsAuthenticatedOrReadOnly])   
class ProfileController:
    @route.get("/{slug}/", response=ProfileSchema)
    def get_profile(self, slug: str):
        profile = get_object_or_404(Profile, slug=slug)
        return profile


    @route.get("/profile/all", response=list[ProfileSchema], permissions=[])
    def get_all_profiles(self):
        return Profile.objects.all()
    
app.register_controllers(
    UserController,
    ProfileController,
)