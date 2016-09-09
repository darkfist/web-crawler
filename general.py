import os


# create a directory for the project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project " + directory)
        os.makedirs(directory)


# create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


# create a new file
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# add data into an existing file
def append_to_file(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")


# delete the contents of an existing file
def delete_file_contents(path):
    with open(path, "w"):
        pass


# read a file and convert each line to a set items
def file_to_set(filename):
    results = set()
    with open(filename, "rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))
    return results


# convert the set into a file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
