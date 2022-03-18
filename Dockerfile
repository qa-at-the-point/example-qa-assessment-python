FROM python:3.8

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install latest stable Google Chrome
RUN apt-get -y update && apt-get -y install google-chrome-stable

# Copy our project to the container
COPY . /app
WORKDIR /app

# Install poetry and dependencies
RUN pip install poetry && poetry install

# Run the tests
ENTRYPOINT poetry run pytest --html=report.html --junitxml=report.xml
