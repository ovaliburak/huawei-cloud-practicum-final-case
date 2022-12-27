import jwt
import datetime
import os
from flask import Flask, request
import psycopg2

server = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", '0.0.0.0'),
        database=os.environ.get("POSTGRES_DB", 'hr'),
        user=os.environ.get("POSTGRES_USER", 'root'),
        password=os.environ.get("POSTGRES_PASSWORD", '0074'),
        port=os.environ.get("POSTGRES_PORT", '5432'),
    )
    return conn


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401
    # check db for username and password
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT phone_number, password FROM employee_user WHERE phone_number='%s'" % auth.username)
    user_row = cur.fetchone()
    if len(user_row) > 0:
        phone_number = user_row[0]
        password = user_row[1]
        if auth.username != phone_number or auth.password != password:
            return "invalid credentials", 401
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return "invalid credentials", 401


@server.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "missing credentials", 401

    encoded_jwt = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(
            encoded_jwt, os.environ.get("JWT_SECRET"), algorithms=["HS256"]
        )
    except:
        return "not authorized", 403

    return decoded, 200


def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
