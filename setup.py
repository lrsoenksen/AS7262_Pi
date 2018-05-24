#!/usr/bin/env python

from distutils.core import setup

setup(name            = "adafruit_as7262",
      version         = "1.0.0",
      description     = "Python library to control Adafruit or Sparkfun as7262 boards",
      requires        = ['spidev'],
      author          = "Shoe-Pi and modified by Luis Soenksen",
      author_email    = "",
      maintainer      = "Luis Soenksen",
      maintainer_email= "soenksen@mit.edu",
      license         = "MIT",
      url             = "https://github.com/lrsoenksen/Adafruit_Python_AS7262",
      py_modules      = ['adafruit_as7262'],
)
