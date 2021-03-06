import json
from preprocess.pipeline import *
from preprocess.writer import Writer

folder = './dataset/nlpcc'

writer = Writer(folder=folder)

pipelines = [
    StripPipeline(),
    PhonePipeline(),
    EmailPipeline(),
    UrlPipeline(),
    RemovePipeline(),
    HalfWidthPipeline(),
    LowerPipeline(),
    ReplacePipeline(),
    MaxPipeline(),
    JiebaPipeline(join_flag=' '),
]


def process():
    # train with summ
    file = './source/nlpcc/toutiao4nlpcc/train_with_summ.txt'
    f = open(file, encoding='utf-8')
    articles = []
    for line in f.readlines():
        item = json.loads(line)
        article = item.get('article')
        articles.append(article)
    
    # train without summ
    file = './source/nlpcc/toutiao4nlpcc/train_without_summ.txt'
    f = open(file, encoding='utf-8')
    for line in f.readlines():
        item = json.loads(line)
        article = item.get('article')
        articles.append(article)
    
    print(len(articles))
    
    # pre precess by pipeline
    for pipeline in pipelines:
        print('Running', pipeline)
        articles = pipeline.process_all(articles)
    
    print(len(articles))
    
    writer.write_to_txt(articles, 'articles.pretrain.txt')
