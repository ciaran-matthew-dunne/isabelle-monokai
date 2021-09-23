import sys
import re

# Takes the path of a plain text file of =-seperated settings values
# and returns a list of setting-value pairs
def get_settings(path):
  file = open(path)
  settings = [ re.sub(r" |\n",'', l).split('=')
            for l in file.readlines()
            if l[0] not in ['#','('] and l != '\n' ]
  file.close()
  return settings

# Looks up 'key' in 'settings', returning the value if found, and NONE otherwise
def lookup_val(key, settings):
  return next((kv[1] for kv in settings if kv[0] == key), 'NONE')

# Updates values in s1 with those with the same keys in s2

def merge_settings(s1, s2):
  dom = lambda xss: map (lambda xs : xs[0], xss)
  unmodified = [ [key, lookup_val(key, s1)] for key in set(dom(s1)) - set(dom(s2)) ]
  updated = [ [key, lookup_val(key, s2)] for key in set(dom(s2))]
  return unmodified + updated

# Exports a settings keyval list into a filepath
def export_settings(settings, path):
  new_settings = open(path, "w+") 
  for kv in settings:
    new_settings.write(kv[0] + " = " + kv[1] + "\n")
  new_settings.close()  

# Reading settings from files into key-value lists
isa_prefs = get_settings(sys.argv[1])
dark_prefs = get_settings("colour-preferences")
jedit_props = get_settings(sys.argv[2])
dark_props = get_settings("jedit-properties")

# Merging and exporting settings
export_settings(merge_settings(isa_prefs, dark_prefs), "new_preferences")
export_settings(merge_settings(jedit_props, dark_props), "new_properties")


