Posted by: Yusra Hassan 2024-05-08


On May 6th, 2024, users reported a significant slowdown in accessing the Yaquut network website in Saudi Arabia, specifically while browsing internet package options. The issue stemmed from a database bottleneck caused by a sudden surge in traffic. The incident was mitigated by scaling up the database infrastructure and implementing caching mechanisms to enhance performance.
Outage Duration: May 6th, 2024. 14:30 AST – 16:45 AST (approximately 2 hours, 15 minutes).

Timeline: (all time in AST - Arabia Standard Time)

2024-05-06 14:30: Reports of slow website performance begin to surface, particularly when accessing internet package options.
2024-05-06 14:35: Operations team receives alerts and initiates investigation.
2024-05-06 14:40: Database performance degradation identified as the underlying cause.
2024-05-06 14:45: Immediate action taken by restarting database servers to alleviate performance issues temporarily.
2024-05-06 15:00: Traffic analysis reveals a sudden surge in user requests, exacerbating the database bottleneck.
2024-05-06 15:10: Decision made to scale up the database infrastructure by adding additional read replicas and increasing server capacity.
2024-05-06 15:30: New database instances provisioned and configurations updated to accommodate higher traffic demands.
2024-05-06 16:00: Caching mechanisms deployed to offload database traffic and improve response times for frequently accessed pages.
2024-05-06 16:30: Monitoring confirms improved performance and system stability.
2024-05-06 16:45: Incident resolved, normal website operations restored.
2024-05-07 10:00: Postmortem meeting conducted.

Impact:

Customer Impact: Approximately 15,000 users encountered slow website performance, especially when browsing internet package options. Certain pages experienced intermittent unavailability during the peak of the incident.
Business Impact: The slowdown led to a temporary decrease in user engagement and potential revenue loss. Customer support channels experienced a higher volume of inquiries and complaints.

Root Cause(s):

	Technical Cause: Sudden increase in user traffic overwhelmed the existing database infrastructure, resulting in performance degradation and extended response times.
	Contributing Factors: Inadequate database capacity planning and failure to anticipate and address unexpected spikes in traffic.

	Corrective Actions:

	Immediate Fixes: Database servers restarted to alleviate immediate performance impact temporarily.
	Infrastructure Scaling: Additional read replicas provisioned, and server capacity increased to accommodate higher traffic loads.
	Caching Mechanisms: Implemented caching mechanisms to reduce database load and enhance response times for frequently accessed pages.
	Monitoring and Alerting: Enhanced monitoring and alerting systems implemented to detect and respond to performance bottlenecks more proactively.

	Preventative Measures:

	Capacity Planning: Develop a robust capacity planning strategy to forecast and handle sudden spikes in traffic effectively.
	Load Testing: Conduct regular load testing to identify performance limitations and validate scalability measures.
	Auto-scaling: Explore the possibility of implementing auto-scaling mechanisms to dynamically adjust resources based on traffic patterns.

	Lessons Learned:

	Scalability and Capacity Planning: Critical to maintain a scalable infrastructure and anticipate potential traffic spikes to prevent performance degradation during peak periods.
	Monitoring and Alerting: Strengthen monitoring capabilities and establish proactive alerting systems to detect and address issues promptly.
	Load Testing: Regular load testing essential to identify performance bottlenecks and validate scalability measures effectively.
	Communication:

Internal: Operations team utilized a dedicated incident response channel in Slack to facilitate real-time collaboration and updates.
External: Regular status updates communicated via social media platforms and a public status page to keep users informed about the ongoing incident and resolution progress

