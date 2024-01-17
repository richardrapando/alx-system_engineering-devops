A report on server failure.
-A complaint reported to the engineering team that requests made to the server was returning a 500 Error resulting to delayed service delivery. It was established that the problem was from a configuration file of the web_stack_debugging_1 server

Series of events.
-11th January 11:00 am (EAT) – Problem detection. Upon notification, the engineering team quickly login to the server to try resolve the issue.
-11th January 1:00 pm (EAT) – Problem completely resolved.

Cause of problem and appropriate response.
-The unprecedented failure of the server was because the config of the software(Nginx) serving the server pages was a directory instead of a link to another config file. The config file(sites-enabled) was removed right away. The config file(sites-enabled) was then corrected to be a symbolic link to the original config file(sites-available) .This was followed by restarting the server successfully.

Correction mechanisms to prevent occurrence of problem.
•	Checking the servers regularly to ensure they are running properly.
•	Having backup servers to ensure constant service delivery  in the event of an emergency.
•	Regular testing and checking the config files before deployment.

