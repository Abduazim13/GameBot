from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS")
DATABASE_PRO = env.list("DATABASE_URL")

channel = (-1001915598425, 'https://t.me/carsinvideo')
