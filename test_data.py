from app.controller import result_controller
from app.data_models.result_models import Result, CommandList, Output
from app.data_models.command_models import Command
from dotenv import load_dotenv
import os
import random

load_dotenv()

host_name = os.getenv("HOST_NAME", "localhost:27017")

url = f"mongodb://root:example@{host_name}"


async def main():
    try:
        for i in range(100):
            result_instance = Result(
                hostname=f"example_host_{i}",
                ip=f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
                date=f"{str(random.randint(1, 25)).zfill(2)}-{str(random.randint(1, 12)).zfill(2)}-{random.randint(2016, 2024)}",
                score=random.randint(1, 100),
                commands=[
                    CommandList(
                        command=Command(chapter=f"{str(random.randint(1, 12))}.{str(random.randint(1, 12))}.{str(random.randint(1, 12))}.{str(random.randint(1, 12))}", description=f"This command is for show purposes", command="mount | grep -E '\\s/var/tmp\\s' | grep -v noexec", level=f"{str(random.randint(1, 2))}", weight=random.randint(1, 10)),
                        result=Output(output=f"output{i}", value=random.randint(0, 1))
                    )
                ]
            )
            result = await result_controller.insert_result(result_instance)
            print(f"{i+1}. - Successfully inserted the new result: {result}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())