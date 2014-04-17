#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d
import util as u

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest, self).setUp()
        u.setup(d)

    def tearDown(self):
        super(CameraTest, self).tearDown()
        u.teardown(d)

    def testTakePicture(self):
        """
        Summary:testCapturePictureAndDelete: Take a picture, then view and delete the picture.
        Steps:1. Open Camera app
              2. Capture a picture
              3. Touch thumbnail to view the picture
              4. Touch Delete button to delete the picture
              5. Exit Camera app
        """
        #Start camera and check if sucessful
        d.start_activity(component='com.intel.camera22/.Camera')
        assert d(description='Shutter button').wait.exists(timeout=5000), 'can not launch camera in 5s'

        #Take picture
        d(description='Shutter button').click.wait()
        u.sleep(5)

        d(description='Most recent photo').click.wait()
        d.click(500,500)
        assert d(description="Delete").wait.exists(timeout=3000), 'No picture to delete.'
        d(description='Delete').click.wait()
        d(text='Delete').click.wait()
        u.sleep(3)

        assert d(description="Shutter button").wait.exists(timeout=5000), 'unable back to camera after delete in 5s.'
