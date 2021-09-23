import sys
import re

# Takes the path of a plain text file of =-seperated settings values
# and returns a list of setting-value pairs
def get_settings(path):
  return [ re.sub(r" |\n",'', l).split('=')
            for l in open(path).readlines()
            if l[0] not in ['#','('] and l != '\n' ]

# Looks up 'key' in 'settings', returning the value if found, and NONE otherwise
def lookup_val(key, settings):
  return next((kv[1] for kv in settings if kv[0] == key), 'NONE')

# Updates values in s1 with those with the same keys in s2
def merge_settings(s1, s2):
  return [ [kv[0], (lookup_val(kv[1], s2) if lookup_val(kv[1], s2) != 'NONE' else kv[1])] 
            for kv in s1]

# Exports a settings keyval list into a filepath
def export_settings(settings, path):
  new_settings = open(path, "w+") 
  for kv in settings:
    new_settings.write(kv[0] + " = " + kv[1] + "\n")

# Reading settings from files into key-value lists
isa_prefs = get_settings(sys.argv[1])
dark_prefs = get_settings("colour-preferences")
jedit_props = get_settings(sys.argv[2])
dark_props = get_settings("jedit-properties")

# Merging and exporting settings
export_settings(merge_settings(isa_prefs, dark_prefs), "new_preferences")
export_settings(merge_settings(jedit_props, dark_props), "new_properties")


