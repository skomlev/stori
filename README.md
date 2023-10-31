# Stori Challenge.
Full specification of the challenge can be found [here]([Tech_Challenge_-_Software_Engineer-1.pdf](doc%2FTech_Challenge_-_Software_Engineer-1.pdf))

## Getting Started

These are the steps to set up and run your project using Docker Compose.

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/skomlev/stori.git
    cd stori
    ```

2. Edit `setting.py` with your configuration settings:
    ```
   EMAIL = {
      'host': os.environ.get('EMAIL_HOST', 'smtp.gmail.com'),
      'port': os.environ.get('EMAIL_PORT', 587),
      'sender': os.environ.get('EMAIL_SENDER', 'example@gmail.com'),
      'user': os.environ.get('EMAIL_USER', 'example@gmail.com'),
      # https://support.google.com/accounts/answer/185833?hl=es&sjid=14820134242632080947-SA
      'password': os.environ.get('EMAIL_PASSWORD', "secret password cccc xxxx "),
   }

   FILE_PATH = os.environ.get('FILE_PATH', 'data/txns.csv')
   SUMMARY_USER = os.environ.get('SUMMARY_USER', 'destination@gmail.com')
    ```

3.1 Execute whit Dockerfile

3.1.1 Prerequisites
Make sure you have the following software installed on your machine:
Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)

3.1.2 Build and run the Docker image:
 ```bash
    docker build -t stori .
    docker run story
 ```

3.2 Execute whit [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
```bash
 virtualenv venv
 . venv/bin/activate
 pip install -r requirements.txt
 python many.py
 ```

