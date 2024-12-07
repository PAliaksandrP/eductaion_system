from Application import Application
import uvicorn

if __name__ == "__main__":
    app = Application()
    uvicorn.run(app.app, host="127.0.0.1", port=8000)