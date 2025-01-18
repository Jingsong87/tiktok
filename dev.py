from hashlib import md5, sha1
from time import time


def generate_as(time_now: str) -> str:
    as_md5 = md5(time_now.encode()).hexdigest()

    return as_md5


def generate_cp(time_now: str) -> str:
    time_now += str(time())

    cp_md5 = md5(time_now.encode()).hexdigest()

    return cp_md5


def generate_mas(time_now: str) -> str:
    mas_sha = sha1(time_now.encode()).hexdigest()
    mas_md5 = md5(mas_sha.encode()).hexdigest()

    return mas_md5


if __name__ == '__main__':
    now = str(int(round(time() * 1000)))

    param_as = generate_as(now)
    param_cp = generate_cp(now)
    param_mas = generate_mas(now)

    print({'as': param_as, 'cp': param_cp, 'mas': param_as})
