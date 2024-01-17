import logging
from app.utils.auth import auth
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.controller import user_controller
from app.data_models.response_models import response_factory
from app.data_models.user_models import NewUser
from app.utils.database import login_collection as user_collection

router = APIRouter()
logger = logging.getLogger(__name__)


#####################################
# POST
#####################################

@router.post('/')
async def get_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await auth.authenticate_user(username=form_data.username, password=form_data.password)
    if user:
        if user.active:
            token = {
                "access_token": auth.create_access_token(
                    json_web_token={
                        'sub': user.username
                    }),
                'token_type': 'bearer'
            }
            if await user_controller.update_access_token(username=user.username, token=token['access_token']):
                logger.debug(f"Update {user.username} with new access_token token")
                return token
            else:
                logger.debug(f"Update of {user.username} with token failed")
                raise HTTPException(status_code=500, detail="Setting JWT failed")
        else:
            logger.debug("No Access-Token was created for user {}: User inactive".format(user.username, user.active))
    else:
        logger.debug("User {} not found in database or password invalid".format(form_data.username))
        raise HTTPException(status_code=403, detail='Invalid Username or Password or user inactive')


@router.delete('/')
async def delete_access_token(token=Depends(auth.oauth2scheme)):
    if await auth.is_authenticated(token=token):
        payload = auth.decode_jwt(token=token)
        if await user_controller.update_access_token(username=payload.get("sub"), token=''):
            logger.debug("Access Token removed successfully, user logged out")
            return response_factory(None, "Logout successfull")
        else:
            logger.debug("Error while removing access-token")
            raise HTTPException(status_code=500, detail="Logout failed")
    else:
        logger.debug("Rejected unauthenticated api call")
        raise HTTPException(status_code=403, detail='Unauthenticated')


"""
@router.post('/cre')
async def create_new_user(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user_data = {
            "username": form_data.username,
            "password": form_data.password,
            "active": True,
            "email": "john.doe@example.com",
        }
        response = await user_controller.insert_single_user(NewUser(**user_data))
        return {"message": "Purfekt"}
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
"""