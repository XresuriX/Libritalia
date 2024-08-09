from ninja import ModelSchema, Schema # type: ignore
from .models import User, Profile

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')

class UserCreationSchema(Schema):
    username: str
    email: str
    password1: str
    password2: str


class ProfileSchema(ModelSchema):
    user: UserSchema 

    class Meta:
        model = Profile
        fields = ('user', 'avatar', 'about', 'slug', 'followers', 'location')


"""class DeviceCreateSchema(Schema):
    name: str 
    location_id: int | None = None"""


class Error(Schema):
    message: str