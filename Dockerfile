FROM python:3.8.1-slim-buster
COPY *.py app/
COPY Scores.txt app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask
RUN chmod 644 Utils.py MainScores.py Scores.txt
EXPOSE 5000
CMD ["python", "MainScores.py"]

