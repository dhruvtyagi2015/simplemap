FROM python

RUN mkdir /app

WORKDIR /app



## Add application code
COPY ./* /app/
RUN ls /app
## Allows port 3000 to be publicly available
EXPOSE 8000


CMD ["python ./server.py"]
