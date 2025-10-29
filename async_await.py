import asyncio


async def create_user():
    print("Creating User...")
    for i in range(50_000_000):
        if i == 4_999_999:
            print("User Created.") 
                           
        if i % 1_000_000 == 0:
            await asyncio.sleep(0)
            
async def mail():
    print("Mail Sent")


async def main():    
    await asyncio.gather(
        create_user(),
        mail()
    )

asyncio.run(main())
