from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")

@app.get("/")
def Home(req: Request):
    
    ip_address = req.client.host
    
    return template.TemplateResponse(req, "index.html", {

        "ip" : ip_address
    })