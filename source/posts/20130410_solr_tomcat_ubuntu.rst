How to install solr on tomcat7, over Ubuntu 12.04
#################################################

:date: 2013-04-10 15:30
:author: guglielmo
:category: howto
:tags: solr, tomcat, ubuntu


Tomcat7
-------

Ubuntu 12.04 comes with tomcat_ easily installable as a package (you need jdk)::

    apt-get install default-jdk tomcat7 tomcat7-admin tomcat7-user tomcat7-docs


Configure access to the web-admin in ``/etc/tomcat7/tomcat-users.xml``::

    <tomcat-users>
      <role rolename="manager-gui"/>
      <user username="manager" password="S3krEt" roles="manager-gui"/>
    </tomcat-users>

The tomcat management console is now accessible, through authentication at ``http://HOST:8080/manager/html``

Please, do change username and password in your ``tomcat-users.xml``.

.. _tomcat: http://tomcat.apache.org/


Solr
----

It can be useful to have different, isolated instances of solr_ running, corresponding to different solr versions 
(i.e. 1.2, 1.4,  3.4, ...). One of the instances could be a *multicore* solr instance, able to host multiple indexes under a single app.

This is possible by creating different **contexts** inside ``/etc/tomcat7/Catalina/localhost/``.

**open_parlamento.xml**::

    <?xml version="1.0" encoding="utf-8"?>
    <Context docBase="/home/solr/open_parlamento/apache-solr-1.4.0.war" debug="0" crossContext="true" >
       <Environment name="solr/home" type="java.lang.String" value="/home/solr/open_parlamento" override="true" />
    </Context>

**open_politici.xml**::

    <?xml version="1.0" encoding="utf-8"?>
    <Context docBase="/home/solr/open_politici/apache-solr-1.2.0.war" debug="0" crossContext="true" >
       <Environment name="solr/home" type="java.lang.String" value="/home/solr/open_politici" override="true" />
    </Context>

**multicore.xml**::

    <?xml version="1.0" encoding="utf-8"?>
    <Context docBase="/home/solr/multicore/apache-solr-3.4.0.war" debug="0" crossContext="true" >
       <Environment name="solr/home" type="java.lang.String" value="/home/solr/multicore/cores" override="true" />
    </Context>
  

Create this directory tree::
    
    /home/solr
    |- open_parlamento
    |  |- apache-solr-1.4.0.war
    |  |- data
    |  |  |- index
    |  |  |  |- ...
    |  |- conf
    |     |- admin-extra.html
    |     |- elevate.xml
    |     |- italian-stopwords.txt
    |     |- mapping-ISOLatin1Accent.txt
    |     |- protwords.txt
    |     |- schema.xml
    |     |- scripts.conf
    |     |- solrconfig.xml
    |     |- spellings.txt
    |     |- stopwords.txt
    |     |- synonyms.txt
    |- open_polis
    |  |- apache-solr-1.2.0.war
    |  |- ...
    |- multicore
       |- apache-solr.3.4.0.war
       |- cores
       |  |- solr.xml
       |  |- app1
       |  |  |- conf
       |  |- app2
       |  |  |- conf
       |- data
          |- app1
          |  |- index
          |- app2
             |- index

Note:
  You need to download the different versions of the solr war from their web site, and you may eventually need to
  download libraries, as pointed in the ``solrconfig.xml`` file to handle advanced tasks, so *your mileage may vary*.
     

**solr.xml** is the configuration file that points to the various cores in the multicore instance::
 
    <?xml version="1.0" encoding="UTF-8" ?>
    <solr persistent="false" sharedLib="lib">
      <cores adminPath="/admin/cores" shareSchema="true">
        <core name="app1"  instanceDir="app1"  dataDir="${solr.data.dir:../data}/app1" />
        <core name="app2"  instanceDir="app2"  dataDir="${solr.data.dir:../data}/app2" />
      </cores>
    </solr>

The ``conf`` directories in ``cores/appX`` are standard solr conf directories, with all files needed, according to
the solr version.
 
 
.. _solr: http://lucene.apache.org/solr/

Permissions
-----------

Tomcat is run by the ``tomcat7`` user, so all the ``data`` directories need to be writeable to this user::

    chgrp -R tomcat7 /home/solr/open_parlamento/data
    chmod -R g+w /home/solr/open_parlamento/data
    
    
Restart
-------
Is needed whenever a tomcat or solr configuration changes. Under ubuntu::

    service tomcat7 restart
    
The applications are visible under ``http://HOST:8080/APP_NAME`` where ``APP_NAME`` is the name of the context file (``open_parlamento``, ``open_politici``) or the name of the core (app1, app2).
    
