# 背景  
按天创建的es数据库，今天出现了异常，导致mapping是自动生成的。这样子，在做一些特定聚合查询的时候，
es直接报错，严重影响了生产数据的获取。  
异常来得总是那么突然，那么，我们要怎样解决这个问题？  

1. 数据转移。创建一个新的数据库，并更新其mapping  
```json
curl -x POST 'http://localhost:8888/testtmp/hotel/_mapping?' -d '
  {
        "properties": {
            "user": {
                "type": "string",
                "index": "not_analyzed"
            }
        }
    }'

````  

2. 建立别名  

```json
curl -XPOST 'http://localhost:9200/_aliases' -d '
    {
        "actions": [
            {"add": {"index": "testtmp", "alias": "test"}}
        ]
    }'
```  

至此，整个数据切换过程完成。我们可以通过查询别名查询获取到真实数据库中的数据
```json
/POST /test/_search?

{
    "_source": ["title","publishDateStr"
    ],
    "size": 50,
     "sort":{"createDate":{"order":"desc"}},
    "query": {
        "bool": {
            "must": [
            	
            ],
            "must_not": [
            
            	]
        }
    }
}
```