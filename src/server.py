from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")

@app.get("/")
def Home(req: Request):
    # 1. Check if the header exists (provided by Render's proxy)
    forwarded = req.headers.get("x-forwarded-for")
    
    if forwarded:
        # The header can be a list: "Client-IP, Proxy1-IP, Proxy2-IP"
        # The first IP is always the real user.
        ip_address = forwarded.split(",")[0]
    else:
        # Fallback for local development
        ip_address = req.client.host
    
    return template.TemplateResponse(req, "index.html", {
        "ip": ip_address
    })