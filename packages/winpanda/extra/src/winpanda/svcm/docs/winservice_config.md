## Description of the configuration file fields

| parameter  | description | default |type
| :------------- | :------------- |:---------------:|:--------|
||`Application` |||
|serviceName|service name|*none*|string|
|Application|the path to the application (or script)|*none*|string
|AppDirectory|startup directory|*directory containing the application*|string
||`Details` ||
|DisplayName|display name|*service name*|string
|Description|description|*none*|string
|Start|startup type|*automatic startup at boot*|LIST
||`Dependencies` |||
|DependOnService|any services which must be started before the the service can run|*none*|string|
||`Process` |||
|AppPriority|process priority|*NORMAL_PRIORITY_CLASS*|LIST|
|AppAffinity|CPU affinity for the application|*All*|int|
||`Stop methods and timeouts` |||
|AppStopMethodConsole||*1500*|ms|
|AppStopMethodWindow||*1500*|ms|
|AppStopMethodThreads||*1500*|ms|
|AppStopMethodSkip||*0*||
||`action on exit for the service` |||
|AppThrottle||*1500*|ms|
|AppExit ||*Default Restart*|LIST|
|AppStopMethodThreads||*1500*|ms|
|AppRestartDelay||*0*|ms|
||` I/O redirection` ||
|AppStdout|Output (stdout)|*none*|string
|AppStderr|Error (stderr)|*none*|string
||`File rotation` ||
|AppRotateFiles ||*name*|1 or 0
|AppRotateOnline ||*none*|1 or 0
|AppRotateSeconds||*none*|sec
|AppRotateBytes||*none*|kB
||`Environment` ||
|AppEnvironmentExtra|environment variables|*none*|string


## List *Start* parameters

| parameter  | description | 
| :------------- | :------------- |
|SERVICE_AUTO_START| Automatic startup at boot |
|SERVICE_DELAYED_START| Delayed startup at boot|
|SERVICE_DEMAND_START| Manual startup|
|SERVICE_DISABLED| Service is disabled|

## Example (diagnostic.nssm)


```ini
[main]
servicename = dcos-diagnostics
DisplayName = dcos-diagnostics
Description = diagnostics windows-node
Application = c:\dcos\dcos-diagnostics.exe
AppDirectory = c:\dcos
AppParameters = --config dcos-diagnostics-config.json --role=agent daemon
DependOnService = mesos-agent
Start = SERVICE_AUTO_START
AppStdout = c:\dcos\mesos-logs\dcos-diagnostics.log
AppStderr = c:\dcos\mesos-logs\dcos-diagnostics.log
AppEnvironmentExtra = DCOS_VERSION=13.3
```
