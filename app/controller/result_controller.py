import logging

from typing import List, Union

from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from app.utils.database import result_collection
from app.data_models.result_models import Result

logger = logging.getLogger(__name__)


#####################################
# GET
#####################################

async def retrieve_all_results() -> List[Result]:
    results: List[Result] = []
    async for result in result_collection.find():
        results.append(result)
    logger.info("Found {} results in database".format(len(results)))
    return results


async def retrieve_results_pagination(page_number=1, page_size=20) -> List[Result]:
    skipAmount = (page_number - 1) * page_size
    results: List[Result] = []
    async for result in result_collection.find().skip(skipAmount).limit(page_size):
        results.append(result)
    logger.info("Found {} results in database".format(len(results)))
    return results


async def retrieve_single_result(result_id: str) -> Result:
    result: Union[None, Result] = await result_collection.find_one({'_id': ObjectId(result_id)})
    logger.info("Found result {} in database".format(result))
    return result


async def count_documents() -> int:
    count: int = await result_collection.count_documents({})
    logger.info("Amount of results: {}".format(str(count)))
    return count


async def search_documents(search_term: str) -> List[Result]:
    results: List[Result] = []
    regex_pattern = f".*{search_term}.*"
    query = {
        "$or": [
            {"ip": {"$regex": regex_pattern, "$options": "i"}},
            {"date": {"$regex": regex_pattern, "$options": "i"}},
            {"hostname": {"$regex": regex_pattern, "$options": "i"}},
            {"score": {"$regex": search_term, "$options": "i"}},
        ]
    }
    async for result in result_collection.find(query):
        results.append(result)
    logger.info(f"Found {len(results)} Results for the term {search_term}")
    return results


#####################################
# POST
#####################################

async def insert_result(result: Result):
    return await result_collection.insert_one(jsonable_encoder(result))


#####################################
# DELETE
#####################################

async def delete_result(result_id: str):
    return await result_collection.delete_one({"_id": ObjectId(result_id)})
