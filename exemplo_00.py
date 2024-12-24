from loguru import logger

def soma(x, y):
     logger.info(x)
     logger.info(y)
     logger.info(x + y)
     return x + y

print(soma(2, 3))