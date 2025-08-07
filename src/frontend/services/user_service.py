import httpx

async def fetch_users() -> tuple[list[dict], str]:
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/admin/users")
        if response.status_code == 200:
            return response.json(), "Usuarios cargados correctamente"
        return [], f"Error al cargar usuarios: {response.status_code}"
