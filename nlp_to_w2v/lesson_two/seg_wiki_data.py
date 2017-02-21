#!/usr/bin/env python
# -*- coding: utf-8 -*-
# process_wiki_data.py 用于解析XML，将XML的wiki数据转换为text格式
import logging
import os.path
import sys

import jieba as jieba
from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    # check and process input arguments
    if len(sys.argv) < 3:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = " "
    i = 0
    output = open(outp, 'a')
    for line in open(inp,'r'):
        try:
            seg_list = jieba.cut(line,cut_all=False)
            seg_line = space.join(seg_list)
            output.write(seg_line.encode('utf-8'))
            output.write("\n")
            i += 1
            if i % 10000 == 0:
                logger.info("Saved " + str(i) + " articles")
        except Exception as e:
            print e.message
    output.close()
    logger.info("Finished Saved " + str(i) + " articles")