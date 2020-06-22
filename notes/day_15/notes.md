# Day 15 Notes

## Things to talk about

* What is docker doing?
    - docker ps <-- lists all the docker containers running
    - docker rm -f <container_id>  <-- kills container

Example of the Docker daemon not running:
(python-tutorial) deanchin@deans-mbp ~/i/t/p/d/python-tutorial> docker ps
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
Find the DOcker executable (search in Windows) and run it.  Wait for it to fully start up... you should be able to see from the Docker icon.  Then run `docker ps`.

```bash
# To startup mongo container
# you need to change directory to where the docker-compose.yml is.
docker-compose up -d
```

* What is a ODM?
- I belive this means Object Data Mapping.  It is a way to map your python objects 
  to a document structure in the mongo collection.  We will put this on hold for now and
  come back to it later

* What do we need to do to start up our own little database?
- If you have docker, use the docker-compose.yml file in the root of our repository to start up a docker
  container that has mongo database running.  execute `docker-compose up -d`
- If not running docker, you will install the mongo on your laptop/machine and start it up.


* How do we use it with the address book?
```bash
# tracing back our app.py to get an understanding of how it uses the database (bottom up approach)
/utils/db_util.py: db_name = 'python-tutorial'              <-- Database Name
/utils/db_util.py: self.db_client = self.client[db_name]    <-- Database Client connect to database python-tutorial
/utils/db_util.py: get_collection returns self.db_client[collection_name]  <-- Use the db client to get the contact collection
/src/service/contact.py: self.collection_name = contact
/src/service/contact.py: self.collection =  DBUtil().get_collection(self.collection_name)
/src/service/contact.py: self.collection.insert_one()       <-- Insert a document into the collection
app.py - Contact().add_item()
```
    - Debug issues
* Go thru Ricky's code where he was having issues with a post and multiple insert of documents.

* Other practice problems

```bash
When you run your app.py it can do the following:
Create a new database called blockbuster
Create a collection called movies
Add/Delete/Get movies
```


## Ideas

* Online Diary
