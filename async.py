import asyncio
import aiohttp

# async def fetch_data():
#     print("Fetching data...")
#     await asyncio.sleep(2)  # Simulates a network request
#     print("Data fetched!")
#     return {"data": "sample"}


# async def process_data():
#     print("Processing data...")
#     await asyncio.sleep(1)  # Simulates data processing
#     print("Data processed!")


# async def main():
#     # Run tasks concurrently
#     fetch_task = asyncio.create_task(fetch_data())
#     process_task = asyncio.create_task(process_data())

#     # Wait for both tasks to complete
#     await fetch_task
#     await process_task

# # Run the event loop
# asyncio.run(main())


# Make a GET request
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()  # Parse JSON response
                print("Data received:", data)
            else:
                print("Failed to fetch data. Status code:", response.status)
            print("Data fetched!")

async def main():
    # Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/users"
    # Create and await the task directly
    await fetch_data(url)


async def send_data():
    async with aiohttp.ClientSession() as session:
        payload = {'key': 'value'}
        async with session.post('https://api.example.com/submit', json=payload) as response:
            print("Status:", response.status)
            print("Response:", await response.json())

asyncio.run(send_data())

# Run the event loop
asyncio.run(main())
