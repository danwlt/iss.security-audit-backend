import logging

from typing import List

from app.utils.database import command_collection
from app.data_models.command_models import Command

logger = logging.getLogger(__name__)


#####################################
# GET
#####################################

async def retrieve_all_commands() -> List[Command]:
    commands: List[Command] = []
    async for result in command_collection.find():
        commands.append(result)
    logger.info("Found {} commands in database".format(len(commands)))
    return commands
