# Temperature and humidity monitoring with Raspberry Pi and Grafana

This repo contains the code files, and the commands to run a Python app for monitoring temperature and humidity with a Raspberry Pi and Grafana.

For the full step-by-step instructions including hardware and software requirements, Raspberry Pi sensor wiring, code explanation, and overview of the tech stack needed (Python, Prometheus, Docker), see this [blog post](). 

## How to use the files

Below are the simplified steps that you need to take: 

- Step 1: Interact with your sensor, enable and export your sensor data through a port with the help of an exporter. For this part we will use Python. 

- Step 2: Scrape your sensor data with Prometheus
- Step 3: Monitor your data from Grafana

### Step 1 - Python

1. Clone this repo into your Raspberry Pi. 

    ``` git
    git clone https://github.com/tonypowa/sensor-data-monitoring-grafana.git
    ```

2. Open the console from the folder containing the cloned files.

3. Install the Python libraries in your Raspberry Pi.

    ```shell
    pip3 install Adafruit_DHT flask prometheus_client
    ```

4. Create, and run the Python script as a service.

   ``` shell
   sudo nano /etc/systemd/system/sensor-flask.service
   ```
    Inside, paste the following:
    
    ```
    [Unit]
    Description=A service that will keep my python app running in the background
    After=multi-user.target
    [Service]
    Type=simple
    Restart=always
    ExecStart=/usr/bin/python3 /path-to-python-file-/app.py
    [Install]
    WantedBy=multi-user.target
    ```
    Change is the **ExecStart** flag. The Python path, and the path to the script that needs to be executed.

    Reload the systemd manager.

   ```
   sudo systemctl daemon-reload
   ```
    Enable, and start our service right away.

   ```
   sudo systemctl enable sensor-flask.service --now
   ```
    Check the status of your service

   ```
   systemctl status sensor-flask.service
   ```
   
    Your Python web server should be up and running.

    If you send a request to  http://localhost:5000/metrics , or visit http://{you-raspberry-pi-IP-address}:5000/metrics from another machine in your network, you should be able to see the exported metrics.

### Step 2 - Prometheus

1. Run Prometheus on Docker

We will access the host port (our Raspberry Pi’s port), from inside the Docker container.
Run the below command. Make sure to tell Docker the path to the prometheus.yml file.

``` shell
docker run \
  -d \
    -p 9090:9090 \
    -v ./prometheus.yml:/etc/prometheus/prometheus.yml \
  --add-host=host.docker.internal:host-gateway \
    prom/prometheus
```


### Step 3 - Monitor your data from Grafana

From your machine, access your Raspberry PI by entering the IP address into the browser address: http://192.168.x.x:3000 . The Grafana login page should appear (if you [installed Grafana](https://grafana.com/tutorials/install-grafana-on-raspberry-pi/) before to this point).

DONE! Go ahead and [Explore]() [LINK TO LAST SECTION OF THE BLOG]() your data and create your own dashboards.
