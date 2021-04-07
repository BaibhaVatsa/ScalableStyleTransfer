# 4287-FinalProject

## How to run

```
```

## Pipeline
- Ansible playbook starts the entire system
- Boots up a k8s cluster which starts the kafka and serving the front end jobs
- The number of brokers in the kafka cluster should scale up depending on the demand
- Use Kakfa Stream to handle scaling and elasticity. 
- Depending on the calculated demand, scale up the number of brokers and the number of machines serving the front end 
- The front end application takes in a video stream (video file uploaded by the user) does some analytics and passed onto the brokers with our configured kafka stream
- The brokers take the stream, send a request to 3rd party style transfer api, and then return the stream (interim-ly stored in a stream-table)
- The front end application receives this and then returns the video for the user to download
- Cleanup as the demand slows down

## Technical configuration and visualization
- Use mininet to fake traffic for the VMs
- Use traffic graph similar to class
- Create visualization of results

## Parts
- Front end application (JAVA)
- K8S
- Kafka
- Ansible
- Cloud instances
- SDN Mininet
- Visualizations

## Future work
- Application logic and code
- kafka stream execution
- backend analytics and process of stream data (MAP REDUCE?)

