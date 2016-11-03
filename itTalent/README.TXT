
== Introduction ==

itTalent is a general usage datbase manager for manager IT/RD talent 
information. It works like any talent information system but it
was designed in a small scale and focus on talent's real experience only.

I hope this could be used standalone in android pad or android phone and
also in traditional web. 


    	=== license ===
	I haven't decide the license model yet. Since this is nothing but
	a specific headhunter's application it might not be very popular.
	Currently, itTalent is hosted in github, therefore, feel free to
	download and use. We will not ask for pay the usage.
	===============

== Design ==

* Leverage stable open source tools as much as possible to reduce reinventing the wheel.
	* mybatis and the generator tool for reduce the work on data access.
	* gson to manage DAO object accessed via WebCliet
	* jquery and jquery-ui for simple web UI

== Simple Web site ==
* http request for select/add/remove/modify database
* example:
	- add talent
		curl -X POST http://localhost:8080/itTalent/api/Talent/add --data "{'name':'rz','email':'somebody2@gmail.com','cellPhone':'23939889','birthYear':'2011','selfSkillDesc':'too many to mentain','desc':'simple description of my self','birthData':'1988-04-21','firstName':'Rad','lastName':'Zebra'}"
	- select talent 
		curl -X POST http://localhost:8080/itTalent/api/talent.byEmail/select --data "{'email':'gmail.com'}"
	- remove talent 
		curl -X POST http://localhost:8080/itTalent/api/Talent/delete --data "{'primarykey':'15'}"
	- update talent
		curl -X POST http://localhost:8080/itTalent/api/Talent/update --data "{'id':'11', 'name':'rz','email':'somebody2@gmail.com','cellPhone':'23939889','birthYear':'2011','selfSkillDesc':'updated! too many to mentain','desc':'simple description of my self','birthData':'1988-04-21','firstName':'Rad','lastName':'Zebra'}"
== Merge database ==



