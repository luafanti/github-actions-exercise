"""
FastAPI application with health-check and hello-world endpoints.
"""
import os

from fastapi import FastAPI, Response

app = FastAPI(
    title="GitHub Actions Exercise",
    description="Simple HTTP server",
    version="1.0.0",
)


@app.get("/health-check")
async def health_check():
    """
    Health check endpoint returning status in JSON format.

    Returns:
        dict: JSON response with status "ok"
    """
    return {"status": "ok"}


@app.get("/hello-world")
async def hello_world():
    """
    Hello world endpoint returning text from SERVER_HELLO environment variable.

    Returns:
        Response: Plain text response with content from SERVER_HELLO environment variable

    Raises:
        RuntimeError: If SERVER_HELLO environment variable is not set
    """
    hello_text = os.getenv("SERVER_HELLO")
    if hello_text is None:
        raise RuntimeError("SERVER_HELLO environment variable is not set")
    return Response(content=hello_text, media_type="text/plain")
