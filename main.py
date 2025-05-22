from domain.weather_service import get_weather_string
from infra.file_writer import final_message
from infra.logger import setup_logger
from datetime import datetime

logger=setup_logger()
def main():
    logger.info('Starting the weather application')
    city_name=input('Enter city name:')
    get_weather_string(city_name)
    print(get_weather_string(city_name))
    final_message()
   # logger.info(datetime.now())
    logger.info(f' {datetime.now()} Weather checked for {city_name}')


if __name__ == '__main__':
    main()