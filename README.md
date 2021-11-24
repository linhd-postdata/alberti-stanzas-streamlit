# alberti-stanzas-streamlit

This is a demo for the ALBERTI language model trained for stanza type detection.
ALBERTI is a set of two BERT-based multilingual model for poetry. 
One for verses and another one for stanzas. 
This model has been further trained with the PULPO corpus. 
Paste or write your own your own poem and click the button to try it.
Read more: https://huggingface.co/flax-community/alberti-bert-base-multilingual-cased

## Deployment

This app can be run completely using `Docker` is recommended, as it guarantees the application is run using compatible versions of Python and streamlit

### Prerequisites

Clone this repository:
```
git clone https://github.com/linhd-postdata/alberti-stanzas-streamlit.git
```

Download the model files from [OneDrive](https://unedo365.sharepoint.com/:f:/s/proyectoercpostdata/Eo6PIEWJZGpGjROIL6R5p-sBqK2A7w4YVTVBH3IFXbsYqA?e=U8tJea) 
and place them in a folder named `alberti-finetuned`.

### Docker Quickstart

To build the docker container:
```
docker build -t albertistreamlit:latest .
```
and then, to run it on the port 8008:
```
docker run -p 8008:8008 albertistreamlit:latest
```
You will see a pretty web page at [localhost:8008](localhost:8008)

### Running locally (development)
Run the following commands (it's recommended to create and use a virtual environment)

```bash
cd alberti-stanzas-streamlit
pip install -r requirements.txt
streamlit run stanza_detection.py
```
