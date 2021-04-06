# 4287-FinalProject

## How to run

```
```

## Pipeline
- Ansible playbook starts the entire system
- Boots up a k8s cluster which starts the kafka and serving the front end jobs
- The number of brokers in the kafka cluster should scale up depending on the demand
- The demand is pre estimated using the MARQ-PRO algo
- Depending on the calculated demand, scale up the number of brokers and the number of machines serving the front end
- The front end takes in a video stream (video file uploaded by the user) and passes it on to the brokers
- The brokers take the stream, send a request to 3rd party style transfer api, and then return the stream (interim-ly stored in a stream-table)
- The front end receives this and then returns the video for the user to download
- Cleanup as the demand slows down
- Use mininet to fake traffic for the VMs
- Use traffic graph similar to class
- Create visualization of results
- Easily adjustible for parameters with MARQ-PRO

## Parts
- Front end
- MARQ-PRO
- K8S
- Kafka
- Ansible
- Cloud instances
- SDN Mininet
- Visualizations

