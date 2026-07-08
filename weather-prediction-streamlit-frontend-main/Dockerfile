FROM python:3.9

# Set working directory
WORKDIR /app

# Expose the port the app runs on
EXPOSE 8080

# Upgrade pip
RUN pip install -U pip

# Copy and install requirements
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy app code
COPY streamlit_predict.py /app/

# # Local testing: add Google Cloud credentials
# COPY gcp_credentials.json /app/gcp_credentials.json
# ENV GOOGLE_APPLICATION_CREDENTIALS=/app/gcp_credentials.json

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "streamlit_predict.py", "--server.port=8080", "--server.address=0.0.0.0"]


# docker build -t eu.gcr.io/gcp_project_name/app_name:v1 .
# docker push eu.gcr.io/gcp_project_name/app_name:v1