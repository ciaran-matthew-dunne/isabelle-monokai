#!/usr/bin/env bash

preferences="$(isabelle getenv -b ISABELLE_HOME_USER)/etc/preferences"
properties="$(isabelle getenv -b JEDIT_SETTINGS)/properties"
python merge-settings.py $preferences $properties