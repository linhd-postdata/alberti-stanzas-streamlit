FROM python:3.9

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8008

ENTRYPOINT ["streamlit", "run"]
CMD ["stanza_detection.py"]
