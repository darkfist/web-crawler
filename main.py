import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

print("\nWelcome to this python Web Crawler. \n")
project_name = input("Give a name to this project: ")
homepage = input("Enter the url you want to crawl: ")
domain_name = get_domain_name(homepage)
queue_file = project_name + "/queue.txt"
crawled_file = project_name + "/crawled.txt"
number_of_spiders = 4
queue = Queue()
Spider(project_name, homepage, domain_name)


# spider threads
def spiders():
    for i in range(number_of_spiders):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# do the next job in queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done


# job for the spiders
def jobs():
    for link in file_to_set(queue_file):
        queue.put(link)
    queue.join()
    crawl()


# crawl all the links in the queue
def crawl():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue")
        jobs()

spiders()
crawl()
