from fastapi import FastAPI, Depends, HTTPException, Response, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
import jwt

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define a hard-coded username and password for testing purposes
sec_username = "hunkim"
sec_password = "lovehunkim"

# Define a secret key to sign the JWT tokens
secret_key = "secret"

# Define the HTTPBasic and HTTPBearer security classes
basic_auth = HTTPBasic()
bearer_auth = HTTPBearer()

# Define a route that accepts HTTP Basic authentication credentials and returns a JWT token
@app.post("/login")
async def login(request: Request):
    payload = await request.json()
    username = payload["username"]
    password = payload["password"]
    
    if username != sec_username or password != sec_password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
        
    # Generate a JWT token with an expiration time of 1 hour
    expiration = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode({"username": username, "exp": expiration}, secret_key, algorithm="HS256")
    return {"access_token": token}

# Define a dependency that retrieves the user information from a JWT token
async def get_user(token: HTTPAuthorizationCredentials = Depends(bearer_auth)):
    try:
        payload = jwt.decode(token.credentials, secret_key, algorithms=["HS256"])
        return payload["username"]
    except (jwt.exceptions.InvalidTokenError, jwt.exceptions.ExpiredSignatureError):
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
# Define a route that requires a valid JWT token for authentication
@app.get("/secure")
async def secure_route(username: str = Depends(get_user)):
    return {"message": f"Hello, {username}!"}

