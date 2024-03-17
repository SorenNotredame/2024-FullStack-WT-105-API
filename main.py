from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import FW_endpoints, SG_endpoints, SN_endpoints, TL_endpoints

app = FastAPI(docs_url=config.documentation_url)

app.include_router(router=FW_endpoints.app, prefix="/FW")
app.include_router(router=SG_endpoints.app, prefix="/SG")
app.include_router(router=SN_endpoints.app, prefix="/SN")
app.include_router(router=TL_endpoints.app, prefix="/TL")

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




