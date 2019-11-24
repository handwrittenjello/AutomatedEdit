from crontab import CronTab

cron = CronTab(user='andrewlittlejohn')
job = cron.new(command='sh /Users/andrewlittlejohn/projects/AutomatedEdit/Scraper/IBJJF/ibjjf.sh')
job.hour.every(1)

cron.write()

for job in cron:
    print(job)