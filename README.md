# open-bas
FUTURE conecept idea when life permits finding the time to create a free and open source building automation system (BAS) server to run on Linux that would integrate a local operations technology (OT) BACnet devices on a LAN only through BACnet.

## Writeup:
* [linkedin story](https://www.linkedin.com/pulse/can-bas-industry-evolve-removing-things-like-value-ben-bartling%3FtrackingId=qsEcSqfdTHaN%252BMtpb%252FMmIg%253D%253D/?trackingId=qsEcSqfdTHaN%2BMtpb%2FMmIg%3D%3D)
  
## GOALS
* To be free and open source inspired by Home Assistant
* Minimalistic global share logic to BACnet devices for outside air temperature and zone level information to air handling unit systems (AHU)
* Dirt simple web app that can handle a drag and drop calendar for time-of-week equipment run scheduling. Under the hood the calendar would be linked up via BACnet protocol to occupancy point/objects in devices same way as propreitary BAS do in handling equipment run schedules.
* Alarm dashboard through BACnet
* Chart some historical data based on caching, IE., such as a days data only which is common for building operators to only look back on a day at most for troubleshooting purposes. IoT would be required for long term data storage which should the mechanism for long term data storage where on the cloud analytics and fault rules can be ran.


## Author

[LinkedIn](https://www.linkedin.com/in/ben-bartling-510a0961/)

## Legal Stuff

**Disclaimer:** The operation and implementation of this application are the sole responsibility of the person who chooses to set it up. The author and affiliates of this app are not liable for any consequences or incidents that may arise from the use of this application.

**Cybersecurity Notice:** This application is designed exclusively for use in operational technology (OT) environments that do not reside on the internet or have internet connectivity. It does not incorporate cybersecurity measures for internet-facing or IoT (Internet of Things) applications. 

Users are advised that the security of the application is limited to its use within isolated OT networks. The creator of this app and its affiliates are not responsible for cybersecurity incidents that result from poor IT practices, misconfiguration, or the use of this application in conjunction with internet-connected devices or applications.

It is essential to acknowledge that any negative outcomes, including but not limited to equipment damage, indoor air quality issues, or personal injuries, are the responsibility of the person or firm who deploys and operates the application within a building. Users are strongly encouraged to thoroughly evaluate and assess the application's suitability for their specific use case, implement appropriate cybersecurity measures where necessary, and take all required precautions to ensure safe and effective utilization.

## License

【MIT License】

Copyright 2023 Ben Bartling

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


