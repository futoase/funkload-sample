# -*- coding:utf-8 -*-

import unittest
import random
import json
from funkload.FunkLoadTestCase import FunkLoadTestCase

with open('conf/user_names.json') as f:
  USER_NAMES = json.loads(f.read())

with open('conf/comments.json') as f:
  COMMENTS = json.loads(f.read())

class CommentBoard(FunkLoadTestCase):
  def setUp(self):
    self.target_url = self.conf_get('main', 'url')
    self.try_count = self.conf_getInt('comment_board_setting', 'try_count')

  def test_index(self):
    target_url = self.target_url
    try_count = self.try_count

    for i in range(try_count):
      self.get(target_url, description='Get comment board index.') 

  def test_posts(self):
    target_url = self.target_url + 'comment'
    try_count = self.try_count

    user_name = random.choice(USER_NAMES)
    comment = random.choice(COMMENTS)

    self.post(target_url,
      params=[
        ('user_name', user_name),
        ('comment', comment)
      ],
      description='Comment as {user_name}'.format(user_name=user_name)
    )

if __name__ == '__main__':
  unittest.main()
