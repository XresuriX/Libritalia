from django.shortcuts import get_object_or_404
from ninja_extra import NinjaExtraAPI, api_controller, route, permissions, throttle, ModelConfig, ModelControllerBase, ModelSchemaConfig # type: ignore
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from allauth.account.views import SignupView
from django.http import HttpRequest
from libretalia.users.models import User, Profile
from .schemas import UserSchema, UserCreationSchema, ProfileSchema

app = NinjaExtraAPI()

"""@api_controller('/account', tags=['User'], permissions=[permissions.IsAuthenticatedOrReadOnly])
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
            return 400, {"errors": signup_form.errors}"""
        
@api_controller('/profiles', tags=['Profile'], permissions=[permissions.IsAuthenticatedOrReadOnly])   
class ProfileModelController(ModelControllerBase):
    model_config = ModelConfig(
        model=Profile,
        allowed_routes=['find_one', "update", "patch", "delete", 'list'],
        schema_config=ModelSchemaConfig(read_only_fields=["id"]),
    )
    
app.register_controllers(
    #UserController,
    ProfileModelController,
)