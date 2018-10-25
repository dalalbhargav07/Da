# Relational DBMS (MySQL) vs NoSQL (ElasticSearch)

This mini project compares conventional RDBMS using MySQL and no structure DBMS using Elastic Search (NoSQL) which is installed on Microsoft Azure ubuntu instance.


### Report for the project
Report can be found [here](https://github.com/dalalbhargav07/Data-Warehousing-to-Data-Analytics/blob/master/Relational%20DBMS%20(MySQL)%20vs%20NoSQL/Report.pdf).

### Installation guide for ELasticSearch and MYSQL

Installation steps is for Ubuntu OS.

#### Installation steps for MYSQL:

1. Update the packages if there any:
 >> * sudo apt-get update
2. Install MYSQL server:
  >> * sudo apt-get install mysql-server
3. Enable Remote connection:
  >> * sudo vim /etc/mysql/mysql.conf.d/mysqld.conf
  >> * Look up for bind-adress field and in that uncomment network host and change it to whatever the remote IP you want to use and also uncomment the http port
 >> * Save the file
 >> * Restrart mysqlservice 
 >> * sudo systemctl restart mysql.service
4. Once restarted, connect to the mysql-server:
  >> * mysql -u root -p
5. Create new user:
  >> * CREATE USER 'username'@'localhost' IDENTIFIED BY 'passwrod';
  >> * GRANT ALL ON *.* TO 'username'@'localhost';
6. Create Database:
  >> * CREATE DATABASE dbname;

The setup for mysql server is ready for you!

### Installation steps for ElasticSearch:

1. Add the pre-requisite software JAVA PPA to apt-run:
  >> * sudo add-apt-repository -y ppa:webupd8team/java
  >> * sudo apt-get update
  >> * sudo apt-get -y install oracle-java8-installer
2. Download and install the public signing key:
  >> * wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
3. Save the definition of the repository to /etc/apt/sources.list.d/elasticsearch-6.x.list:
  >> * echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
4. Install elasticsearch
  >> * sudo apt-get install elasticsearch
5. Some important config changes:
  >> * sudo vim  /etc/elasticsearch/elasticsearch.yml
  >> * Locate and uncomment node.name and cluster.name and give new names.
  >> * Locate and uncomment network.host and change to 0.0.0.0.
  >> * Save the file and exit.
6. Restart the elasticsearch service.
  >> * sudo service elasticsearch restart
7. Test elastic search is running:
  >> * sudo service elasticsearch status
8. You can also setup elasticsearch to start during the server is booting up:
  >> * sudo update-rc.d elasticsearch defaults 95 10


The elastic search is ready to use. You can use any REST client (Postman, Insomia, Kibana, etc.) for doing the CRUD (Create, Read, Update and Delete) operations.

### References:

[1] “Install Elasticsearch with Debian Package | Elasticsearch Reference [6.2] | Elastic,” Open Source Search & Analytics · Elasticsearch. [Online]. Available: https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html. [Accessed: 23-May-2018]. <br />
[2] “Install MySQL on Ubuntu 14.04,” Linode Guides & Tutorials, 26-Aug-2015. [Online]. Available: https://www.linode.com/docs/databases/mysql/install-mysql-on-ubuntu-14-04/. [Accessed: 23-May-2018].

