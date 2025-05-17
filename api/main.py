from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
import uvicorn
from comp.computing import make_table

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/plan/{teams}/{gyms}/{starttime}/{time_per_game}/{time_per_break}")
def make_game_plan(teams: int, gyms: int, starttime: str, time_per_game: int, time_per_break: int):
    return make_table(teams, gyms, starttime,time_per_game, time_per_break)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info", timeout_keep_alive=60)

if __name__ == "__main__":
    main()
