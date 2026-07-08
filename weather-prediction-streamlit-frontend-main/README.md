# Weather Prediction Streamlit Web App
Weather prediction model predictions Web App Fronend made with Streamlit (for a cloud computing uni course - RSO).

Its a simple app that shows the value of the latest prediction and a graph of the last month predictions.

![Streamlit Web App](./images/wp-streamlit.png)

## Running Locally

To run the application locally, follow these steps:

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Google Application Credentials**:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json
   ```

3. **Start Ray Serve Application**:
   ```bash
   streamlit run streamlit_predict.py
   ```

## Docker and GCP CloudRun Deployment 

To deploy the application using Docker and Google Cloud Run, follow these steps:

1. **Build the Docker Image Locally**:
   ```bash
   docker build -t streamlit_wp_predict .
   ```

2. **Run the Docker Image Locally for Testing**:
   - This command runs the Docker container locally and sets the Google Cloud credentials.
   ```bash
   docker run -p 8080:8080 \
      -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/gcp_credentials.json \
      -v /path/to/your/credentials:/tmp/keys \
      streamlit_wp_predict
   ```
   Replace `/path/to/your/credentials` with the actual path to your Google Cloud credentials JSON file.

3. **Authenticate with Google Cloud**:
   ```bash
   gcloud auth login
   gcloud projects list --sort-by=projectId --limit=5
   gcloud config set project <project_id>
   gcloud auth configure-docker
   ```

4. **Build and Tag the Image for Google Container Registry**:
   ```bash
   docker build -t eu.gcr.io/<project_id>/streamlit_wp_predict:v1 .
   ```

5. **Push the Docker Image to Google Container Registry**:
   ```bash
   docker push eu.gcr.io/<project_id>/streamlit_wp_predict:v1
   ```

6. **Deploy to Google Cloud Run**:
   - Open the Google Cloud Console.
   - Navigate to Cloud Run.
   - Click on 'Create Service'.
   - Choose the image you just pushed.
   - Set any required configurations (like memory, CPU).
   - Deploy the image.

