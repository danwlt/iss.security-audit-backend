import logging

from fastapi.encoders import jsonable_encoder
from app.utils.database import login_collection as user_collection
from app.data_models.user_models import UserModel, UserPublicModel, NewUser

logger = logging.getLogger(__name__)


#####################################
# GET
#####################################

async def retrieve_single_user(user_id: str = '', username: str = '') -> UserPublicModel:
    user = None
    if user_id:
        user = await user_collection.find_one({'_id': user_id})
    if username:
        user = await user_collection.find_one({'username': username})

    if user:
        logger.info("Found user {} in database".format(username, user_id))
        return user
    else:
        logger.info("Did not find user for user_id / username {} in database".format(user_id, username))
        return user


async def retrieve_single_user_private(username: str) -> UserModel:
    return await user_collection.find_one({'username': username})


async def retrieve_all_user() -> list:
    users = []
    async for user in user_collection.find():
        users.append(user)
    logger.info("Found {} users in database".format(len(users)))
    return users


async def access_token_exists(token: str) -> bool:
    access_token = await user_collection.find_one({'accessToken': token})
    if access_token:
        return True
    else:
        return False


#####################################
# POST
#####################################

async def insert_single_user(user: NewUser):
    from app.utils.auth import auth
    user.password = auth.get_password_hash(plain_password=user.password)
    return await user_collection.insert_one(jsonable_encoder(user))


#####################################
# PUT
#####################################

async def update_access_token(username: str, token: str):
    return await user_collection.update_one({'username': username}, {'$set': {'accessToken': token}})
