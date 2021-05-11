echo "Step: cd /final/dockerfiles"
cd /home/ec2-user/final/dockerfiles
#echo "Step: docker build -t zookeeper -f zookeeper.dockerfile ../"
#sudo docker build -t zookeeper -f zookeeper.dockerfile ../
echo "Step: docker build -t broker1 -f broker1.dockerfile ../"
sudo docker build -t broker1 -f broker1.dockerfile ../
echo "Step: docker build -t broker2 -f broker2.dockerfile ../"
sudo docker build -t broker2 -f broker2.dockerfile ../
echo "Step: docker build -t backend -f backend.dockerfile ../Consumer"
sudo docker build -t backend -f backend.dockerfile ../src
echo "Step: docker build -t webapp -f webapp.dockerfile ../Consumer"
sudo docker build -t webapp -f webapp.dockerfile ../src
#echo "Step: Start zookeeper"
#../kafka/bin/zookeeper-server-start.sh ../config/zookeeper.properties
echo "Step: docker run -d -p 9092:9092 -t broker1"
sudo docker run -d -p 9062:9062 -t broker1
echo "Step: docker run -d -p 9062:9062 -t broker2"
sudo docker run -d -p 9092:9092 -t broker2
echo "Step: docker run -d -t backend"
sudo docker run -d -t backend
echo "Step: docker run -d -p 5000:5000 -t webapp"
sudo docker run -d -p 5000:5000 -t webapp

