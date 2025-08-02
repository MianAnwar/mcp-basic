import asyncio


# with open("data.txt", "r") as file:
#     data = file.read()
#     print(data)

# with open("output.txt", "w") as file:
#     file.write("data")

# with open("data.txt", "r") as file, open("output.txt", "w") as output_file:
#     for line in file:
#         output_file.write("1: "+line)
#         print(line.strip())  # Print each line without extra newlines







# from contextlib import asynccontextmanager
# @asynccontextmanager
# async def make_connection(name: str):
#     print(f"Connecting to {name}...")
#     await asyncio.sleep(10)  # Simulate a network delay
#     yield name
#     print(f"Connected to {name}!")

# async def main():
#     async with make_connection("ConnectionString") as conn:
#         print(f"Using {conn} in the main function.")
#         await asyncio.sleep(2)  # Simulate some work
#     print("Connection closed.")









from contextlib import AsyncExitStack


async def get_connection(name: str):
    class ctx():
        def __init__(self):
            self.name = name
        
        async def __aenter__(self):
            print(f"Connecting to {self.name}...")
            await asyncio.sleep(3)
            return self.name
        
        async def __aexit__(self, exc_type, exc_value, traceback):
            print(f"Connected to {self.name}! Connection closed.")
    
    return ctx()

# async def main():
#     async with await get_connection("ConnectionString") as conn:
#         print(f"Using {conn} in the main function.")
#         await asyncio.sleep(2)  # Simulate some work

async def main():
    async with AsyncExitStack() as stack:
        a = await stack.enter_async_context(await get_connection("A ConnectionString"))
        if(a == "A ConnectionString"):
            b = await stack.enter_async_context(await get_connection("B ConnectionString"))
            print(f"Using {a} and {b} in the main function.")
        
        async def customClearnUp():
            await asyncio.sleep(1)
            print("Custom cleanup logic executed.")
            
        stack.push_async_callback(customClearnUp)
        # locals is a dictionary that contains the current local symbol table
        print(f"Doing processing with {a} and {locals().get('B ConnectionString')} in the main function.")
        await asyncio.sleep(2)  # Simulate some work
            
asyncio.run(main())
