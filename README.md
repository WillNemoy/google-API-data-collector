# Google-API-Data-Collector
Collect review data from Google Places API.


## Setup

Create and activate a virtual environment:

```sh
conda create -n googleAPI-env python=3.8

conda activate googleAPI-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://console.cloud.google.com/welcome?project=tweet-research-shared) from Google.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

GOOGLE_API_KEY="_________"

```



## Usage

Run the program:

```sh
python app.py
```
