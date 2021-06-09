FROM python:3.9

ADD app.py .

COPY requirements.txt .

COPY ./Data//CleanedData/CleanHolidayData2016-2022.csv ./Data/CleanedData/CleanHolidayData2016-2022.csv

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]