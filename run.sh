echo "Step: sudo yum install docker"
sudo yum install docker
echo "Step: cd /final/dockerfiles"
cd /final/dockerfiles
echo "Step: docker build -t zookeeper -f zookeeper.dockerfile ../"
docker build -t zookeeper -f zookeeper.dockerfile ../
echo "Step: docker build -t broker1 -f broker1.dockerfile ../"
docker build -t broker1 -f broker1.dockerfile ../
echo "Step: docker build -t broker2 -f broker2.dockerfile ../"
docker build -t broker2 -f broker2.dockerfile ../
echo "Step: docker build -t backend -f backend.dockerfile ../Consumer"
docker build -t backend -f backend.dockerfile ../Consumer
echo "Step: docker build -t webapp -f webapp.dockerfile ../Consumer"
docker build -t webapp -f webapp.dockerfile ../Consumer
echo "Step: docker run -d -p 2181:2181 -t zookeeper"
docker run -d -p 2181:2181 -t zookeeper
echo "Step: docker run -d -p 9092:9092 -t broker1"
docker run -d -p 9092:9092 -t broker1
echo "Step: docker run -d -p 9062:9062 -t broker2"
docker run -d -p 9062:9062 -t broker2
echo "Step: docker run -d -t backend"
docker run -d -t backend
echo "Step: docker run -d -p 5000:5000 -t webapp"
docker run -d -p 5000:5000 -t webapp

