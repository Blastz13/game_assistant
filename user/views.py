from typing import List

from asgiref.sync import sync_to_async
from ninja import Router

from .models import User
from .schemas import UserOut


user_router = Router()


@user_router.get('/', response=List[UserOut])
async def get_user_list(request):
    return await sync_to_async(list)(User.objects.all())
