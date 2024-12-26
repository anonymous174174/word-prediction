import uvicorn

def run_server():
    # Initialize and run the FastAPI server
    uvicorn.run("app.api:service", host="0.0.0.0", port=8080, reload=True)

if __name__ == "__main__":
    run_server()
