from dataclasses import dataclass

from environs import Env

@dataclass
class Django_password:
    SECRET_KEY:str

@dataclass
class Config:
    dp: Django_password


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    SECRET_KEY = env.str('SECRET_KEY')
    return SECRET_KEY
    # return Config(
    #     dp=Django_password(
    #         SECRET_KEY=env.str('SECRET_KEY'),
    #     ),
    # )


# def load_postgres_URI(path: str = None):
#     env = Env()
#     env.read_env(path)
#     return DbConfig(
#         host=env.str('DB_HOST'),
#         password=env.str('PG_PASSWORD'),
#         user=env.str('DB_USER'),
#         database=env.str('DB_NAME'),
#         postgres_uri=f"postgresql://{env.str('DB_USER')}:{env.str('PG_PASSWORD')}@{env.str('DB_HOST')}/{env.str('DB_NAME')}"
#     )
