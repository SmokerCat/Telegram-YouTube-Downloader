from __future__ import unicode_literals
import asyncio
from Trial import *
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
async def fetvisual(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print(e_response)
    filename = t_response.split(
    "Merging formats into")
    [-1].split('"')[1]
    return filename
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"
async def fetaudio(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print("Download error:", e_response)
    return t_response.split("Destination")[-1].split("Deleting")[0].split(":")[-1].strip()
"|►►►►►►►►►►►►►►►►►►►►►✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄◄|"