import dict_manager
import config

def get_roles(message):
    return {"id": "config", "message": list(f"**{i}.** {rol.name}" for i, rol in enumerate(message.guild.roles, start=1))}