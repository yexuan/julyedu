#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gensim

model = gensim.models.Word2Vec.load("data/wiki.zh.text.model")

result = model.most_similar(u"足球")

result = model.similarity(u"计算机", u"自动化")

result = model.doesnt_match(u"早餐 晚餐 午餐 中心".split())

print "test over"

