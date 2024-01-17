import os
import logging
import motor.motor_asyncio as async_motor
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

host_name = os.getenv("HOST_NAME", "localhost:27017")


def create_mongo_client(username, password):
    mongo_details = f"mongodb://{username}:{password}@{host_name}"
    return async_motor.AsyncIOMotorClient(mongo_details)


try:
    login_client = create_mongo_client(os.getenv('MONGODB_USER_LOGIN_WRITE'), os.getenv('MONGODB_PASSWORD_LOGIN_WRITE'))
    login_collection = login_client.Security_Audit.get_collection("Login")
    logger.info("Connection to LOGIN established")

    command_client = create_mongo_client(os.getenv('MONGODB_USER_COMMANDS_WRITE'),
                                         os.getenv('MONGODB_PASSWORD_COMMANDS_WRITE'))
    command_collection = command_client.Security_Audit.get_collection("Commands")
    logger.info("Connection to COMMANDS established")

    result_client = create_mongo_client(os.getenv('MONGODB_USER_RESULTS_WRITE'),
                                        os.getenv('MONGODB_PASSWORD_RESULTS_WRITE'))
    result_collection = result_client.Security_Audit.get_collection("Audit_Results")
    logger.info("Connection to AUDIT-RESULTS established")
except ServerSelectionTimeoutError as e:
    logger.error(f"Failed to connect to the database: {e}")
    exit(1)
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
    exit(1)
