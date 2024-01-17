import logging

import math
from app.data_models.result_models import Result
from app.utils.auth import auth
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
import jwt as jwt
from app.controller import result_controller
from app.data_models.response_models import response_factory
router = APIRouter()
logger = logging.getLogger(__name__)


#####################################
# GET
#####################################

@router.get('/page/{page_number}')
async def get_results(page_number: int, token: jwt = Depends(auth.oauth2scheme)):
    if await auth.is_authenticated(token=token):
        try:
            results = await result_controller.retrieve_results_pagination(page_number=page_number)
            for result in results:
                result["_id"] = str(result["_id"])
            return results
        except Exception as e:
            logger.debug(f"Error: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
    else:
        logger.debug("Rejected unauthenticated api call")
        raise HTTPException(status_code=403, detail='failed to authenticate')


@router.get('/pages')
async def get_pages(token: jwt = Depends(auth.oauth2scheme)):
    if await auth.is_authenticated(token=token):
        try:
            results: int = await result_controller.count_documents()
            results = math.ceil(results / 20)
            return {"pages": results}
        except Exception as e:
            logger.debug(f"Error: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
    else:
        logger.debug("Rejected unauthenticated api call")
        raise HTTPException(status_code=403, detail='failed to authenticate')


@router.get('/search/{search_term}')
async def search_results(search_term: str, token: jwt = Depends(auth.oauth2scheme)):
    if await auth.is_authenticated(token=token):
        try:
            results = await result_controller.search_documents(search_term=search_term)
            for result in results:
                result["_id"] = str(result["_id"])
            return results
        except Exception as e:
            logger.debug(f"Error: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
    else:
        logger.debug("Rejected unauthenticated api call")
        raise HTTPException(status_code=403, detail='failed to authenticate')


@router.get('/single/{result_id}')
async def retrieve_single_result(result_id: str, token: jwt = Depends(auth.oauth2scheme)):
    if await auth.is_authenticated(token=token):
        try:
            result: Result = await result_controller.retrieve_single_result(result_id)
            result["_id"] = str(result["_id"])
            return result
        except Exception as e:
            logger.debug(f"Error: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
    else:
        logger.debug("Rejected unauthenticated api call")
        raise HTTPException(status_code=403, detail='failed to authenticate')


#####################################
# POST
#####################################

@router.post('/')
async def post_results(result: Result):
    try:
        results = await result_controller.insert_result(result=result)
        if results:
            return response_factory(None, "inserted result")
        else:
            raise HTTPException(status_code=500, detail="inserting result failed")
    except Exception as e:
        logger.debug(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


#####################################
# DELETE
#####################################

@router.delete('/{result_id}')
async def delete_result(result_id: str, token=Depends(auth.oauth2scheme)):
    if await auth.is_authenticated(token=token):
        try:
            results = await result_controller.delete_result(result_id=result_id)
            if results:
                return response_factory(None, "deleted result")
            else:
                raise HTTPException(status_code=500, detail="deleting resul failed")
        except Exception as e:
            logger.debug(f"Error: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
    else:
        logger.debug("Rejected unauthenticated api call")
        raise HTTPException(status_code=403, detail='failed to authenticate')
