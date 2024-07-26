from news_bot import app

if __name__ == "__main__":
    import hypercorn.asyncio
    import asyncio

    asyncio.run(hypercorn.asyncio.serve(app, hypercorn.Config()))
