There is a access log available at:

`/app/access.log`

Analyze the traffic recorded in this log file and create a summary report.

Your task is to generate the following output file:

`/app/report.json`

The report must be in JSON object format containing exactly the fields listed below:

- `total_requests`
  - Format: integer
  - Description: The total number of requests found in the access log.

- `unique_clients`
  - Format: array of strings
  - Description: A list of unique client IP addresses that made requests.

- `top_path`
  - Format: string
  - Description: The page path that received the highest number of requests.

Save the completed report to:

`/app/report.json`

Do not create any additional output files.

You have 500 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.