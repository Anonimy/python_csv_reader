FROM python:3
ARG csvfile=users.csv
ADD $csvfile users.csv
ADD script.py script.py
RUN pip install requests
CMD [ "python", "script.py" ]
