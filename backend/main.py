from typing import Union
from decouple import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import format_output
import paramiko

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_vms():
    username = config('ssh_username')
    password = config('ssh_password')
    url = config('ssh_url')

    with paramiko.SSHClient() as client:
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(url, username=username, password=password)

        _, stdout, __ = client.exec_command('powershell.exe get-vm')
        stdout = stdout.read().decode('utf-8')
        vms = format_output(stdout)

    return {"item_id": "ok"}