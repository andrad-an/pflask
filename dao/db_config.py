import psycopg2
import os

DATABASE_URL = os.getenv(
    'POSTGRES_URL',
    'postgresql://neondb_owner:npg_G71wvbmUBSgq@ep-dry-waterfall-b8g3dy56-pooler.c-14.us-east-1.aws.neon.tech/neondb?sslmode=require'
)

def get_connection():
    return psycopg2.connect(DATABASE_URL)