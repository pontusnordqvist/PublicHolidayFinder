FROM python:3.9

ADD app.py .

#WORKDIR /src

COPY requirements.txt .

COPY ./Data/MinedData/CleanedHolidayData2016-2022.csv ./Data/MinedData/CleanedHolidayData2016-2022.csv

RUN pip install -r requirements.txt

#COPY ./src ./src

#CMD [ "python", "./src/app.py" ]
CMD [ "python", "./app.py" ]