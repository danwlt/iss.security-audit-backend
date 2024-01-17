import logging

from fastapi import APIRouter, HTTPException
from app.controller import command_controller

router = APIRouter()
logger = logging.getLogger(__name__)


#####################################
# GET
#####################################

@router.get('/get_commands')
async def get_commands():
    try:
        commands = await command_controller.retrieve_all_commands()
        for command in commands:
            command["_id"] = str(command["_id"])
        return commands
    except Exception as e:
        logger.debug(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
