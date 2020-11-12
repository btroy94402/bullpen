"""
Created by Brian Troy (bitroy@yahoo.com) Nov 11, 2020
Script is a generic use of the watchdog python package.
It creates a watcher on some directory ('path' below), and takes actions
when files are created, modified, moved, or deleted.

To use it, modify path location, tailor my_event_handler actions, and
launch script.
"""

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
	patterns = ["*.csv"]
	ignore_patterns = ["*.txt","*.xlsx"]
	ignore_directories = True
	case_sensitive = False
	my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
	
def on_created(event):
	print(f"hey, {event.src_path} has been created!")
	
def on_deleted(event):
	print(f"hey, {event.src_path} has been deleted!")
	
def on_modified(event):
	print(f"hey buddy, {event.src_path} has been modified")
	
def on_moved(event):
	print(f"ok, ok, someone moved {event.src_path} to {event.dest_path}")
	
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "C:\\Users\\bitro\\Desktop\\TestFolder"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	my_observer.stop()
	my_observer.join()
